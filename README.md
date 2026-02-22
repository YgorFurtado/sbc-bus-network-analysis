# sbc-bus-network-analysis

Projeto em Python para construir e analisar grafos de bairros a partir de linhas de ônibus de São Bernardo do Campo.

## Propósito

Converter dados de rotas em representações de rede para estudar:

- conectividade de nós e arestas;
- densidade da rede;
- coeficiente de agrupamento;
- diâmetro por componente;
- centralidades de proximidade e intermediabilidade.

## Funcionalidades

- Geração de lista de arestas para Gephi:
  - conexão sequencial entre bairros da rota;
  - conexão completa (clique) entre bairros da rota.
- Conversão de lista de arestas para matriz de adjacência.
- Cálculo de métricas com e sem peso.
- Exportação de resultados para arquivos `.txt`.

## Instalação

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Opcional (modo pacote):

```bash
pip install -e .
```

## Uso

No diretório raiz do projeto:

```bash
python scripts/build_edge_list_sequential.py
python scripts/build_edge_list_clique.py
python scripts/edge_list_to_matrix.py
python scripts/analyze_weighted.py
python scripts/analyze_unweighted.py
```

## Estrutura do projeto

```text
.
├── src/
│   └── sbc_bus_network/
│       ├── analysis/
│       ├── graph_builders/
│       ├── io/
│       └── utils/
├── scripts/                # pontos de entrada da aplicação
├── data/
│   ├── raw/                # entradas originais
│   ├── processed/          # CSVs gerados (listas/matrizes)
│   └── external/           # dados auxiliares
├── outputs/
│   ├── metrics/            # resultados numéricos .txt
│   └── gephi/              # projetos/exportações Gephi
├── docs/
├── tests/
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Exemplo programático

```python
from sbc_bus_network.analysis.weighted_metrics import compute_weighted_metrics
from sbc_bus_network.graph_builders.sequential_edges import build_sequential_edges
from sbc_bus_network.io.csv_graph import adjacency_csv_to_graph
from sbc_bus_network.io.excel_loader import load_routes

routes = load_routes("data/raw/linhas.xlsx", sheet="bairros", column="Bairros")
edge_df = build_sequential_edges(routes)
graph = adjacency_csv_to_graph("data/processed/gephi_matriz2.csv")
metrics = compute_weighted_metrics(graph)

print(edge_df.head())
print(metrics["densidade"])
```

## Contribuição

1. Faça fork do repositório.
2. Crie branch de trabalho (`feature/nome-curto`).
3. Instale dependências e rode testes.
4. Abra PR com objetivo, impacto e evidências.

Comando de teste:

```bash
pytest
```

## Licença

Distribuído sob licença MIT. Consulte `LICENSE`.
