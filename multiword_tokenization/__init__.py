# -*- coding: utf-8 -*-

"""Multi-word tokenization

This module allows you to extract multi-word as one word.
You need to prepare two things:
1. Python function to tokenize input text
2. List of multi-words (keywords/named entities) to extract from text

Usage
-------------------------------------------------------------------------------
>>> from nltk.tokenize import word_tokenize
>>> keywords = ['New York', 'San Francisco', 'New Orleans']
>>> text = 'A Python event was held in New York.'
>>> mword_tokenize = MultiWordTokenizer(word_tokenize, keywords)
>>> mword_tokenize.tokenize(text)
['A', 'Python', 'event', 'was', 'held', 'in', 'New York', '.']
-------------------------------------------------------------------------------
"""

from multiword_tokenization.tokenize import MultiWordTokenizer

__all__ = ['MultiWordTokenizer']
__version__ = '0.2.0a1'
