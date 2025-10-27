# 🚚 Sabor Express — Rotas Otimizadas com Ordem

## 📌 1. Descrição do Problema e Objetivos
No contexto de entregas urbanas de comida, otimizar as rotas dos entregadores é essencial para reduzir tempo e custo de deslocamento. Este projeto oferece uma solução de roteamento inteligente que:

- Determina a rota mais curta entre os pedidos de cada cluster.
- Agrupa pedidos de forma eficiente entre múltiplos entregadores.
- Visualiza rotas e clusters de pedidos em um mapa interativo.

**Objetivos do projeto:**

1. Criar um grafo urbano real da cidade (São Paulo por padrão).
2. Gerar pedidos aleatórios e agrupar em clusters, simulando entregadores.
3. Calcular rotas usando A* e resolver o TSP por cluster.
4. Exibir resultados em mapas interativos com ordem de entrega numerada.

---

## 🛠️ 2. Estrutura do Projeto

Sabor-Express/
├── src/
│ └── rota_inteligente.py # Código principal do projeto
├── data/
│ └── pedidos.csv (opcional) # Arquivo CSV de pedidos gerados
├── docs/
│ └── rotas_entrega_optimizada_numerada.html # Mapa interativo gerado
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto

markdown
Copiar código

**Explicação rápida das pastas:**

- `src/` → Contém o código-fonte do projeto e scripts principais.  
- `data/` → Armazena dados brutos ou simulados, como pedidos aleatórios.  
- `docs/` → Contém mapas interativos e visualizações do grafo urbano.  
- `requirements.txt` → Lista de pacotes Python necessários.  
- `README.md` → Documentação e instruções do projeto.  

---

## 🧮 3. Algoritmos Utilizados

| Algoritmo | Função no Projeto |
|-----------|-----------------|
| A* | Calcula o caminho mais curto entre os pedidos no grafo urbano. |
| K-Means | Agrupa pedidos em clusters geográficos, representando cada entregador. |
| TSP (OR-Tools) | Define a sequência de entrega dentro de cada cluster para minimizar a distância total. |

---

## 📊 4. Abordagem Detalhada

**Criação do grafo urbano:**

- Utilizamos `OSMnx` para baixar o grafo de ruas da cidade de São Paulo.
- Cada nó representa um cruzamento, e cada aresta uma rua com peso baseado na distância.

**Geração de pedidos aleatórios:**

- Seleção aleatória de nós do grafo para simular pedidos.
- Armazenamento em um DataFrame com `id`, coordenadas e cluster.

**Clusterização de pedidos:**

- Aplicamos `K-Means` para dividir os pedidos em clusters.
- Cada cluster representa a área de atuação de um entregador.

**Cálculo de rotas e TSP:**

- Para cada cluster, criamos uma matriz de distâncias entre pedidos.
- Utilizamos `OR-Tools` para resolver o TSP e definir a sequência de entrega.
- Calculamos rotas completas no grafo usando A* entre os nós ordenados.

**Visualização:**

- Mapa interativo `Folium` com rotas coloridas por cluster.
- Marcadores numerados mostram a ordem de entrega de cada pedido.

---

## 📈 5. Outputs Relevantes

- **Mapa interativo:** `docs/rotas_entrega_optimizada_numerada.html`  
  Exibe rotas de cada entregador com pedidos numerados.

- **Exemplo de CSV de pedidos (opcional):** `data/pedidos.csv`  

---

## ⚙️ 6. Instruções de Execução

### 6.1 Pré-requisitos

- Python 3.8 ou superior
- pip

### 6.2 Instalar dependências

