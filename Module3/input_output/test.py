import unittest
import unittest.mock as mock
import input_output.topic2 as topic2


class MyTestCase(unittest.TestCase):

    def test_quit(self):

        with mock.patch('builtins.input', return_value="yes"):
            assert topic2.yes_or_no() == "Sorry to see you go!"

        with mock.patch('builtins.input', return_value="no"):
            assert topic2.yes_or_no() == "Awesome!"

        with mock.patch('builtins.input', return_value="123"):
            assert topic2.yes_or_no() == "BAD INPUT!"


if __name__ == '__main__':
    unittest.main()
