import networkx as nx

from sbc_bus_network.utils.graph_utils import component_diameters, degree_mean


def compute_unweighted_metrics(graph: nx.Graph) -> dict:
    metrics = {}
    metrics["nós"] = graph.number_of_nodes()
    metrics["arestas"] = graph.number_of_edges()
    metrics["conectividade_de_nós"] = nx.node_connectivity(graph)
    metrics["conectividade_de_arestas"] = nx.edge_connectivity(graph)

    metrics["densidade"] = nx.density(graph)
    metrics["grau_medio"] = degree_mean(graph, weighted=False)
    metrics["clustering_medio"] = nx.average_clustering(graph)

    metrics["maior_componente"] = len(max(nx.connected_components(graph), key=len))
    metrics["diametros"] = component_diameters(graph, weighted=False)

    metrics["centralidade_de_proximidade"] = nx.closeness_centrality(graph)
    metrics["centralidade_de_intermedialidade"] = nx.betweenness_centrality(graph)
    metrics["clustering"] = nx.clustering(graph)
    return metrics
