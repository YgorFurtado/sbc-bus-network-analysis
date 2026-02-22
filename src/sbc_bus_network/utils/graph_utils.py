from pathlib import Path

import networkx as nx
import pandas as pd


def degree_mean(graph: nx.Graph, weighted: bool) -> float:
    if weighted:
        degree_sum = sum(dict(graph.degree(weight="weight")).values())
    else:
        degree_sum = sum(dict(graph.degree()).values())
    return degree_sum / graph.number_of_nodes()


def component_diameters(graph: nx.Graph, weighted: bool) -> list[float]:
    components = list(nx.connected_components(graph))
    diameters: list[float] = []

    for component in components:
        subgraph = graph.subgraph(component)
        if weighted:
            diameters.append(nx.diameter(subgraph, weight="weight"))
        else:
            diameters.append(nx.diameter(subgraph))

    diameters.sort(reverse=True)
    return diameters


def invert_weights_csv(input_path: str | Path, output_path: str | Path) -> None:
    dataframe = pd.read_csv(input_path, index_col=0)
    inverted = dataframe.replace(0, pd.NA)
    inverted = 1 / inverted
    inverted = inverted.fillna(0)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    inverted.to_csv(output_path)


def save_results(metrics: dict, output_file: str | Path) -> None:
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Número de nós: {metrics['nós']}\n")
        file.write(f"Conectividade de Nós: {metrics['conectividade_de_nós']}\n")
        file.write(f"Número de arestas: {metrics['arestas']}\n")
        file.write(f"Conectividade de Arestas: {metrics['conectividade_de_arestas']}\n\n")

        file.write(f"Densidade do grafo: {metrics['densidade']:.4f}\n")
        file.write(f"Grau médio do grafo: {metrics['grau_medio']:.4f}\n")
        file.write(f"Coeficiente médio de agrupamento: {metrics['clustering_medio']:.4f}\n\n")

        file.write(f"Tamanho do maior componente conexo: {metrics['maior_componente']}\n")
        if len(metrics["diametros"]) == 1:
            file.write(f"Diâmetro do grafo: {metrics['diametros'][0]}\n\n")
        else:
            for index, diameter in enumerate(metrics["diametros"]):
                file.write(f"Diâmetro do componente conexo {index + 1}: {diameter}\n")
            file.write("\n")

        file.write("\nCoeficiente de Agrupamento por Nó:\n")
        for node, clustering in metrics["clustering"].items():
            file.write(f"  Nó {node}: {clustering:.4f}\n")

        file.write("Centralidade de Proximidade:\n")
        for node, centrality in metrics["centralidade_de_proximidade"].items():
            file.write(f"  Nó {node}: {centrality:.4f}\n")

        file.write("\nCentralidade de Intermediabilidade:\n")
        for node, centrality in metrics["centralidade_de_intermedialidade"].items():
            file.write(f"  Nó {node}: {centrality:.4f}\n")
