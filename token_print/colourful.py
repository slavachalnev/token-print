from typing import Any, List
from termcolor import colored
from itertools import cycle


class ColoredTokenizer:
    def __init__(self, tokenizer, colors: List[str] = None):
        if not hasattr(tokenizer, 'encode') or not hasattr(tokenizer, 'decode'):
            raise ValueError("The provided tokenizer object must have 'encode' and 'decode' methods.")

        self.tokenizer = tokenizer

        if colors is None:
            self.colors = ['on_magenta', 'on_green', 'on_yellow', 'on_red', 'on_cyan']
        else:
            self.colors = colors
    
    def __call__(self, text: str):
        self.print(text=text)

    def print(self, text: str):
        input_ids = self.tokenizer.encode(text, add_special_tokens=False)
        tokens = [self.tokenizer.decode([id], clean_up_tokenization_spaces=False) for id in input_ids]

        color_iter = cycle(self.colors)

        # Iterate through tokens and print them in corresponding colors
        for token in tokens:
            color = next(color_iter)
            print(colored(token, on_color=color), end='')
        print()  # New line at the end
