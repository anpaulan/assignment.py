#Used GPT To help create this file
import unittest
from assignment import bubble_srt, selection_sort, insertion_sort, algo_time

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_cases = {
            'sorted': [1, 2, 3, 4, 5, 66, 77, 88, 99, 101],
            'reverse_sorted': [9, 8, 7, 6, 5, 4, 3, 2, 1],
            'random': [1, 5, 54, 56, 1, 45, 456, 786, 456, 12, 75654, 4547, 4564, 13021, 76345, 4, 44]
        }

    def test_bubble_sort(self):
        for case, data in self.test_cases.items():
            with self.subTest(case=case):
                sorted_data = bubble_srt(data.copy())
                self.assertEqual(sorted_data, sorted(data))

    def test_selection_sort(self):
        for case, data in self.test_cases.items():
            with self.subTest(case=case):
                sorted_data = selection_sort(data.copy())
                self.assertEqual(sorted_data, sorted(data))

    def test_insertion_sort(self):
        for case, data in self.test_cases.items():
            with self.subTest(case=case):
                sorted_data = insertion_sort(data.copy())
                self.assertEqual(sorted_data, sorted(data))

if __name__ == '__main__':
    unittest.main()
