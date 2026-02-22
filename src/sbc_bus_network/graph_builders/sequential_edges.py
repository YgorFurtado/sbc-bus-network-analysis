import pandas as pd


def build_sequential_edges(routes: list[str]) -> pd.DataFrame:
    edges: dict[tuple[str, str], int] = {}

    for route in routes:
        route_neighborhoods = [item.strip() for item in route.split("-") if item.strip()]
        for index in range(len(route_neighborhoods) - 1):
            source = route_neighborhoods[index]
            target = route_neighborhoods[index + 1]
            if (source, target) in edges:
                edges[(source, target)] += 1
            elif (target, source) in edges:
                edges[(target, source)] += 1
            else:
                edges[(source, target)] = 1

    data = [(source, target, weight) for (source, target), weight in edges.items()]
    return pd.DataFrame(data, columns=["Source", "Target", "Weight"])
