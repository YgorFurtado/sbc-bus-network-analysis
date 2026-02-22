# Metodologia

1. Ler rotas de ônibus a partir de `data/raw/linhas.xlsx`.
2. Gerar lista de arestas no formato Gephi por duas abordagens:
   - sequencial por rota;
   - clique por rota.
3. Converter lista de arestas em matriz de adjacência.
4. Calcular métricas de teoria dos grafos (com e sem peso).
5. Exportar resultados para `outputs/metrics` e visualizar no Gephi.
