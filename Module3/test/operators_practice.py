import unittest


class OperatorsTest(unittest.TestCase):

# test equal operator
    def test_equals_operators(self):
        a = -7
        b = -2
        self.assertFalse(a == b)
# test less than operator
    def test_notequal_operator(self):
        a = 7
        b = 8
        self.assertTrue(a != b)

# test greater than operator
    def test_greaterthan_operator(self):
        a = 20
        b = 10
        self.assertTrue(a > b)

# test less than operator
    def test_lessthan_operator(self):
        a = 10
        b = 20
        self.assertTrue(a < b)

# test greater than or equal operator
    def test_greaterequal_operator(self):
        a = 4
        b = 5
        self.assertFalse(a >= b)

# test less than equal operator
    def test_lessequal_operator(self):
        a = 4
        b = 5
        self.assertTrue(a <= b)


if __name__ == '__main__':
    unittest.main()
