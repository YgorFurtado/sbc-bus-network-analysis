from pathlib import Path

import networkx as nx
import pandas as pd


def edge_list_to_adjacency_matrix(csv_file: str | Path, output_file: str | Path) -> None:
    dataframe = pd.read_csv(csv_file)
    nodes = sorted(set(dataframe["Source"]).union(set(dataframe["Target"])))
    adjacency_matrix = pd.DataFrame(0, index=nodes, columns=nodes)

    for _, row in dataframe.iterrows():
        source = row["Source"]
        target = row["Target"]
        weight = row["Weight"]
        adjacency_matrix.at[source, target] = weight
        adjacency_matrix.at[target, source] = weight

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    adjacency_matrix.to_csv(output_file, index=True)


def adjacency_csv_to_graph(csv_path: str | Path) -> nx.Graph:
    dataframe = pd.read_csv(csv_path, sep=",", index_col=0)
    graph = nx.from_pandas_adjacency(dataframe)
    return graph


def save_edge_list(dataframe: pd.DataFrame, output_path: str | Path) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)
