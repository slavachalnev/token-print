from transformers import AutoTokenizer
from token_print.colourful import ColoredTokenizer


def test_tokenization():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    text = "The quick brown fox jumps over the lazy dog."

    ct = ColoredTokenizer(tokenizer)
    ct(text)
