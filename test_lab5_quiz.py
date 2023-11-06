# Save this as test_quiz_lab5.py in the tests directory

import unittest
from lab5_quiz import _filter, _map, all_are_positive_2

class TestQuizLab5(unittest.TestCase):
    
    def test_filter(self):
        self.assertEqual(list(_filter(lambda x: x % 2 == 0, range(10))), [0, 2, 4, 6, 8])
        self.assertEqual(list(_filter(None, [True, False, True])), [True, True])
        self.assertEqual(list(_filter(lambda x: x > 5, [3, 4, 5, 6, 7])), [6, 7])

    def test_map(self):
        self.assertEqual(list(_map(lambda x: x * 2, range(5))), [0, 2, 4, 6, 8])
        self.assertEqual(list(_map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])), [5, 7, 9])

    def test_all_are_positive_2(self):
        self.assertTrue(all_are_positive_2([1, 2, 3]))
        self.assertFalse(all_are_positive_2([1, -2, 3]))
        self.assertTrue(all_are_positive_2([10, 20, 30, 40]))

if __name__ == '__main__':
    unittest.main()
