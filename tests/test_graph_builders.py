from sbc_bus_network.graph_builders.route_clique_edges import build_route_clique_edges
from sbc_bus_network.graph_builders.sequential_edges import build_sequential_edges


def test_build_sequential_edges_counts_neighbors_only():
    routes = ["A-B-C", "A-B"]
    dataframe = build_sequential_edges(routes)
    rows = {(row.Source, row.Target): row.Weight for row in dataframe.itertuples(index=False)}
    assert rows[("A", "B")] == 2
    assert rows[("B", "C")] == 1


def test_build_route_clique_edges_counts_all_pairs():
    routes = ["A-B-C"]
    dataframe = build_route_clique_edges(routes)
    rows = {(row.Source, row.Target): row.Weight for row in dataframe.itertuples(index=False)}
    assert rows[("A", "B")] == 1
    assert rows[("A", "C")] == 1
    assert rows[("B", "C")] == 1
