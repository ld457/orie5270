import unittest

import numpy as np

from algos.bellman_ford import find_negative_circles


class TestBellman(unittest.TestCase):

    def test_bellman_1(self):
        negative_circle = find_negative_circles('bellman_1.txt')
        assert np.all(np.array(negative_circle) == np.array([2., 3., 4., 2.]))

    def test_bellman_2(self):
        negative_circle = find_negative_circles('bellman_2.txt')
        assert negative_circle is None
