import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "src"))

from sbc_bus_network.analysis.weighted_metrics import compute_weighted_metrics
from sbc_bus_network.io.csv_graph import adjacency_csv_to_graph
from sbc_bus_network.utils.graph_utils import save_results


def main() -> None:
    graph = adjacency_csv_to_graph("data/processed/gephi_matriz2.csv")
    metrics = compute_weighted_metrics(graph)
    output_file = Path("outputs/metrics/Resultados2 - Com Peso.txt")
    save_results(metrics, output_file)
    print(f"Resultados com peso salvos em: {output_file}")


if __name__ == "__main__":
    main()
