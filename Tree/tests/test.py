import unittest

import numpy as np

from tree.tree import Tree, Node


class TestTree(unittest.TestCase):

    def setUp(self):
        # Four test cases
        t21 = Node(4, None, None)
        t22 = Node(5, None, None)
        t23 = Node(6, None, None)
        t24 = Node(7, None, None)
        t11 = Node(2, t21, t22)
        t12 = Node(3, t23, t24)
        root_1 = Node(1, t11, t12)
        self.test_1 = Tree(root_1)

        n3 = Node(4, None, None)
        n2 = Node(3, n3, None)
        n1 = Node(2, n2, None)
        root_2 = Node(1, n1, None)
        self.test_2 = Tree(root_2)

        root_3 = Node(1, None, None)
        self.test_3 = Tree(root_3)

        n5 = Node(9, None, None)
        n4 = Node(8, None, n5)
        n3 = Node(7, n4, None)
        n2 = Node(6, None, None)
        n1 = Node(5, None, n2)
        root_4 = Node(4, n1, n3)
        self.test_4 = Tree(root_4)

    def test_case_1(self):

        tree_list = self.test_1.print_tree()
        assert np.all(np.array(tree_list) ==
                      np.array([['|', '|', '|', '1', '|', '|', '|'],
                                ['|', '2', '|', '|', '|', '3', '|'],
                                ['4', '|', '5', '|', '6', '|', '7']]))

    def test_case_2(self):

        tree_list = self.test_2.print_tree()
        assert np.all(np.array(tree_list) ==
                      np.array([['|'] * 7 + ['1'] + ['|'] * 7,
                                ['|'] * 3 + ['2'] + ['|'] * 11,
                                ['|'] + ['3'] + ['|'] * 13,
                                ['4'] + ['|'] * 14]))

    def test_case_3(self):

        tree_list = self.test_3.print_tree()
        assert np.all(np.array(tree_list) == np.array(['1']))

    def test_case_4(self):

        tree_list = self.test_4.print_tree()
        assert np.all(np.array(tree_list) ==
                      np.array([['|'] * 7 + ['4'] + ['|'] * 7,
                                ['|'] * 3 + ['5'] + ['|'] * 7 + ['7'] + ['|'] * 3,
                                ['|'] * 5 + ['6'] + ['|'] * 3 + ['8'] + ['|'] * 5,
                                ['|'] * 10 + ['9'] + ['|'] * 4]))
