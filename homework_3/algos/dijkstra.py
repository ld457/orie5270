from heapq import heappush, heappop

import numpy as np

from txt_to_graph import txt_to_graph


def find_shortest_path(name_txt_file, source, destination):
    """
    Find the shortest path from source to destination using Dijkstra's algorithm.

    :param name_txt_file: (str) the name of the text file for the graph
    :param source: (float) the starting node of a path
    :param destination: (float) the end node of a path
    :return: dist, path: (tuple) dist: (float) the distance of the shortest path;
                                 path: the shortest path
    """

    graph_dict = txt_to_graph(name_txt_file)

    settled = []
    frontier = [source]

    dist = dict(zip(graph_dict.keys(), [np.inf]*len(graph_dict.values())))
    dist[source] = 0.

    pre_point = dict(zip(graph_dict.keys(), [None]*len(graph_dict)))

    while frontier:
        f = heappop(frontier)
        settled.append(f)

        for node, weight in graph_dict[f]:
            if node not in frontier and node not in settled:
                dist[node] = dist[f] + weight
                heappush(frontier, node)
                pre_point[node] = f
            elif dist[f] + weight < dist[node]:
                dist[node] = dist[f] + weight
                pre_point[node] = f

    path = [destination]
    pre = pre_point[destination]
    while pre != source:
        path.insert(0, pre)
        pre = pre_point[pre]
    path.insert(0, pre)

    return dist[destination], path

if __name__ == '__main__':
    dist, path = find_shortest_path(name_txt_file='../dijkstra_1.txt', source=1., destination=4.)
    print(dist, path)
