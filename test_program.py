from parse_messages import validate_file, validate_contents, parse_file
import unittest


class ProgramTest(unittest.TestCase):

    def setUp(self):
        self.file = open('test.txt')

    def test_file_input_is_txt(self):
        self.assertTrue(validate_file(self.file))

    def test_file_input_multiple_dots(self):
        multi_dot_file = open('test.tmp.txt')
        self.assertTrue(validate_file(multi_dot_file))

    def test_contents_is_json(self):
        json_string = '{"name": "Jonas"}'
        self.assertTrue(validate_contents(json_string))

    def test_parse_file(self):
        self.assertEqual(parse_file(self.file), 'nl')