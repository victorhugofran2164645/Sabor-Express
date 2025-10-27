# 🚚 Projeto Sabor Express — Rotas Otimizadas

## Descrição do Problema
No contexto de entregas urbanas, empresas enfrentam desafios para organizar rotas eficientes, reduzir custos com combustível e tempo, e garantir entregas rápidas para múltiplos clientes. A complexidade aumenta quando há vários veículos e centenas de pedidos espalhados pela cidade.

O problema central é otimizar a distribuição de pedidos entre entregadores e determinar a melhor sequência de entregas, considerando as distâncias reais entre endereços.

---

## Desafio Proposto
O desafio do projeto é criar um sistema que, dado um conjunto de pedidos em uma cidade:

- Agrupe os pedidos de forma eficiente entre múltiplos veículos/entregadores.
- Defina a ordem ideal de entrega de cada veículo, minimizando a distância total percorrida.
- Gere uma visualização interativa das rotas, permitindo acompanhar a sequência de entregas em um mapa.

---

## Objetivos
O projeto visa:

- Simular pedidos aleatórios em uma cidade para testes de roteirização.
- Agrupar pedidos por entregador utilizando o algoritmo **K-Means**.
- Calcular rotas otimizadas para cada cluster de pedidos com o Problema do Caixeiro Viajante (TSP), usando **OR-Tools**.
- Visualizar interativamente as rotas e a ordem de entrega utilizando **Folium**.
- Fornecer uma solução modular e escalável, que possa ser adaptada para cidades, número de pedidos e veículos diferentes.

---

## Funcionalidades
- Geração de pedidos aleatórios em uma cidade (sem necessidade de arquivos externos).
- Agrupamento de pedidos por entregador com **K-Means**.
- Cálculo de rotas mais curtas usando **OR-Tools** e **NetworkX**.
- Visualização interativa das rotas no mapa com ordem numerada de entregas.
- Suporte para múltiplos veículos e clusters.

---

## Dados de Entrada
> **Importante:** Não existem arquivos de dados externos.  
> Todos os pedidos e suas coordenadas são gerados **automaticamente** pelo script `rota_inteligente.py`.

- DataFrame interno `pedidos` com colunas: `id`, `node`, `lat`, `lon`, `cluster`.

---

## Estrutura do Código — Passo a Passo

