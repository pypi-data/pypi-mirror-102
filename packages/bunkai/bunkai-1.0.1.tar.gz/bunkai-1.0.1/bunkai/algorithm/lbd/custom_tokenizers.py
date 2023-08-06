#!/usr/bin/env python3

import collections
import logging
import os
import typing
import unicodedata

from janome.tokenizer import Tokenizer
from transformers.file_utils import cached_path
from transformers.models.bert.tokenization_bert import (BertTokenizer,
                                                        WordpieceTokenizer,
                                                        load_vocab)

import bunkai.constant

"""MecabではなくJanomeに合わせて作成されたTokenizer
The original source code is from cl-tohoku/bert-japanese.
https://github.com/cl-tohoku/bert-japanese/blob/master/tokenization.py
The original source code is under Apache-2.0 License.
"""

logger = logging.getLogger(__name__)

VOCAB_FILES_NAMES = {"vocab_file": "vocab.txt"}

PRETRAINED_VOCAB_FILES_MAP = {
    "vocab_file": {
        "cl-tohoku/bert-base-japanese":
            "https://s3.amazonaws.com/models.huggingface.co/bert/cl-tohoku/bert-base-japanese/vocab.txt",
        "cl-tohoku/bert-base-japanese-whole-word-masking":
            "https://s3.amazonaws.com/models.huggingface.co/bert/cl-tohoku/bert-base-japanese-whole-word-masking/vocab.txt",
        "cl-tohoku/bert-base-japanese-char":
            "https://s3.amazonaws.com/models.huggingface.co/bert/cl-tohoku/bert-base-japanese-char/vocab.txt",
        "cl-tohoku/bert-base-japanese-char-whole-word-masking":
            "https://s3.amazonaws.com/models.huggingface.co/bert/cl-tohoku/bert-base-japanese-char-whole-word-masking/vocab.txt",
    }
}

PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES = {
    "cl-tohoku/bert-base-japanese": 512,
    "cl-tohoku/bert-base-japanese-whole-word-masking": 512,
    "cl-tohoku/bert-base-japanese-char": 512,
    "cl-tohoku/bert-base-japanese-char-whole-word-masking": 512,
}

PRETRAINED_INIT_CONFIGURATION = {
    "cl-tohoku/bert-base-japanese": {
        "do_lower_case": False,
        "word_tokenizer_type": "janome",
        "subword_tokenizer_type": "wordpiece",
    },
    "cl-tohoku/bert-base-japanese-whole-word-masking": {
        "do_lower_case": False,
        "word_tokenizer_type": "janome",
        "subword_tokenizer_type": "wordpiece",
    },
    "cl-tohoku/bert-base-japanese-char": {
        "do_lower_case": False,
        "word_tokenizer_type": "janome",
        "subword_tokenizer_type": "character",
    },
    "cl-tohoku/bert-base-japanese-char-whole-word-masking": {
        "do_lower_case": False,
        "word_tokenizer_type": "janome",
        "subword_tokenizer_type": "character",
    },
}


class JanomeTokenizer(object):
    """Runs basic tokenization with Janome morphological parser."""

    def __init__(self, *, do_lower_case=False, never_split=None, normalize_text=True):
        """
        Construct a JanomeTokenizer.

        :arg do_lower_case: (`optional`) boolean (default True)
                Whether to lower case the input.
        :arg never_split: (`optional`) list of str
                Kept for backward compatibility purposes.
                Now implemented directly at the base class level (see :func:`PreTrainedTokenizer.tokenize`)
                List of token not to split.
        :arg normalize_text: (`optional`) boolean (default True)
                Whether to apply unicode normalization to text before tokenization.
        """
        self.do_lower_case = do_lower_case
        self.never_split = never_split if never_split is not None else []
        self.normalize_text = normalize_text
        self.janome_tokenizer = Tokenizer()

    def tokenize(self, text: str, *, never_split=None, **kwargs):
        """Tokenizes a piece of text."""
        if self.normalize_text:
            text = unicodedata.normalize("NFKC", text)

        never_split = self.never_split + (never_split if never_split is not None else [])
        tokens = self.janome_tokenizer.tokenize(text)
        __tokens = []
        last_index = 0
        for t in tokens:
            token = t.surface
            token_start = text.index(token, last_index)
            if last_index != token_start:
                __tokens.append(text[last_index: token_start])

            if self.do_lower_case and token not in never_split:
                token = token.lower()
                __tokens.append(token.lower())
            else:
                __tokens.append(token)
            last_index = token_start + len(token)

        if len(text) != last_index:
            __tokens.append(text[last_index:])

        assert text == ''.join(__tokens), f"[{text}] != [{''.join(__tokens)}]"
        return __tokens


