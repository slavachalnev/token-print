from setuptools import setup, find_packages

setup(
    name='token_print',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'termcolor',
    ],
    author='Sviatoslav Chalnev',
    author_email='slava.chalnev@gmail.com',
    description='Display tokenized text.',
)
