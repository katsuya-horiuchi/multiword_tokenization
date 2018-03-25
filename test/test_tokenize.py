# -*- coding: utf-8 -*-

import unittest

from nltk.tokenize import word_tokenize

from multiword_tokenization import MultiWordTokenizer


class TestMultiWordTokenizer(unittest.TestCase):

    def setUp(self):
        _keywords = [
            'New York', 'San Francisco', 'New Orleans',
            'Python programming language', 'Guido van Rossum',
            'Python Software Foundation'
        ]
        self.instance = MultiWordTokenizer(word_tokenize, _keywords)

    def test_tokenize1(self):
        self.assertEqual(
            self.instance.tokenize('A Python event was held in New York.'),
            ['A', 'Python', 'event', 'was', 'held', 'in', 'New York', '.']
        )

    def test_tokenize2(self):
        self.assertEqual(
            self.instance.tokenize(
                ('Python programming language is an awesome language, '
                 'created by Guido van Rossum.')
            ),
            ['Python programming language', 'is', 'an', 'awesome',
             'language', ',', 'created', 'by', 'Guido van Rossum', '.']
        )


if __name__ == '__main__':
    unittest.main()
