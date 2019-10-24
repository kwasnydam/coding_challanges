import unittest
import array_inversions_count

class TestCountInversions(unittest.TestCase):

    def setUp(self):
        self.object_under_test =  array_inversions_count.count_inversions

    def test_should_return_3_on_input_135246(self):
        test_data = [1, 3, 5, 2, 4, 6]
        expected_value = 3
        self._test_inversions_count(test_data, expected_value)

    def test_should_return_0_on_sorted_input(self):
        test_data = [1, 2, 3, 4, 5, 6]
        expected_value = 0
        self._test_inversions_count(test_data, expected_value)

    def test_should_return_0_on_1_element_input(self):
        test_data = [1]
        expected_value = 0
        self._test_inversions_count(test_data, expected_value)

    def test_should_return_15_on_654321_input(self):
        test_data = [6, 5, 4, 3, 2, 1]
        expected_value = 15
        self._test_inversions_count(test_data, expected_value)

    def _test_inversions_count(self, test_data, expected_value):
        test_result, _ = self.object_under_test(test_data)
        self.assertEqual(test_result, expected_value, 'Assertion Failed: Actual: {},  Expected: {}'.format(
        test_result, expected_value
        ))



if __name__=='__main__':
    unitetest.main()
