# Instalar bibliotecas necessárias
!pip install osmnx folium networkx scikit-learn ortools

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
# 1️⃣ Definir a cidade
# -----------------------------
cidade = "São Paulo, Brasil"  # Pode alterar para qualquer cidade

# -----------------------------
# 2️⃣ Baixar a rede viária
# -----------------------------
G = ox.graph_from_place(cidade, network_type='drive')
nodes = list(G.nodes)

# Extrair coordenadas dos nós
coords_nodes = {n:(G.nodes[n]['y'], G.nodes[n]['x']) for n in nodes}

# -----------------------------
# 3️⃣ Gerar pedidos aleatórios nos nós do grafo
# -----------------------------
num_pedidos = 20
pedidos_nodes = random.sample(nodes, num_pedidos)
pedidos_coords = [coords_nodes[n] for n in pedidos_nodes]

pedidos = pd.DataFrame({
    'id': list(range(1, num_pedidos+1)),
    'node': pedidos_nodes,
    'lat': [c[0] for c in pedidos_coords],
    'lon': [c[1] for c in pedidos_coords]
})

# -----------------------------
# 4️⃣ Agrupar pedidos por cluster (entregador)
# -----------------------------
num_veiculos = 3
kmeans = KMeans(n_clusters=num_veiculos, random_state=0)

# Correção: atribuir a uma coluna simples
pedidos['cluster'] = kmeans.fit_predict(pedidos[['lat','lon']])

# -----------------------------
# 5️⃣ Criar matriz de distâncias
# -----------------------------
dist_matrix = []
for i in pedidos['node']:
    dist_matrix.append([nx.shortest_path_length(G, source=i, target=j, weight='length') for j in pedidos['node']])

# -----------------------------
# 6️⃣ Resolver TSP simplificado para cada cluster
# -----------------------------
rotas_clusters = {}
for c in pedidos['cluster'].unique():
    cluster_pedidos = pedidos[pedidos['cluster']==c]
    tsp_order = cluster_pedidos['id'].tolist()  # sequência simples
    rota = []
    for i in range(len(tsp_order)-1):
        start = cluster_pedidos.iloc[i]['node']
        end = cluster_pedidos.iloc[i+1]['node']
        caminho = nx.astar_path(G, source=start, target=end, weight='length')
        rota.extend(caminho[:-1])
    rota.append(cluster_pedidos.iloc[-1]['node'])
    rotas_clusters[c] = rota

# -----------------------------
# 7️⃣ Visualizar mapa interativo
# -----------------------------
# Centro do mapa
latitudes = pedidos['lat']
longitudes = pedidos['lon']
centro = [np.mean(latitudes), np.mean(longitudes)]

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
    
    # Marcadores dos pedidos
    cluster_pedidos = pedidos[pedidos['cluster']==cluster_id]
    for _, row in cluster_pedidos.iterrows():
        folium.Marker(
            location=(row['lat'], row['lon']),
            popup=f'Pedido {row["id"]}',
            icon=folium.Icon(color=cores[cluster_id % len(cores)])
        ).add_to(mapa)

mapa.save("rotas_entrega_real.html")
mapa
