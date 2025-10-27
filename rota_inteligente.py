# ============================================================
# 🚚 Projeto Sabor Express — Rotas Otimizadas
# ============================================================

# -----------------------------
# 0️⃣ Instalar bibliotecas
# -----------------------------
!pip install osmnx folium networkx scikit-learn ortools

# -----------------------------
# 1️⃣ Importar bibliotecas
# -----------------------------
import osmnx as ox
import networkx as nx
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import folium
import random

# -----------------------------
# 2️⃣ Definir a cidade
# -----------------------------
cidade = "São Paulo, Brasil"

# -----------------------------
# 3️⃣ Baixar a rede viária
# -----------------------------
G = ox.graph_from_place(cidade, network_type='drive', simplify=True)
nodes = list(G.nodes)
coords_nodes = {n: (G.nodes[n]['y'], G.nodes[n]['x']) for n in nodes}

# -----------------------------
# 4️⃣ Gerar pedidos aleatórios
# -----------------------------
num_pedidos = 20
pedidos_nodes = random.sample(nodes, num_pedidos)
pedidos_coords = [coords_nodes[n] for n in pedidos_nodes]

pedidos = pd.DataFrame({
    'id': list(range(1, num_pedidos + 1)),
    'node': pedidos_nodes,
    'lat': [c[0] for c in pedidos_coords],
    'lon': [c[1] for c in pedidos_coords]
})

# -----------------------------
# 5️⃣ Agrupar pedidos por cluster (entregador)
# -----------------------------
num_veiculos = 3
kmeans = KMeans(n_clusters=num_veiculos, random_state=0)
pedidos['cluster'] = kmeans.fit_predict(pedidos[['lat','lon']])

# -----------------------------
# 6️⃣ Criar matriz de distâncias eficiente
# -----------------------------
dist_matrix_total = {}
for n in pedidos['node']:
    lengths = nx.single_source_dijkstra_path_length(G, source=n, weight='length')
    dist_matrix_total[n] = {target: lengths[target] for target in pedidos['node']}

def get_cluster_matrix(cluster_pedidos):
    nodes = cluster_pedidos['node'].tolist()
    matrix = [[dist_matrix_total[i][j] for j in nodes] for i in nodes]
    return matrix

# -----------------------------
# 7️⃣ Resolver TSP com OR-Tools por cluster
# -----------------------------
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

rotas_clusters = {}
for c in pedidos['cluster'].unique():
    cluster_pedidos = pedidos[pedidos['cluster'] == c].reset_index(drop=True)
    matrix = get_cluster_matrix(cluster_pedidos)
    tsp_order = solve_tsp(matrix)
    rota_nodes = [cluster_pedidos.iloc[i]['node'] for i in tsp_order]

    # Construir rota completa no grafo
    rota_final = []
    for i in range(len(rota_nodes) - 1):
        caminho = nx.astar_path(G, source=rota_nodes[i], target=rota_nodes[i+1], weight='length')
        rota_final.extend(caminho[:-1])
    rota_final.append(rota_nodes[-1])
    rotas_clusters[c] = rota_final

# -----------------------------
# 8️⃣ Visualizar mapa interativo com ordem numerada
# -----------------------------
centro = [pedidos['lat'].mean(), pedidos['lon'].mean()]
mapa = folium.Map(location=centro, zoom_start=12)
cores = ['red','blue','green','purple','orange','darkred','lightblue']

for cluster_id, rota_nodes in rotas_clusters.items():
    # Coordenadas da rota
    rota_coords = [coords_nodes[n] for n in rota_nodes]
    folium.PolyLine(
        rota_coords,
        color=cores[cluster_id % len(cores)],
        weight=5,
        opacity=0.7,
        tooltip=f'Veículo {cluster_id}'
    ).add_to(mapa)

    # Pedidos ordenados
    cluster_pedidos = pedidos[pedidos['cluster']==cluster_id].reset_index(drop=True)
    node_to_id = {row['node']: row['id'] for _, row in cluster_pedidos.iterrows()}

    pedidos_ordenados = []
    for n in rota_nodes:
        if n in node_to_id and node_to_id[n] not in pedidos_ordenados:
            pedidos_ordenados.append(node_to_id[n])

    # Adicionar marcadores numerados diretamente no mapa
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

# Salvar mapa interativo
mapa.save("rotas_entrega_optimizada_numerada.html")
mapa
