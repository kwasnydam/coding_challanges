import unittest
import os

from dfs_connected_cell_in_a_grid import maxRegion

class TestMaxRegion(unittest.TestCase):

    def parse_test_data_file(self, file):
        n = int(file.readline())
        m = int(file.readline())
        grid = []
        for _ in range(n):
            grid.append(list(map(int, file.readline().rstrip().split())))
        expected_result = int(file.readline())
        return grid, expected_result

    def test_passes_on_sample_test_cases(self):
        test_data_filenames = ['sample_test_case_{}.txt'.format(i) for i in range(3)]
        for test_data_filename in test_data_filenames:
            test_data_path = os.path.join(os.path.abspath('.'), test_data_filename)
            with open(test_data_path) as f:
                grid, expected_result = self.parse_test_data_file(f)
            res = maxRegion(grid)
            self.assertEqual(expected_result, res, 'Wrong Answer. Expected: {}, Actual: {}'.format(expected_result, res))
