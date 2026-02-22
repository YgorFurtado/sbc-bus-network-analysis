import networkx as nx

from sbc_bus_network.analysis.unweighted_metrics import compute_unweighted_metrics
from sbc_bus_network.analysis.weighted_metrics import compute_weighted_metrics


def test_compute_unweighted_metrics_basic_graph():
    graph = nx.path_graph(["A", "B", "C"])
    metrics = compute_unweighted_metrics(graph)
    assert metrics["nós"] == 3
    assert metrics["arestas"] == 2


def test_compute_weighted_metrics_basic_graph():
    graph = nx.Graph()
    graph.add_edge("A", "B", weight=2)
    graph.add_edge("B", "C", weight=1)
    metrics = compute_weighted_metrics(graph)
    assert metrics["nós"] == 3
    assert metrics["arestas"] == 2
