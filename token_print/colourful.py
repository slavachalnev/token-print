from termcolor import colored

def print_colorful_text(text):
    words = text.split()
    for word in words:
        if word == "red":
            print(colored(word, 'red'), end=' ')
        elif word == "green":
            print(colored(word, 'green'), end=' ')
        else:
            print(word, end=' ')
    print()  # Newline after printing all words
