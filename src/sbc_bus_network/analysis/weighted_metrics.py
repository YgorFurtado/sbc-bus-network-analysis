import networkx as nx

from sbc_bus_network.utils.graph_utils import component_diameters, degree_mean


def compute_weighted_metrics(graph: nx.Graph) -> dict:
    metrics = {}
    metrics["nós"] = graph.number_of_nodes()
    metrics["arestas"] = graph.number_of_edges()
    metrics["conectividade_de_nós"] = nx.node_connectivity(graph)
    metrics["conectividade_de_arestas"] = nx.edge_connectivity(graph)

    metrics["densidade"] = nx.density(graph)
    metrics["grau_medio"] = degree_mean(graph, weighted=True)
    metrics["clustering_medio"] = nx.average_clustering(graph, weight="weight")

    metrics["maior_componente"] = len(max(nx.connected_components(graph), key=len))
    metrics["diametros"] = component_diameters(graph, weighted=True)

    metrics["centralidade_de_proximidade"] = nx.closeness_centrality(graph, distance="weight")
    metrics["centralidade_de_intermedialidade"] = nx.betweenness_centrality(graph, weight="weight")
    metrics["clustering"] = nx.clustering(graph, weight="weight")
    return metrics
