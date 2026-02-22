# Dicionário de dados

## `data/raw/linhas.xlsx`

- Aba: `bairros`
- Coluna principal: `Bairros`
- Formato esperado: sequência de bairros separados por `-`

## `data/processed/gephi_lista*.csv`

- `Source`: bairro de origem
- `Target`: bairro de destino
- `Weight`: frequência da conexão observada

## `data/processed/gephi_matriz*.csv`

- Matriz quadrada de adjacência
- Linhas e colunas representam bairros
- Valores representam peso da conexão
