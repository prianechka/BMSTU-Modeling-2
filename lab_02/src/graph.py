import networkx as nx
import matplotlib.pyplot as plt

EPS = 0.001


def convert_matrix_to_nx_form(matr):
    res = []
    for i_row in range(len(matr)):
        for i_col in range(len(matr[i_row])):
            cur = matr[i_row][i_col]
            if cur > EPS:
                res.append((i_row, i_col, cur))
    return res


def graph(matr):
    DG = nx.DiGraph()
    print(convert_matrix_to_nx_form(matr))
    DG.add_weighted_edges_from(convert_matrix_to_nx_form(matr))
    pos = nx.circular_layout(DG)
    nx.draw(DG, pos, with_labels=True)
    labels = nx.get_edge_attributes(DG, 'weight')
    nx.draw_networkx_edge_labels(DG, pos, edge_labels=labels, label_pos=0.5)
    plt.show()


def graph_probability_over_time(probabilities, stabilization_time, times, probabilities_over_time):
    for i_node in range(len(probabilities_over_time)):
        plt.plot(times, probabilities_over_time[i_node], label = "state " + str(i_node))

    plt.legend()
    plt.xlabel('time')
    plt.ylabel('probability')
    plt.show()