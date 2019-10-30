import unittest

from app.Parser import Parser


class ParserUnitTest(unittest.TestCase):

    def test_unique_words(self):
        parser = Parser()
        result = parser.get_unique_words("hola si is no no")
        self.assertEqual(4, result)

    def test_unique_words_sample2(self):
        parser = Parser()
        result = parser.get_unique_words("hola si is no no casa casa casa")
        self.assertEqual(5, result)

    def test_most_repeated_word(self):
        parser = Parser()
        result = parser.get_most_reapeated_word("hola si is no no casa casa casa")
        self.assertEqual("casa", result)

    def test(self):
        test = dict()
        test["a"] = 4
        test["b"] = 3

        result = sorted(test.items(), key=lambda tuple: tuple[1])
        print(type(result))
