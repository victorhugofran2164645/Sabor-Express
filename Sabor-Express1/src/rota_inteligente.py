"""
rota_inteligente.py
Self-contained script for Sabor-Express routing challenge.
Features:
 - Loads pedidos from CSV (data/pedidos_exemplo.csv)
 - Simple KMeans clustering (from-scratch)
 - Grid graph generation and A* pathfinding (from-scratch)
 - Builds one route per cluster (greedy TSP-like)
 - Saves outputs: docs/diagrama_grafo_rotas.png, docs/rotas_entrega_real.html
 - Command-line interface for parameters
"""
import csv, math, random, argparse, json, os
from pathlib import Path
import matplotlib.pyplot as plt

# -----------------------------
# Utilities
# -----------------------------
def euclid(a,b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

# -----------------------------
# KMeans (simple implementation)
# -----------------------------
def kmeans(points, k, max_iter=100):
    # points: list of (x,y)
    # returns labels list and centroids list
    # init: random k distinct points as centroids
    centroids = random.sample(points, k)
    labels = [None]*len(points)
    for it in range(max_iter):
        changed = False
        # assign
        for i,p in enumerate(points):
            best = min(range(k), key=lambda c: euclid(p, centroids[c]))
            if labels[i] != best:
                labels[i] = best
                changed = True
        # update
        for c in range(k):
            members = [points[i] for i,l in enumerate(labels) if l==c]
            if members:
                cx = sum(m[0] for m in members)/len(members)
                cy = sum(m[1] for m in members)/len(members)
                centroids[c] = (cx,cy)
        if not changed:
            break
    return labels, centroids

# -----------------------------
# Grid graph + A* (on continuous coords snapped to grid)
# -----------------------------
def make_grid_graph(width, height):
    # nodes are (i,j) integer grid coordinates
    neighbors = {}
    for i in range(width):
        for j in range(height):
            nbrs = []
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni,nj = i+di, j+dj
                if 0 <= ni < width and 0 <= nj < height:
                    nbrs.append((ni,nj))
            neighbors[(i,j)] = nbrs
    return neighbors

def astar(start, goal, neighbors):
    # A* on grid where cost=1 per step and heuristic is euclidean distance
    open_set = {start}
    came_from = {}
    gscore = {start:0}
    fscore = {start:euclid(start,goal)}
    while open_set:
        current = min(open_set, key=lambda x: fscore.get(x,float('inf')))
        if current == goal:
            # reconstruct path
            path=[current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return list(reversed(path))
        open_set.remove(current)
        for nbr in neighbors[current]:
            tentative_g = gscore[current] + 1
            if tentative_g < gscore.get(nbr, float('inf')):
                came_from[nbr] = current
                gscore[nbr] = tentative_g
                fscore[nbr] = tentative_g + euclid(nbr,goal)
                if nbr not in open_set:
                    open_set.add(nbr)
    return None

# -----------------------------
# Simple route building per cluster (greedy nearest neighbor)
# -----------------------------
def build_route(points):
    # points: list of (x,y) including depot at first element
    if not points:
        return []
    remaining = points[1:]
    route = [points[0]]
    current = points[0]
    while remaining:
        nearest = min(remaining, key=lambda p: euclid(current,p))
        route.append(nearest)
        remaining.remove(nearest)
        current = nearest
    return route

# -----------------------------
# Main flow
# -----------------------------
def load_pedidos(path):
    pts=[]
    with open(path, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            pts.append({"id": int(row["id"]), "x": float(row["x"]), "y": float(row["y"]), "demand": int(row.get("demand",1))})
    return pts

def snap_to_grid(pt, grid_size):
    # map continuous coords to integer grid indices
    x,y = pt
    return (int(round(x/grid_size)), int(round(y/grid_size)))

def main(args):
    data_path = Path(args.data)
    docs = Path(args.docs)
    docs.mkdir(parents=True, exist_ok=True)
    pedidos = load_pedidos(data_path/"pedidos_exemplo.csv")
    points = [(p["x"], p["y"]) for p in pedidos]
    # number of clusters = number of vehicles; choose heuristically
    k = args.k if args.k else max(1, len(points)//10)
    labels, centroids = kmeans(points, k)
    clusters = {i: [] for i in range(k)}
    for idx,l in enumerate(labels):
        clusters[l].append(pedidos[idx])
    # define depot at center of grid (20,20)
    depot = (20.0, 20.0)
    # grid parameters
    grid_size = 1.0
    width = 41  # 0..40
    height = 41
    neighbors = make_grid_graph(width, height)
    # build routes and get snapped paths
    routes = {}
    for cid, items in clusters.items():
        if not items:
            continue
        pts = [depot] + [(it["x"], it["y"]) for it in items]
        route = build_route(pts)
        # convert to grid nodes and stitch A* between consecutive nodes
        path_nodes = []
        for a,b in zip(route, route[1:]):
            a_node = snap_to_grid(a, grid_size)
            b_node = snap_to_grid(b, grid_size)
            seg = astar(a_node, b_node, neighbors)
            if seg is None:
                seg = [a_node, b_node]
            if path_nodes and path_nodes[-1] == seg[0]:
                path_nodes.extend(seg[1:])
            else:
                path_nodes.extend(seg)
        routes[cid] = {"route_points": route, "path_nodes": path_nodes, "cluster_size": len(items)}
    # Save diagram: plot points, centroids, depot and routes paths
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8,8))
    # grid
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    plt.scatter(xs, ys, c='black', s=20, label='Pedidos')
    # centroids
    cx = [c[0] for c in centroids]
    cy = [c[1] for c in centroids]
    plt.scatter(cx, cy, c='red', marker='x', s=80, label='Centroides (KMeans)')
    # depot
    plt.scatter([depot[0]], [depot[1]], c='green', s=100, marker='*', label='Depósito')
    # draw paths per cluster
    colors = ['tab:blue','tab:orange','tab:purple','tab:olive','tab:brown','tab:pink','tab:gray','tab:cyan']
    for cid, info in routes.items():
        nodes = info["path_nodes"]
        if not nodes:
            continue
        xs_n = [n[0] for n in nodes]
        ys_n = [n[1] for n in nodes]
        plt.plot(xs_n, ys_n, linestyle='-', linewidth=1, label=f'Veículo {cid} (entregas {info["cluster_size"]})', alpha=0.7)
    plt.xlim(0,40)
    plt.ylim(0,40)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    plt.title('Diagrama de grafo e rotas - Sabor-Express (exemplo)')
    plt.xlabel('X (unidades)')
    plt.ylabel('Y (unidades)')
    out_png = docs/"diagrama_grafo_rotas.png"
    plt.savefig(out_png, bbox_inches='tight', dpi=150)
    plt.close()
    # create a simple HTML report
    html = f"""
    <html><head><meta charset='utf-8'><title>Rotas Sabor-Express</title></head><body>
    <h1>Rotas Sabor-Express - Relatório Gerado</h1>
    <p>Clusters (veículos): {k}</p>
    <img src='diagrama_grafo_rotas.png' alt='diagrama' style='max-width:100%;height:auto' />
    <h2>Resumo por veículo</h2>
    <ul>
    """
    for cid, info in routes.items():
        html += f"<li>Veículo {cid}: entregas = {info['cluster_size']}, caminho nós = {len(info['path_nodes'])}</li>"
    html += "</ul></body></html>"
    with open(docs/"rotas_entrega_real.html","w",encoding='utf-8') as f:
        f.write(html)
    # Save a JSON with route details
    with open(docs/"rotas_detalhes.json","w",encoding='utf-8') as f:
        json.dump({"k":k, "clusters": {cid: {"size":info["cluster_size"], "route_points":[list(p) for p in info["route_points"]], "path_nodes":info["path_nodes"]} for cid,info in routes.items()}}, f, indent=2)
    print("Outputs generated: ", out_png, docs/"rotas_entrega_real.html", docs/"rotas_detalhes.json")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rota Inteligente - Sabor-Express demo')
    parser.add_argument('--data', default='../data', help='pasta de dados (contém pedidos_exemplo.csv)')
    parser.add_argument('--docs', default='../docs', help='pasta de outputs/docs')
    parser.add_argument('--k', type=int, default=None, help='numero de clusters/veiculos (opcional)')
    args = parser.parse_args()
    main(args)
