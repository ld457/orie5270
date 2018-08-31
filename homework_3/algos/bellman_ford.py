import copy

import numpy as np

from txt_to_graph import txt_to_graph


def find_negative_circles(name_txt_file):
    """
    Find the negative circles in a graph.

    :param name_txt_file: (str) the name of the graph file
    :return: neg_path: (boolean or list)
    """
    graph_dict = txt_to_graph(name_txt_file)
    num_node = len(graph_dict)

    for node, edges in graph_dict.items():
        edges.append(('sink', 0.))

    graph_dict['sink'] = []

    node_list = graph_dict.keys()

    dist = dict(zip(node_list, [np.inf] * num_node))
    dist['sink'] = 0.

    path_dict = {}
    for node in node_list:
        path_dict[node] = [node]

    for i in range(num_node):
        pre_path_dict = copy.deepcopy(path_dict)
        pre_dist = copy.deepcopy(dist)
        for source in node_list:
            for edge in graph_dict[source]:
                if dist[source] > dist[edge[0]] + edge[1]:
                    dist[source] = pre_dist[edge[0]] + edge[1]
                    path_dict[source] = [source]
                    path_dict[source].extend(pre_path_dict[edge[0]])

    neg_path = None
    pre_path_dict = copy.deepcopy(path_dict)
    pre_dist = copy.deepcopy(dist)
    for source in node_list:
        if neg_path:
            break
        for edge in graph_dict[source]:
            if dist[source] > dist[edge[0]] + edge[1]:
                dist[source] = pre_dist[edge[0]] + edge[1]
                path_dict[source] = [source]
                path_dict[source].extend(pre_path_dict[edge[0]])
                neg_path = path_dict[source]
                break

    neg_circle = []
    idx = 0
    if neg_path:
        for node in neg_path:
            neg_circle.append(node)
            if node in neg_circle[:-1]:
                break
        neg_circle = neg_circle[idx:]
        return neg_circle
    else:
        return None

if __name__ == '__main__':
    negative_circle = find_negative_circles(name_txt_file='../bellman_ford_1.txt')
    print(negative_circle)
