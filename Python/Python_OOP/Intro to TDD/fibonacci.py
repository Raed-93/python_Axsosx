def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

import unittest

class TestFibonacci(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(fibonacci(0), 0)  # fib(0) = 0
    
    def test_case_2(self):
        self.assertEqual(fibonacci(1), 1)  # fib(1) = 1
    
    def test_case_3(self):
        self.assertEqual(fibonacci(5), 5)  # fib(5) = 5
    
    def test_case_4(self):
        self.assertEqual(fibonacci(6), 8)  # fib(6) = 8
    
    def test_case_5(self):
        self.assertEqual(fibonacci(7), 13)  # fib(7) = 13

if __name__ == '__main__':
    unittest.main()