# Sabor-Express — Roteamento Inteligente (pacote entregue)

**Este pacote contém uma implementação completa e reproduzível do projeto Sabor-Express**, feito para avaliação. O objetivo é sugerir rotas de entrega eficientes para uma frota baseada em clusterização + roteamento em um grafo grid.

## Estrutura do repositório
```
/ (root)
├─ src/rota_inteligente.py        # script principal (pode ser executado)
├─ data/pedidos_exemplo.csv      # dados de pedidos de exemplo
├─ docs/                         # outputs gerados (imagens, html, json)
├─ requirements.txt
├─ README.md
```

## O que está incluído (checagem contra o edital)
- ✅ **Descrição do problema e objetivos**: presente neste README e no header do script.
- ✅ **Abordagem adotada**: KMeans (clusterização) + roteamento em um grafo grid com A* entre pontos (detalhado no README e código).
- ✅ **Algoritmos utilizados**: KMeans (implementação própria, explicada), A* (implementação própria), heurística greedy para construção de rotas (NN - nearest neighbor).
- ✅ **Diagrama do grafo/modelo**: `docs/diagrama_grafo_rotas.png` (gerado automaticamente pelo script).
- ✅ **Código-fonte completo e organizado**: todo código em `src/`.
- ✅ **Arquivos de dados**: `data/pedidos_exemplo.csv` incluído.
- ✅ **Outputs relevantes**: `docs/diagrama_grafo_rotas.png`, `docs/rotas_entrega_real.html`, `docs/rotas_detalhes.json`.
- ✅ **Instruções claras de execução** (abaixo).

## Como executar (passo a passo)
Recomendado: criar virtualenv, instalar dependências e rodar o script.

```bash
python -m venv .venv
# Linux / Mac
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
python src/rota_inteligente.py --data data --docs docs --k 3
```

Saídas geradas em `docs/`:
- `diagrama_grafo_rotas.png` — diagrama com pedidos, centroides, depósito e rotas;
- `rotas_entrega_real.html` — arquivo HTML simples com a imagem e resumo;
- `rotas_detalhes.json` — detalhes dos clusters e rotas (para validação).

## Análise de resultados e limitações
- A clusterização reduz o espaço de busca e atribui grupos de entregas a cada veículo.
- O A* foi usado entre pontos (nós de grid). A solução de roteamento dentro de cada cluster é uma aproximação greedy (nearest neighbor) — **não é** solução ótima TSP.
- Limitações: implementação de demonstração (mapa grid fictício), não usa dados reais de ruas (OSM) e não considera capacidades reais dos veículos, janelas de tempo ou restrições de trânsito.
- Sugestões de melhoria: integrar OSMnx para gerar um grafo real de ruas, usar solver de VRP (ex: OR-Tools) para otimização com capacidades, adicionar simulações de tempo de serviço, e testes de desempenho para escalabilidade.

## Arquivos de dados
- `data/pedidos_exemplo.csv` — 30 pedidos de exemplo (colunas: id, x, y, demand).

## Observações finais
Se quiser, eu posso:
- abrir um Pull Request no seu repositório com esses arquivos; ou
- gerar um patch/zip para upload manual (eu já gerei um arquivo zip disponível para download).

---
*Gerado automaticamente por assistência - Sabor-Express pack.*