0️⃣ **Instalar bibliotecas**  
```python
!pip install osmnx networkx pandas numpy scikit-learn ortools folium

1️⃣ Importar bibliotecas

python
Copiar código
import osmnx as ox
import networkx as nx
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import folium
import random


2️⃣ Definir a cidade

python
Copiar código
cidade = "São Paulo, Brasil"


3️⃣ Baixar a rede viária

Construir grafo com nós (interseções/pedidos) e arestas (ruas com distâncias reais).

Gerar um dicionário com coordenadas geográficas de cada nó.

4️⃣ Gerar pedidos aleatórios

Criação de pedidos simulados com ID, nó correspondente e coordenadas geográficas.

5️⃣ Agrupar pedidos por cluster (entregador)

python
Copiar código
num_veiculos = 3
kmeans = KMeans(n_clusters=num_veiculos, random_state=0)
pedidos['cluster'] = kmeans.fit_predict(pedidos[['lat','lon']])


6️⃣ Criar matriz de distâncias eficiente

Calcula a distância entre todos os pares de pedidos usando Dijkstra.

Cria matriz de distâncias por cluster para resolver o TSP.



7️⃣ Resolver TSP com OR-Tools por cluster

Para cada cluster, resolve o TSP para definir a ordem ideal de entrega.

Cria modelo de roteamento (RoutingModel) e aplica estratégia PATH_CHEAPEST_ARC.

Constrói rota completa na rede viária usando A*.



8️⃣ Visualizar mapa interativo com ordem numerada

Centraliza o mapa na média das coordenadas dos pedidos.

Desenha rotas coloridas por veículo.

Adiciona marcadores numerados indicando a sequência de entrega.

Salva o mapa como HTML:

python
Copiar código
mapa.save("rotas_entrega_optimizada_numerada.html")
Abordagem Adotada
A solução combina clustering de pedidos, otimização de rotas e visualização interativa:

Modelagem da cidade e rede viária com grafo dirigido.

Geração de pedidos aleatórios na cidade.

Agrupamento de pedidos em clusters usando K-Means.

Cálculo de matriz de distâncias entre pedidos.

Resolução do TSP com OR-Tools para cada cluster.

Construção de rota completa usando A*.

Visualização de rotas coloridas e marcadores numerados em Folium.

Algoritmos Utilizados
K-Means → Agrupamento de pedidos por proximidade geográfica.

Dijkstra → Cálculo de menor caminho entre nós da rede viária.

A* → Geração da rota real entre pedidos no grafo.

OR-Tools TSP Solver → Otimização da sequência de entregas dentro de cada cluster.

Outputs Relevantes
Mapa interativo das rotas:

rotas_entrega_optimizada_numerada.html

Mostra rotas coloridas, ordem numerada e popups com informações dos pedidos.

Rotas calculadas no código:

Dicionário rotas_clusters → Sequência de nós do grafo por cluster/veículo.

Dados de pedidos (internos):

DataFrame pedidos com IDs, coordenadas e clusters.

Instruções de Execução do Projeto


1️⃣ Instalar dependências
python
Copiar código
!pip install osmnx networkx pandas numpy scikit-learn ortools folium


2️⃣ Obter o código
bash
Copiar código
git clone https://github.com/victorhugofran2164645/Sabor-Express1.git
ou faça upload do arquivo rota_inteligente.py no Colab.



3️⃣ Executar o script
python
Copiar código
!python rota_inteligente.py
Isso executará todas as etapas automaticamente.


4️⃣ Visualizar o mapa
Abra o arquivo gerado: rotas_entrega_optimizada_numerada.html

Confira rotas coloridas, marcadores numerados e popups com informações dos pedidos.

Possíveis Extensões
Vários pontos de partida para veículos.

Rotas dinâmicas considerando trânsito em tempo real.

Visualização com dashboards interativos.

Exportação de rotas para dispositivos GPS ou aplicativos de entrega



🔍 Análise dos Resultados, Eficiência, Limitações e Sugestões de Melhoria
📈 Interpretação dos Resultados

pedidos: mostra IDs, coordenadas e clusters atribuídos por K-Means.

rotas_clusters: define a ordem otimizada de entrega por veículo.

Mapa HTML: permite inspecionar visualmente rotas e validar se há sobreposição ou desvios.

⚙️ Métricas de Eficiência

Distância total percorrida (km)

Tempo total de execução (s)

Balanceamento de entregas (número de pedidos por veículo)

Melhoria percentual em relação a um baseline aleatório

Custo médio por entrega = distância total / número de pedidos

💪 Pontos Fortes

Combina algoritmos clássicos de IA (K-Means, A*, TSP).

Visualização intuitiva e fácil de interpretar.

Código modular e de fácil expansão.

Geração de dados automatizada (sem dependências externas).

⚠️ Limitações

K-Means ignora capacidade ou janelas de tempo.

Agrupamento e roteamento separados → pode não ser ótimo globalmente.

Ignora condições de tráfego ou vias restritas.

Não re-otimiza rotas dinamicamente.

Escalabilidade limitada com muitos pedidos (> 500).

Assume um único depósito para todos os veículos.

💡 Sugestões de Melhoria
🔹 Curto Prazo

Adicionar métricas de desempenho no código (distância total, tempo de execução, balanceamento).

Usar clustering com restrição de capacidade (K-Means balanceado).

Comparar desempenho com heurísticas simples (baseline aleatório).

🔹 Médio Prazo

Migrar de TSP para VRP (Vehicle Routing Problem) com OR-Tools RoutingModel, incluindo:

capacidade dos veículos,

janelas de entrega (time windows),

múltiplos depósitos.

Adicionar tempos de viagem estimados (velocidade média ou APIs de trânsito).

🔹 Longo Prazo

Implementar roteamento dinâmico em tempo real.

Integrar com dashboards interativos (Plotly/Dash).

Criar cache de distâncias e paralelismo para acelerar execuções.

Simular cenários de pico com variação de demanda.


