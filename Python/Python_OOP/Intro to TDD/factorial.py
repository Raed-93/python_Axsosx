def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

import unittest

class TestFactorial(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(factorial(5), 120)  # 5! = 120
    
    def test_case_2(self):
        self.assertEqual(factorial(0), 1)  # 0! = 1
    
    def test_case_3(self):
        self.assertEqual(factorial(1), 1)  # 1! = 1
    
    def test_case_4(self):
        self.assertEqual(factorial(6), 720)  # 6! = 720
    
    def test_case_5(self):
        self.assertEqual(factorial(3), 6)  # 3! = 6

if __name__ == '__main__':
    unittest.main()
