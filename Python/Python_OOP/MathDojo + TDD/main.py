class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num + sum(nums)
        return self

    def subtract(self, num, *nums):
        self.result -= num + sum(nums)
        return self

import unittest

class TestMathDojo(unittest.TestCase):

    def setUp(self):
        self.md = MathDojo()

    def test_add(self):
        self.assertEqual(self.md.add(2).result, 2)
        self.assertEqual(self.md.add(3, 4).result, 9)
        self.assertEqual(self.md.add(1, 2, 3).result, 15)

    def test_subtract(self):
        self.md.add(10) 
        self.assertEqual(self.md.subtract(2).result, 8)
        self.assertEqual(self.md.subtract(3, 4).result, 1)
        self.assertEqual(self.md.subtract(1, 1, 1).result, -2)

if __name__ == '__main__':
    unittest.main()
