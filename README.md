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
- Geração de pedidos aleatórios em uma cidade.
- Agrupamento de pedidos por entregador com **K-Means**.
- Cálculo de rotas mais curtas usando **OR-Tools** e **NetworkX**.
- Visualização interativa das rotas no mapa com ordem numerada de entregas.
- Suporte para múltiplos veículos e clusters.

---

## Pré-requisitos
Para executar o código, você precisa apenas do **Google Colab** e das bibliotecas Python:

```python
!pip install osmnx folium networkx scikit-learn ortools
Estrutura do Código — Passo a Passo
O código está organizado em 8 etapas principais, cada uma responsável por uma parte do fluxo de roteirização e visualização.

0️⃣ Instalar bibliotecas
Instala bibliotecas para manipulação de grafos, clustering, otimização e visualização interativa.

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
Baixa a rede de ruas da cidade usando OSMnx.

Constrói um grafo com nós (interseções/pedidos) e arestas (ruas com distância real).

Gera um dicionário com as coordenadas geográficas de cada nó.

4️⃣ Gerar pedidos aleatórios
Cria pedidos simulados, com ID, nó correspondente e coordenadas geográficas.

5️⃣ Agrupar pedidos por cluster (entregador)
python
Copiar código
num_veiculos = 3
kmeans = KMeans(n_clusters=num_veiculos, random_state=0)
pedidos['cluster'] = kmeans.fit_predict(pedidos[['lat','lon']])
6️⃣ Criar matriz de distâncias eficiente
Calcula a distância entre todos os pares de pedidos usando Dijkstra.

Cria uma matriz de distâncias por cluster para resolver o TSP.

7️⃣ Resolver TSP com OR-Tools por cluster
Para cada cluster, resolve o TSP para definir a ordem ideal de entrega.

Cria modelo de roteamento (RoutingModel), define função de custo baseada em distâncias e aplica a estratégia PATH_CHEAPEST_ARC.

Constrói rota completa na rede viária usando A*.

python
Copiar código
tsp_order = solve_tsp(matrix)
rota_final = nx.astar_path(G, source=rota_nodes[i], target=rota_nodes[i+1], weight='length')
8️⃣ Visualizar mapa interativo com ordem numerada
Centraliza o mapa na média das coordenadas dos pedidos.

Desenha rotas coloridas por veículo.

Adiciona marcadores numerados indicando a sequência de entregas.

Salva o mapa como HTML interativo:

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

Diagrama do Grafo/Modelo Usado
text
Copiar código
[Pedidos] --> [K-Means] --> [Clusters de Pedidos] --> [TSP OR-Tools]
                 |                                      |
                 v                                      v
           [Matriz de Distâncias]                 [Rota Sequencial]
                 |                                      |
                 ---------------------------------------->
                              [Mapa Interativo Folium]
Cada cluster recebe uma rota otimizada que percorre os pedidos em sequência mínima, respeitando a rede viária real da cidade.

Análise dos Resultados
Eficiência da solução:

Redução de distância total percorrida por veículo.

Distribuição equilibrada de pedidos entre veículos.

Sequência de entregas otimizada com base em distâncias reais.

Limitações encontradas:

Pedidos aleatórios podem criar clusters desequilibrados.

Não considera restrições de tempo ou capacidade de veículos.

Cálculo em grafos grandes pode ser computacionalmente pesado.

Sugestões de melhoria:

Inserir endereços reais ou pontos de interesse.

Adicionar restrições de capacidade e janelas de tempo.

Pré-processamento da matriz de distâncias para otimização.

Integração com APIs externas (Google Maps, OpenRouteService) para distâncias reais.

Possíveis Extensões
Vários pontos de partida para veículos.

Rotas dinâmicas considerando trânsito em tempo real.

Visualização com dashboards interativos.

Exportação de rotas para dispositivos GPS ou aplicativos de entrega.

Como Executar
Abra o Google Colab.

Copie e cole o código do projeto no notebook.

Execute célula por célula seguindo a ordem numérica.

Abra o arquivo rotas_entrega_optimizada_numerada.html para visualizar as rotas.
