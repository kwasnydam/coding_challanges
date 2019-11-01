#!/bin/python3
# Problem description: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/
# GitHub: https://github.com/kwasnydam

from collections import deque
EDGE_WEIGHT = 6

class Graph:

    def __init__(self, num_of_nodes):
        self.n = num_of_nodes
        self.edges = {str(node_id): [] for node_id in range(num_of_nodes)}

    def connect(self, source_id, target_id):
        try:
            s_id = str(source_id)
            t_id = str(target_id)
            self.edges[s_id].append((source_id, target_id))
            self.edges[t_id].append((target_id, source_id))
        except KeyError as e:
            raise KeyError('No node ith id {} or {}'.format(source_id, target_id))

    def find_all_distances(self, start_node_id):
        starting_edges = self._get_starting_edges(start_node_id)
        distances = self._find_all_distances(starting_edges)
        distances = self._remove_starting_node_from_distances(distances, start_node_id)
        distances = self._replace_unreachable_nodes_with_minus_1(distances)
        result = ' '.join(str(x) for x in distances)
        print(result)
        return result

    def _get_starting_edges(self, start_id):
        try:
            start = self.edges[str(start_id)]
        except KeyError as e:
            raise KeyError('No node with id {}'.format(start_id))
        return start

    def _find_all_distances(self, starting_edges):
        distances = [0 for _ in range(self.n)]
        discovered = deque()
        discovered.append(starting_edges)
        traversed =set()

        while discovered:
            edges = discovered.popleft()
            for edge in edges:
                if edge not in traversed:
                    if distances[edge[0]] + EDGE_WEIGHT <= distances[edge[1]] or distances[edge[1]] == 0:
                        distances[edge[1]] = distances[edge[0]] + EDGE_WEIGHT
                    discovered.append(self.edges[str(edge[1])])
                    traversed.add(edge)
                    traversed.add((edge[1], edge[0]))
        return distances

    def _remove_starting_node_from_distances(self, distances, start_node_id):
        return distances[0:start_node_id] + distances[start_node_id+1:]

    def _replace_unreachable_nodes_with_minus_1(self, distances):
        for index, distance in enumerate(distances):
            if distance == 0:
                distances[index] = -1
        return distances