```bash
pip install osmnx folium networkx scikit-learn ortools pandas numpy
6.3 Executar o código principal
bash
Copiar código
python src/rota_inteligente.py
6.4 Resultado esperado
Mapa interativo gerado: docs/rotas_entrega_optimizada_numerada.html

Rotas de cada entregador com sequência de pedidos numerada.

📝 7. Análise dos Resultados
Rotas calculadas com A* garantem o menor percurso entre os pedidos.

Clusterização com K-Means otimiza áreas de entrega para múltiplos entregadores.

TSP resolve a ordem de entrega dentro de cada cluster.

Limitações:

Não considera tráfego em tempo real.

Número de pedidos e veículos fixo na simulação.

Sugestões de melhoria:

Integrar tráfego em tempo real ou restrições de tempo de entrega.

Permitir personalização de clusters por prioridade de pedido ou distância máxima.

Ajustar TSP para múltiplos veículos simultâneos em grandes volumes de pedidos.

yaml
Copiar código

---

Se você quiser, posso criar **uma versão ainda mais visual do README**, incluindo **imagens do mapa, cores dos clusters e trechos do código**, para deixar ele pronto para colocar no GitHub.  

Quer que eu faça essa versão visual também?






Você disse:
todos codigos em Markdown para colocar github



O ChatGPT disse:
Perfeito! Vou montar um README completo para GitHub, com todos os códigos em blocos Markdown, pronto para uso, incluindo instalação, execução e exemplos de visualização.

markdown
Copiar código
# 🚚 Sabor Express — Rotas Otimizadas com Ordem

## 📌 1. Descrição do Problema e Objetivos
No contexto de entregas urbanas de comida, otimizar as rotas dos entregadores é essencial para reduzir tempo e custo de deslocamento. Este projeto oferece uma solução de roteamento inteligente que:

- Determina a rota mais curta entre os pedidos de cada cluster.
- Agrupa pedidos de forma eficiente entre múltiplos entregadores.
- Visualiza rotas e clusters de pedidos em um mapa interativo.

**Objetivos do projeto:**

1. Criar um grafo urbano real da cidade (São Paulo por padrão).
2. Gerar pedidos aleatórios e agrupar em clusters, simulando entregadores.
3. Calcular rotas usando A* e resolver o TSP por cluster.
4. Exibir resultados em mapas interativos com ordem de entrega numerada.

---

## 🛠️ 2. Estrutura do Projeto

Sabor-Express/
├── src/
│ └── rota_inteligente.py # Código principal do projeto
├── data/
│ └── pedidos.csv (opcional) # Arquivo CSV de pedidos gerados
├── docs/
│ └── rotas_entrega_optimizada_numerada.html # Mapa interativo gerado
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto

yaml
Copiar código

**Explicação rápida das pastas:**

- `src/` → Contém o código-fonte do projeto e scripts principais.  
- `data/` → Armazena dados brutos ou simulados, como pedidos aleatórios.  
- `docs/` → Contém mapas interativos e visualizações do grafo urbano.  
- `requirements.txt` → Lista de pacotes Python necessários.  
- `README.md` → Documentação e instruções do projeto.  

---

## 🧮 3. Algoritmos Utilizados

| Algoritmo | Função no Projeto |
|-----------|-----------------|
| A* | Calcula o caminho mais curto entre os pedidos no grafo urbano. |
| K-Means | Agrupa pedidos em clusters geográficos, representando cada entregador. |
| TSP (OR-Tools) | Define a sequência de entrega dentro de cada cluster para minimizar a distância total. |

---

## 📊 4. Código do Projeto

### 4.1 Instalar Bibliotecas

```python
# Instalar bibliotecas necessárias
!pip install osmnx folium networkx scikit-learn ortools pandas numpy
4.2 Importar Bibliotecas
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
4.3 Definir a Cidade
python
Copiar código
cidade = "São Paulo, Brasil"
4.4 Baixar a Rede Viária
python
Copiar código
G = ox.graph_from_place(cidade, network_type='drive', simplify=True)
nodes = list(G.nodes)
coords_nodes = {n: (G.nodes[n]['y'], G.nodes[n]['x']) for n in nodes}
4.5 Gerar Pedidos Aleatórios
python
Copiar código
num_pedidos = 20
pedidos_nodes = random.sample(nodes, num_pedidos)
pedidos_coords = [coords_nodes[n] for n in pedidos_nodes]

pedidos = pd.DataFrame({
    'id': list(range(1, num_pedidos + 1)),
    'node': pedidos_nodes,
    'lat': [c[0] for c in pedidos_coords],
    'lon': [c[1] for c in pedidos_coords]
})
4.6 Agrupar Pedidos por Cluster (Entregador)
python
Copiar código
num_veiculos = 3
kmeans = KMeans(n_clusters=num_veiculos, random_state=0)
pedidos['cluster'] = kmeans.fit_predict(pedidos[['lat','lon']])
4.7 Criar Matriz de Distâncias
python
Copiar código
dist_matrix_total = {}
for n in pedidos['node']:
    lengths = nx.single_source_dijkstra_path_length(G, source=n, weight='length')
    dist_matrix_total[n] = {target: lengths[target] for target in pedidos['node']}

