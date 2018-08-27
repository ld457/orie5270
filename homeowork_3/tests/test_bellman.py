import unittest

import numpy as np

from algos.bellman_ford import find_negative_circles


class TestBellman(unittest.TestCase):

    def test_bellman(self):
        negative_circle = find_negative_circles('bellman_ford.txt')
        assert np.all(np.array(negative_circle) == np.array([2., 3., 4., 2.]))
