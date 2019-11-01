import unittest
import os
from bfs_shortest_reach_in_graph import Graph

class TestBFSShortestReachInGraph(unittest.TestCase):

    def test_simple(self):
        test_data_path = os.path.join(os.path.abspath('.'), 'test_input_basic.txt')
        with open(test_data_path) as f:
            self._run_test_on_file(f)

    def test_when_more_then_one_path_should_return_the_lowest_distance(self):
        test_data_path = os.path.join(os.path.abspath('.'), 'test_input_two_paths_to_4.txt')
        with open(test_data_path) as f:
            self._run_test_on_file(f)

    def _run_test_on_file(self, f):
        t = int(f.readline())
        for i in range(t):
            n,m = [int(value) for value in f.readline().split()]
            graph = Graph(n)
            for i in range(m):
                x,y = [int(x) for x in f.readline().split()]
                graph.connect(x-1,y-1)
            s = int(f.readline())
            expected_results = f.readline().rstrip()
            test_results = graph.find_all_distances(s-1)
            self.assertEqual(expected_results, test_results)
