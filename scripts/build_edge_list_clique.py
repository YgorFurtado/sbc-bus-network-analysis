import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from sbc_bus_network.graph_builders.route_clique_edges import build_route_clique_edges
from sbc_bus_network.io.csv_graph import save_edge_list
from sbc_bus_network.io.excel_loader import load_routes


def main() -> None:
    routes = load_routes("data/raw/linhas.xlsx", sheet="bairros", column="Bairros")
    edge_list = build_route_clique_edges(routes)
    output_path = Path("data/processed/gephi_lista2.csv")
    save_edge_list(edge_list, output_path)
    print(f"Lista clique salva em: {output_path}")


if __name__ == "__main__":
    main()
