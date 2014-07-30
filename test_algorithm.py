import unittest
from algorithm import Algorithm


class LanguageTest(unittest.TestCase):

    def setUp(self):
        self.message = "Dit is een fijn bericht"
        self.algorithm = Algorithm(self.message)

    def test_algorithm(self):
        """
        Only test for words that are 4 characters or more
        """
        self.assertEqual(self.algorithm._determine_keywords(), ['fijn', 'bericht'])

    def test_determine_language(self):
        self.assertEqual(self.algorithm.determine_language(), 'nl')

if __name__ == '__main__':
    unittest.main()