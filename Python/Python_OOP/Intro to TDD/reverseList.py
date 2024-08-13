def reverseList(lst):
    
    left = 0
    right = len(lst) - 1
    
    while left < right:
        
        lst[left], lst[right] = lst[right], lst[left]
        
        left += 1
        right -= 1
    
    return lst

import unittest

class TestReverseList(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])

    def test_case_2(self):
        self.assertEqual(reverseList([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_case_3(self):
        self.assertEqual(reverseList([7, 8, 9]), [9, 8, 7])

    def test_case_4(self):
        self.assertEqual(reverseList([]), [])

if __name__ == '__main__':
    unittest.main()
