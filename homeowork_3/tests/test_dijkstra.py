import unittest

import numpy as np

from algos.dijkstra import find_shortest_path
from algos.bellman_ford import find_negative_circles


class TestAlgos(unittest.TestCase):

    def test_dijkstra(self):
        dist, path = find_shortest_path('dijkstra.txt', source=1., destination=6.)
        assert dist == 11. and np.all(np.array(path) == np.array([1., 2., ]))