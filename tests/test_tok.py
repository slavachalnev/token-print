from transformers import AutoTokenizer
from token_print import ColoredTokenizer


def test_tokenization():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    text = "The quick brown fox jumps over the lazy dog."

    ct = ColoredTokenizer(tokenizer)
    ct(text)

def test_custom_colors():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    text = "The quick brown fox jumps over the lazy dog."

    ct = ColoredTokenizer(tokenizer, colors=['on_green', 'on_red', 'on_blue'])
    ct(text)
