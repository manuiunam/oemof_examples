import networkx as nx
import matplotlib.pyplot as plt

from oemof.network.graph import create_nx_graph


def plot_energy_system(energysystem):

    graph = energysystem.to_networkx()

    pos = nx.spring_layout(graph, seed=42)

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=2500,
        arrows=True,
        font_size=9
    )

    plt.show()