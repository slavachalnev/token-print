# token-print
Colourful tokenized text.

`token_print` uses `termcolor` to display tokenized text in different background colors. Inspired by [OpenAI's tokenizer playground](https://platform.openai.com/tokenizer).


## Installation

```bash
pip install git+https://github.com/slavachalnev/token-print.git
```

## Usage

```python
from transformers import AutoTokenizer
from token_print import ColoredTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
text = "The quick brown fox jumps over the lazy dog."

ct = ColoredTokenizer(tokenizer)
ct(text)
```

## Test
```bash
pytest -s tests
```