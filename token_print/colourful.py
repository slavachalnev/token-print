from typing import Any, List
from termcolor import colored
from itertools import cycle


class ColoredTokenizer:
    def __init__(self, tokenizer, custom_colors: List[str] = None):
        if not hasattr(tokenizer, 'encode') or not hasattr(tokenizer, 'decode'):
            raise ValueError("The provided tokenizer object must have 'encode' and 'decode' methods.")

        self.tokenizer = tokenizer

        if custom_colors is None:
            self.colors = ['on_magenta', 'on_green', 'on_yellow', 'on_red', 'on_cyan']
        else:
            self.colors = custom_colors
    
    def __call__(self, input_data: Any):
        self.print(input_data)
    
    def print(self, input_data: Any):
        if isinstance(input_data, str):
            self._print_text(input_data)
        elif isinstance(input_data, list):
            if all(isinstance(item, str) for item in input_data):
                self._print_batch_texts(input_data)
            elif all(isinstance(item, int) for item in input_data):
                self._print_token_ids(input_data)
            elif all(isinstance(item, list) for item in input_data) and all(isinstance(sub_item, int) for item in input_data for sub_item in item):
                self._print_batch_token_ids(input_data)
            else:
                raise ValueError("Unsupported input type.")
        else:
            raise ValueError("Input data must be a string, list of strings, list of integers, or list of lists of integers.")

    def _print_text(self, text: str):
        input_ids = self.tokenizer.encode(text, add_special_tokens=False)
        self._print_token_ids(token_ids=input_ids)
    
    def _print_batch_texts(self, texts: List[str]):
        for text in texts:
            self._print_text(text=text)
        
    def _print_batch_token_ids(self, batch: List[List[int]]):
        for token_ids in batch:
            self._print_token_ids(token_ids=token_ids)
    
    def _print_token_ids(self, token_ids: List[int]):
        tokens = [self.tokenizer.decode([id], clean_up_tokenization_spaces=False) for id in token_ids]
        color_iter = cycle(self.colors)
        for token in tokens:
            color = next(color_iter)
            print(colored(token, on_color=color), end='')
        print()  # New line at the end
