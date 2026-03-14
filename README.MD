# Pipeline ETL com Python

## Descrição
Este projeto foi desenvolvido para demonstrar a implementação de um pipeline ETL (Extract, Transform, Load) em Python.

Devido à possível indisponibilidade da API pública proposta no laboratório, foi utilizada uma abordagem alternativa com arquivo CSV, conforme sugerido no próprio desafio.

## Etapas do ETL

### Extract
Os dados dos usuários são extraídos de um arquivo CSV.

### Transform
Os dados são processados para gerar mensagens personalizadas para cada usuário.

### Load
Os resultados são carregados em um novo arquivo CSV contendo as mensagens geradas.

## Estrutura do projeto

- `data/usuarios.csv` → dados de entrada
- `data/mensagens_geradas.csv` → dados de saída
- `main.py` → execução do pipeline

## Como executar

1. Instale o Python 3
2. Execute o comando:

```bash
python main.py
