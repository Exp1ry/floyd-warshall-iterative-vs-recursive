import unittest
from sys import maxsize, path
import os

path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import recursion.recursive_floyd as rec
import iterative.iterative_floyd as it

NO_PATH = maxsize

class TestFloydAlgorithm(unittest.TestCase):
    def setUp(self):
        """ Setup that resets the graph to conduct both tests. """
        new_graph = [[0, 7, NO_PATH, 8],
                     [NO_PATH, 0, 5, NO_PATH],
                     [NO_PATH, NO_PATH, 0, 2],
                     [NO_PATH, NO_PATH, NO_PATH, 0]]

        
        rec.GRAPH = [row[:] for row in new_graph]
        it.GRAPH = [row[:] for row in new_graph]

    def test_recursive(self):
        """ Checks if Floyd-Warshall recursive version computes correct shortest paths """
        rec.recursive_floyd_warshall(0, 0, 0)
        expected = [[0, 7, 12, 8],
                    [NO_PATH, 0, 5, 7],
                    [NO_PATH, NO_PATH, 0, 2],
                    [NO_PATH, NO_PATH, NO_PATH, 0]]
        self.assertEqual(rec.GRAPH, expected)

    def test_iterative(self):
        """ Checks if Floyd-Warshall iterative version computes correct shortest paths """
        it.iterative_floyd()
        expected = [[0, 7, 12, 8],
                    [NO_PATH, 0, 5, 7],
                    [NO_PATH, NO_PATH, 0, 2],
                    [NO_PATH, NO_PATH, NO_PATH, 0]]
        self.assertEqual(it.GRAPH, expected)

# Test Suite & Runner
if __name__ == '__main__':
    unittest.main()