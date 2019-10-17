#!/bin/python3

import os
import queue

class Node:

    def __init__(self, value, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return '{}'.format(self.value)

class Tree:

    def __init__(self, root):
        self.root = root
        self._depth = None
        self._levels_nodes_map = None

    def swap_child_on_level(self, level):
        nodes_on_level = self.get_nodes_on_level(level)
        for node in nodes_on_level:
            temp = node.left_child
            node.left_child = node.right_child
            node.right_child = temp

    def get_nodes_on_level(self, level):
        if self._levels_nodes_map is None:
            self._explore_tree()
        if str(level) in self._levels_nodes_map:
            return self._levels_nodes_map[str(level)]
        else:
            raise ValueError('level = {} not found in the tree'.format(level))

    def get_depth(self):
        if self._depth is None:
            self._explore_tree()
        return self._depth

    def in_order(self):
        current = self.root
        stack = []
        result = []
        while True:
            # reach the leaf of the left subtree
            if current is not None:
                stack.append(current)
                current = current.left_child
            # leaf reached: get the value and check right subtree
            elif stack:
                current = stack.pop()
                result.append(current.value)
                current = current.right_child
            else:
                break
        return result


    def _explore_tree(self):
        # perform bfs with level retrieval
        root = self.root
        discovered_nodes = queue.Queue()
        level_nodes_map = {}
        level = 1
        discovered_nodes.put(root)
        discovered_nodes.put(None)
        while not discovered_nodes.empty():
            node = discovered_nodes.get()
            if node is None:
                if not discovered_nodes.empty():
                    discovered_nodes.put(None)
                    level += 1
            else:
                if node.left_child is not None:
                    discovered_nodes.put(node.left_child)
                if node.right_child is not None:
                    discovered_nodes.put(node.right_child)
                if str(level) in level_nodes_map:
                    level_nodes_map[str(level)].append(node)
                else:
                    level_nodes_map[str(level)] = [node]

        self._depth = level
        self._levels_nodes_map = level_nodes_map

def swapNodes(indexes, queries):
    tree = build_tree(indexes)
    return execute_swap_queries(tree, queries)

def build_tree(indexes):
    root = Node(value = 1)
    created_nodes = [root]
    for index, pair in enumerate(indexes):
        left = Node(pair[0]) if pair[0] >= 0 else None
        if left is not None:
            created_nodes.append(left)
        right = Node(pair[1]) if pair[1] >= 0 else None
        if right is not None:
            created_nodes.append(right)

        # the input format makes it so the i-th row contains values for i-th tree node
        created_nodes[index].left_child = left
        created_nodes[index].right_child = right
    return Tree(root)

def execute_swap_queries(tree: Tree, queries):
    results = []
    for query in queries:
        query_multiples = get_query_multiplies(query, tree.get_depth())
        for query_multiply in query_multiples:
            tree.swap_child_on_level(query_multiply)
        results.append(tree.in_order())
    return results

def get_query_multiplies(query, limit):
    k = 1
    query_multiples = []
    while k*query <= limit:
         query_multiples.append(k*query)
         k += 1
    return query_multiples


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
