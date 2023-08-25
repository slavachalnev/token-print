from termcolor import colored
from itertools import cycle


from transformers import AutoTokenizer
from transformer_lens import HookedTransformer


def print_colored_tokens(text: str, tokenizer):
    if not hasattr(tokenizer, 'encode'):
        raise ValueError("The provided tokenizer object must have a 'encode' method.")
    
    if not hasattr(tokenizer, 'decode'):
        raise ValueError("The provided tokenizer object must have a 'decode' method.")

    input_ids = tokenizer.encode(text, add_special_tokens=False)
    tokens = [tokenizer.decode([id], clean_up_tokenization_spaces=False) for id in input_ids]

    colors = ['on_magenta', 'on_green', 'on_yellow', 'on_red', 'on_cyan']
    color_iter = cycle(colors)

    # Iterate through tokens and print them in corresponding colors
    for token in tokens:
        color = next(color_iter)
        print(colored(token, on_color=color), end='')
    print() # New line at the end


if __name__ == '__main__':
    text = "The Eiffel Tower is located in Paris."
    tokenizer = AutoTokenizer.from_pretrained("gpt2")

    print_colored_tokens(text, tokenizer=tokenizer)
