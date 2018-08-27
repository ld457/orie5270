import unittest

import numpy as np

from algos.dijkstra import find_shortest_path


class TestDijkstra(unittest.TestCase):

    def test_dijkstra(self):
        dist, path = find_shortest_path('dijkstra.txt', source=1., destination=6.)
        assert dist == 11. and np.all(np.array(path) == np.array([1., 2., 4., 6.]))
