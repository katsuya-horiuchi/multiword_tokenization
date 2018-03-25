# -*- coding: utf-8 -*-

"""Multi-word tokenization

Author: Katsuya Horiuchi
License: Apache License 2
"""

from __future__ import print_function
from copy import deepcopy
import re


class MultiWordTokenizer:
    """Multi-word tokenization

    This module allows you to extract multi-word as one word.
    You need to prepare two things:
    1. Python function to tokenize input text
    2. List of multi-words (keywords/named entities) to extract from text

    Usage (`nltk` module is used as an example.)
    ---------------------------------------------------------------------------
    >>> from nltk.tokenize import word_tokenize
    >>> keywords = ['New York', 'San Francisco', 'New Orleans']
    >>> text = 'A Python event was held in New York.'
    >>> mword_tokenize = MultiWordTokenizer(word_tokenize, keywords)
    >>> mword_tokenize.tokenize(text)
    ['A', 'Python', 'event', 'was', 'held', 'in', 'New York', '.']
    ---------------------------------------------------------------------------
    """

    def __init__(self, func, entities):
        """Initialization

        Arg:
            func: Python function; End-user can specify Python function to
                                   tokenize for customization
            entities: list; Pre-defined named entities
        """
        self.func = func
        self.entities = entities
        self._space = re.compile(r'\s')

    def tokenize(self, text):
        """Tokenize text while extracting keywords

        Arg:
            text: str; Input text
        Return:
            list; Tokenized text with keywords grouped as one element
        """
        tokenized = self.func(text)
        while True:
            # Replace one named entity at time until there's no more to replace
            new_tokenized = self.__replace_one_word(text, tokenized)
            if new_tokenized == tokenized:
                return new_tokenized
            else:
                tokenized = new_tokenized

    def __replace_one_word(self, text, tokenized):
        """Replace one multi-word in the input list

        This method has to be called multiple times until there's no more
        element to replace.

        Args:
            text: str; Input text
            tokenized: list; Tokenized input text
        Return:
            list; Same as `tokenized` param with one multi-word replaced as
                  one element. If no new multi-word was found, exactly the same
                  list as `tokenized` will be returned.
        """
        # Without deep copying, input list will be altered, causing a problem
        copied = deepcopy(tokenized)
        keywords = [word for word in self.entities if word in text]
        if not keywords:  # No entity was found
            return tokenized
        n_iteration = self.__get_n_iteration(keywords)
        for i in range(2, n_iteration + 1):
            for j, _ in enumerate(copied):
                try:
                    combined_str = ' '.join([copied[j + k] for k in range(i)])
                    # If `combined_str` is one of the keywords, replace
                    # multiple elements with one element
                    if combined_str in keywords:
                        copied[j] = combined_str
                        pop_index = -1
                        for k in range(1, i):
                            if pop_index == -1:
                                pop_index = j + k
                            copied.pop(pop_index)
                        return copied
                except IndexError:
                    break
        return copied

    def __get_n_iteration(self, keywords):
        """Get the length of the longest keyword, aka the number of iteration

        Getting this number is very important.
        This is because you can connect all the words in the list and check if
        that random string is a named entity, which consumes unnecessary time
        looping.
        If `n_iteration` is 3, all you have to do is to connect 2 or 3 elements
        in the list and see if the created string exist in the list of the
        named entities. It'll save a lot of time.

        Arg:
            keywords: list; Keywords
        Return:
            int; Word count of the longest keyword
        """
        n_iteration = 0
        for element in keywords:
            spaces = self._space.findall(element)
            if spaces:
                if len(spaces) + 1 > n_iteration:
                    n_iteration = len(spaces) + 1
        return n_iteration
