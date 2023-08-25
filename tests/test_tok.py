from transformers import AutoTokenizer
from token_print.colourful import print_colored_tokens


def test_tokenization():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    text = "The quick brown fox jumps over the lazy dog."

    print_colored_tokens(text, tokenizer)
