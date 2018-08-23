class Tree(object):

    def __init__(self, root):
        self.root = root
        self.tree_list = []

    def get_value_root(self):
        if self.root is not None:
            return self.root.value
        else:
            return None

    @classmethod
    def get_height(cls, node):
        """
        Compute the height of a tree

        :param node:
        :return: height
        """
        if node is not None:

            left_height = cls.get_height(node.left)
            right_height = cls.get_height(node.right)

            height = 1 + max(left_height, right_height)
        else:
            height = 0

        return height

    def print_tree(self, is_print=True):
        """
        Print the tree

        :return: tree_list:
        """
        height = Tree.get_height(self.root)
        width = 2 ** height - 1

        tree_list = []
        for h in range(height):
            tree_list.append(["|"] * width)

        def fill_node(root, row, left_end, right_end):
            """

            :param root:
            :param row:
            :param left_end:
            :param right_end:
            :return: tree_list:
            """

            if root is None:
                return None

            middle = (left_end + right_end) / 2
            tree_list[row][middle] = str(root.value)
            fill_node(root.left, row + 1, left_end, middle - 1)
            fill_node(root.right, row + 1, middle + 1, right_end)

        fill_node(self.root, row=0, left_end=0, right_end=width-1)

        if is_print:
            # Print the tree
            for i in tree_list:
                print "".join(i)

        return tree_list


class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


if __name__ == '__main__':
    t21 = Node(4, None, None)
    t22 = Node(5, None, None)
    t23 = Node(6, None, None)
    t24 = Node(7, None, None)
    t11 = Node(2, t21, t22)
    t12 = Node(3, t23, t24)

    root_1 = Node(1, t11, t12)
    test_1 = Tree(root_1)
    test_1.print_tree()
    print ""

    n3 = Node(4, None, None)
    n2 = Node(3, n3, None)
    n1 = Node(2, n2, None)
    root_2 = Node(1, n1, None)
    test_2 = Tree(root_2)
    test_2.print_tree()
    print ""

    root_3 = Node(1, None, None)
    test_3 = Tree(root_3)
    test_3.print_tree()
    print ""

    n5 = Node(9, None, None)
    n4 = Node(8, None, n5)
    n3 = Node(7, n4, None)
    n2 = Node(6, None, None)
    n1 = Node(5, None, n2)
    root_4 = Node(4, n1, n3)
    test_4 = Tree(root_4)
    test_4.print_tree()
    print ""