class CharacterTokenizer(object):
    """Runs Character tokenziation."""

    def __init__(self, vocab, unk_token, normalize_text=True):
        self.vocab = vocab
        self.unk_token = unk_token
        self.normalize_text = normalize_text

    def tokenize(self, text):
        """
        Tokenize a piece of text into characters.

        For example:
            input = "apple"
            output = ["a", "p", "p", "l", "e"]
        :arg text: A single token or whitespace separated tokens.
        This should have already been passed through `BasicTokenizer`.
        :return: A list of characters.
        """
        if self.normalize_text:
            text = unicodedata.normalize("NFKC", text)

        output_tokens = []
        for char in text:
            if char not in self.vocab:
                output_tokens.append(self.unk_token)
                continue

            output_tokens.append(char)

        return output_tokens


class JanomeSubwordsTokenizer(BertTokenizer):
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    pretrained_init_configuration = PRETRAINED_INIT_CONFIGURATION
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES

    def __init__(
            self,
            vocab_file,
            *,
            subword_tokenizer_type="wordpiece",
            do_subword_tokenize: bool = True,
            never_split=None,
            unk_token="[UNK]",
            sep_token="[SEP]",
            pad_token="[PAD]",
            cls_token="[CLS]",
            mask_token="[MASK]",
            **kwargs
    ):
        """
        Construct a MecabBertTokenizer.

        :arg vocab_file: Path to a one-wordpiece-per-line vocabulary file.
        :arg do_lower_case: (`optional`) boolean (default True)
        Whether to lower case the input.
        Only has an effect when do_basic_tokenize=True.
        :arg do_word_tokenize: (`optional`) boolean (default True) Whether to do word tokenization.
        :arg do_subword_tokenize: (`optional`) boolean (default True) Whether to do subword tokenization.
        :arg word_tokenizer_type: (`optional`) string (default "basic") Type of word tokenizer. basic / janome / pre_tokenize
        :arg subword_tokenizer_type: (`optional`) string (default "wordpiece") Type of subword tokenizer.
        :arg cls_token: No description.
        """
        super(BertTokenizer, self).__init__(
            unk_token=unk_token,
            sep_token=sep_token,
            pad_token=pad_token,
            cls_token=cls_token,
            mask_token=mask_token,
            **kwargs,
        )
        if vocab_file in PRETRAINED_VOCAB_FILES_MAP['vocab_file']:
            self.vocab = load_vocab(
                cached_path(
                    PRETRAINED_VOCAB_FILES_MAP['vocab_file'][vocab_file],
                )
            )
        elif not os.path.isfile(vocab_file):
            raise ValueError(
                "Can't find a vocabulary file at path '{}'. To load the vocabulary from a Google pretrained "
                "model use `tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)`".format(vocab_file)
            )
        else:
            self.vocab = load_vocab(vocab_file)

        # add new vocab
        self.add_tokens([' ', bunkai.constant.METACHAR_LINE_BREAK])

        self.ids_to_tokens = collections.OrderedDict([(ids, tok) for tok, ids in self.vocab.items()])

        self.do_word_tokenize = False
        self.do_subword_tokenize = True
        if do_subword_tokenize:
            if subword_tokenizer_type == "wordpiece":
                self.subword_tokenizer = WordpieceTokenizer(vocab=self.vocab, unk_token=self.unk_token)
            elif subword_tokenizer_type == "character":
                self.subword_tokenizer = CharacterTokenizer(vocab=self.vocab, unk_token=self.unk_token)
            else:
                raise ValueError("Invalid subword_tokenizer_type '{}' is specified.".format(subword_tokenizer_type))

        self.janome_tokenizer = JanomeTokenizer()

    def tokenize(self, text: typing.Union[str, typing.List[str]]) -> typing.List[str]:
        if isinstance(text, str):
            morphemes = self.janome_tokenizer.tokenize(text)
        elif isinstance(text, list) and all([isinstance(t, str) for t in text]):
            morphemes = text
        else:
            raise Exception(f'Invalid input-type {text}')

        if self.do_subword_tokenize:
            split_tokens = []
            for token in morphemes:
                sts = [sub_token for sub_token in self.subword_tokenizer.tokenize(token)]
                if len(sts) == 0:
                    split_tokens.append(token)
                else:
                    split_tokens += sts
        else:
            split_tokens = morphemes

        return split_tokens
