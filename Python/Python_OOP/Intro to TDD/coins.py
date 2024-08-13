def coins(cents):
    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10
    
    nickels = cents // 5
    cents %= 5
    
    pennies = cents
    
    return [quarters, dimes, nickels, pennies]

import unittest

class TestCoins(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])

    def test_case_2(self):
        self.assertEqual(coins(99), [3, 2, 0, 4])

    def test_case_3(self):
        self.assertEqual(coins(41), [1, 1, 1, 1])

    def test_case_4(self):
        self.assertEqual(coins(0), [0, 0, 0, 0])

    def test_case_5(self):
        self.assertEqual(coins(1), [0, 0, 0, 1])

    def test_case_6(self):
        self.assertEqual(coins(5), [0, 0, 1, 0])

if __name__ == '__main__':
    unittest.main()
