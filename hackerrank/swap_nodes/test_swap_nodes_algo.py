import unittest
import os
from source import swap_nodes_algo


class TestSwapNodes(unittest.TestCase):

    def test_100_nodes_45_queries(self):
        test_input_filepath = os.path.join(os.path.abspath('.'), 'test_input_1.txt')
        with open(test_input_filepath) as fp:
            indexes, queries, expected_results = self.parse_file(fp)

        print('testing with:\nindexes = {}\nqueries = {}'.format(
        indexes, queries
        ))

        results = swap_nodes_algo.swapNodes(indexes, queries)
        line = 0
        for line_result, line_expected in zip(results, expected_results):
            self.assertListEqual(line_result, line_expected, 'Error at line = {}'.format(line))
            line+=1

    def parse_file(self, file):
        n = int(file.readline())
        indexes = []
        for _ in range(n):
            line = file.readline()
            indexes.append(list(map(int, line.rstrip().split())))

        queries_count = int(file.readline())
        queries = []
        for _ in range(queries_count):
            queries_item = int(file.readline())
            queries.append(queries_item)

        results = []
        for _ in range(queries_count):
            line = file.readline()
            results.append(list(map(int, line.rstrip().split())))

        return indexes, queries, results

if __name__=='__main__':
    unitetest.main()
