import torch

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

    ct = ColoredTokenizer(tokenizer, custom_colors=['on_green', 'on_red', 'on_blue'])
    ct(text)

def test_list_of_strings():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    texts = ["First sentence.", "Second sentence."]

    ct = ColoredTokenizer(tokenizer)
    ct.print(texts)

def test_list_of_integers():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    text = "The quick brown fox jumps over the lazy dog."
    token_ids = tokenizer.encode(text, add_special_tokens=False)
    print(token_ids)

    ct = ColoredTokenizer(tokenizer)
    ct.print(token_ids)

def test_list_of_lists_of_integers():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    texts = ["Fisrt sentence.", "Another sentence."]
    batch_token_ids = [tokenizer.encode(text, add_special_tokens=False) for text in texts]
    print(batch_token_ids)

    ct = ColoredTokenizer(tokenizer)
    ct.print(batch_token_ids)

def test_tensor_input():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    text = "The quick brown fox jumps over the lazy dog."
    # token_ids = torch.tensor(tokenizer.encode(text, add_special_tokens=False))
    token_ids = tokenizer.encode(text, add_special_tokens=False, return_tensors='pt').squeeze(0)
    print(token_ids)

    ct = ColoredTokenizer(tokenizer)
    ct.print(token_ids)

def test_batch_tensor_input():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    texts = ["The quick brown fox", "Jumps over the"]
    batch_token_ids = torch.tensor([tokenizer.encode(text, add_special_tokens=False) for text in texts])

    ct = ColoredTokenizer(tokenizer)
    ct.print(batch_token_ids)
