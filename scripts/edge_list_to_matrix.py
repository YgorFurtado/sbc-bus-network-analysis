import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from sbc_bus_network.io.csv_graph import edge_list_to_adjacency_matrix


def main() -> None:
    input_file = Path("data/processed/gephi_lista2.csv")
    output_file = Path("data/processed/gephi_matriz2.csv")
    edge_list_to_adjacency_matrix(input_file, output_file)
    print(f"Matriz salva em: {output_file}")


if __name__ == "__main__":
    main()
