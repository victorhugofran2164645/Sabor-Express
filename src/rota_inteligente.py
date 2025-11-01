import os
import osmnx as ox
import networkx as nx
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import folium
import random
import matplotlib.pyplot as plt

cidade = "São Paulo, Brasil"
G = ox.graph_from_place(cidade, network_type="drive")
nodes = list(G.nodes)
coords_nodes = {n:(G.nodes[n]['y'], G.nodes[n]['x']) for n in nodes}

num_pedidos = 20
pedidos_nodes = random.sample(nodes, num_pedidos)
pedidos_coords = [coords_nodes[n] for n in pedidos_nodes]

pedidos = pd.DataFrame({
    'id': list(range(1, num_pedidos+1)),
    'node': pedidos_nodes,
    'lat': [c[0] for c in pedidos_coords],
    'lon': [c[1] for c in pedidos_coords]
})

num_veiculos = 3
kmeans = KMeans(n_clusters=num_veiculos, random_state=0)
pedidos['cluster'] = kmeans.fit_predict(pedidos[['lat','lon']])

rotas_clusters = {}
for c in pedidos['cluster'].unique():
    cluster_pedidos = pedidos[pedidos['cluster']==c]
    tsp_order = cluster_pedidos['id'].tolist()
    rota = []
    for i in range(len(tsp_order)-1):
        start = cluster_pedidos.iloc[i]['node']
        end = cluster_pedidos.iloc[i+1]['node']
        caminho = nx.astar_path(G, source=start, target=end, weight='length')
        rota.extend(caminho[:-1])
    rota.append(cluster_pedidos.iloc[-1]['node'])
    rotas_clusters[c] = rota

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
    cluster_pedidos = pedidos[pedidos['cluster']==cluster_id]
    for _, row in cluster_pedidos.iterrows():
        folium.Marker(
            location=(row['lat'], row['lon']),
            popup=f'Pedido {row["id"]}',
            icon=folium.Icon(color=cores[cluster_id % len(cores)])
        ).add_to(mapa)

os.makedirs("../docs", exist_ok=True)
mapa.save("../docs/rotas_entrega_real.html")
plt.figure(figsize=(10,10))
for cluster_id, rota_nodes in rotas_clusters.items():
    rota_coords = np.array([coords_nodes[n] for n in rota_nodes])
    plt.plot(rota_coords[:,1], rota_coords[:,0], 
             color=cores[cluster_id % len(cores)], 
             linewidth=2, label=f'Veículo {cluster_id}')
plt.scatter(pedidos['lon'], pedidos['lat'], c='black', s=50, label='Pedidos')
plt.title("Diagrama de Rotas e Clusters - Sabor Express")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.savefig("../docs/diagrama_grafo_rotas.png")
plt.show()
