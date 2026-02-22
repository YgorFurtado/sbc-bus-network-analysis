from itertools import combinations

import pandas as pd


def build_route_clique_edges(routes: list[str]) -> pd.DataFrame:
    edges: dict[tuple[str, str], int] = {}

    for route in routes:
        route_neighborhoods = [item.strip() for item in route.split("-") if item.strip()]
        for source, target in combinations(route_neighborhoods, 2):
            if (source, target) in edges:
                edges[(source, target)] += 1
            elif (target, source) in edges:
                edges[(target, source)] += 1
            else:
                edges[(source, target)] = 1

    data = [(source, target, weight) for (source, target), weight in edges.items()]
    return pd.DataFrame(data, columns=["Source", "Target", "Weight"])
