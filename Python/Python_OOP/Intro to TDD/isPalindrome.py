def isPalindrome(word):
    return word == word[::-1]

import unittest

class TestIsPalindrome(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(isPalindrome("racecar"))

    def test_case_2(self):
        self.assertFalse(isPalindrome("hello"))

    def test_case_3(self):
        self.assertTrue(isPalindrome("madam"))

    def test_case_4(self):
        self.assertFalse(isPalindrome("palindrome"))

    def test_case_5(self):
        self.assertTrue(isPalindrome("level"))

    def test_case_6(self):
        self.assertTrue(isPalindrome(""))

if __name__ == '__main__':
    unittest.main()