def get_cluster_matrix(cluster_pedidos):
    nodes = cluster_pedidos['node'].tolist()
    matrix = [[dist_matrix_total[i][j] for j in nodes] for i in nodes]
    return matrix
4.8 Resolver TSP com OR-Tools
python
Copiar código
def solve_tsp(dist_matrix):
    size = len(dist_matrix)
    manager = pywrapcp.RoutingIndexManager(size, 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        return int(dist_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_params = pywrapcp.DefaultRoutingSearchParameters()
    search_params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing.SolveWithParameters(search_params)
    if solution:
        index = routing.Start(0)
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        return route
    else:
        return list(range(size))
4.9 Calcular Rotas por Cluster
python
Copiar código
rotas_clusters = {}
for c in pedidos['cluster'].unique():
    cluster_pedidos = pedidos[pedidos['cluster'] == c].reset_index(drop=True)
    matrix = get_cluster_matrix(cluster_pedidos)
    tsp_order = solve_tsp(matrix)
    rota_nodes = [cluster_pedidos.iloc[i]['node'] for i in tsp_order]

    rota_final = []
    for i in range(len(rota_nodes) - 1):
        caminho = nx.astar_path(G, source=rota_nodes[i], target=rota_nodes[i+1], weight='length')
        rota_final.extend(caminho[:-1])
    rota_final.append(rota_nodes[-1])
    rotas_clusters[c] = rota_final
4.10 Visualizar Mapa Interativo
python
Copiar código
centro = [pedidos['lat'].mean(), pedidos['lon'].mean()]
mapa = folium.Map(location=centro, zoom_start=12)
cores = ['red','blue','green','purple','orange','darkred','lightblue']

for cluster_id, rota_nodes in rotas_clusters.items():
    rota_coords = [coords_nodes[n] for n in rota_nodes]
    folium.PolyLine(
        rota_coords,
        color=cores[cluster_id % len(cores)],
        weight=5,
        opacity=0.7,
        tooltip=f'Veículo {cluster_id}'
    ).add_to(mapa)

    cluster_pedidos = pedidos[pedidos['cluster']==cluster_id].reset_index(drop=True)
    node_to_id = {row['node']: row['id'] for _, row in cluster_pedidos.iterrows()}

    pedidos_ordenados = []
    for n in rota_nodes:
        if n in node_to_id and node_to_id[n] not in pedidos_ordenados:
            pedidos_ordenados.append(node_to_id[n])

    for ordem, pedido_id in enumerate(pedidos_ordenados, start=1):
        row = cluster_pedidos[cluster_pedidos['id']==pedido_id].iloc[0]
        folium.CircleMarker(
            location=(row['lat'], row['lon']),
            radius=10,
            color='white',
            fill=True,
            fill_color=cores[cluster_id % len(cores)],
            fill_opacity=0.9,
            popup=f'Pedido {pedido_id} — Ordem {ordem}'
        ).add_to(mapa)
        folium.map.Marker(
            [row['lat'], row['lon']],
            icon=folium.DivIcon(html=f"""<div style="font-size: 12pt; color: white; text-align:center">{ordem}</div>""")
        ).add_to(mapa)

mapa.save("docs/rotas_entrega_optimizada_numerada.html")
mapa
⚙️ 5. Instruções de Execução
Pré-requisitos
Python 3.8 ou superior

pip

Instalar dependências
bash
Copiar código
pip install osmnx folium networkx scikit-learn ortools pandas numpy
Executar o código
bash
Copiar código
python src/rota_inteligente.py
Resultado esperado
Mapa interativo gerado: docs/rotas_entrega_optimizada_numerada.html

Rotas de cada entregador com sequência de pedidos numerada.

📝 6. Análise dos Resultados
Rotas calculadas com A* garantem o menor percurso entre os pedidos.

Clusterização com K-Means otimiza áreas de entrega para múltiplos entregadores.

TSP resolve a ordem de entrega dentro de cada cluster.

Limitações:

Não considera tráfego em tempo real.

Número de pedidos e veículos fixo na simulação.

Sugestões de melhoria:

Integrar tráfego em tempo real ou restrições de tempo de entrega.

Permitir personalização de clusters por prioridade de pedido ou distância máxima.

Ajustar TSP para múltiplos veículos simultâneos em grandes volumes de pedidos.










