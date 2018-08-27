import pandas as pd


def txt_to_graph(name_txt_file):
    """
    Parse the text for a graph and return a dictionary for a graph.

    :param name_txt_file: (str) the name of the text file for a graph
    :return: graph_dict: (dict) the dictionary of the graph
    """
    graph = pd.read_table(name_txt_file, header=None, skip_blank_lines=False)
    node_list = graph.iloc[range(0, len(graph), 2), 0].apply(lambda x: float(x)).tolist()
    edge = graph.iloc[range(1, len(graph), 2), 0].fillna('')
    edge = edge.apply(lambda x: x.replace('(', '').replace(')', '').split(','))
    edge_list = []
    for e in edge:
        sub_edge = []
        for i in range(0, len(e), 2):
            if e[i] != '':
                sub_edge.append((float(e[i]), float(e[i + 1])))
        edge_list.append(sub_edge)

    graph_dict = dict(zip(node_list, edge_list))
    return graph_dict


if __name__ == '__main__':
    import os

    cwd = os.getcwd()
    print cwd
    graph_dict = txt_to_graph('dijkstra.txt')
    print graph_dict
