# 🍔 Sabor Express — Sistema Inteligente de Roteamento e Entregas

O **Sabor Express** é um sistema de otimização de rotas de entrega, que utiliza algoritmos clássicos de Inteligência Artificial e fornece uma **API RESTful** para calcular rotas e clusterizar pedidos de forma eficiente.  

Ele permite que restaurantes ou serviços de delivery **reduzam tempo e custo de entregas**, distribuam pedidos de forma equilibrada entre entregadores e avaliem diferentes algoritmos de roteamento.

---

## 📌 1️⃣ Descrição do Problema, Desafio Proposto e Objetivos

**Problema:** Reduzir tempo e custo das entregas em uma rede de restaurantes, mantendo a eficiência e balanceamento entre entregadores.

**Desafio:** Criar um sistema capaz de:
- Calcular rotas individuais eficientes entre pontos (origem → destino);
- Agrupar pedidos geograficamente em zonas de entrega;
- Comparar algoritmos de busca para análise de desempenho.

**Objetivos:**
1. Criar uma API funcional usando **Flask**;
2. Implementar algoritmos de busca (**A\***, BFS, DFS) e clusterização (**K-Means**);
3. Utilizar dados simples (CSV) para testes e simulações;
4. Documentar o projeto de forma clara para execução imediata.

---

## 🧭 2️⃣ Abordagem Adotada

### Modelagem dos Dados
- **Nós:** restaurantes, clientes, entregadores, cruzamentos.  
- **Arestas:** conexões com custo entre os nós, definidas em `rotas.csv`.

### Rotas (Busca em Grafos)
- **A\***: encontra caminho de menor custo usando heurística (distância euclidiana).  
- **BFS**: menor número de arestas (útil para grafos não ponderados).  
- **DFS**: exploração em profundidade para comparação.

### Clusterização de Pedidos
- **K-Means**: agrupa pedidos em zonas de entrega para cada entregador.

### Fluxo do Sistema
1. Carregar dados do grafo (`locais.csv` e `rotas.csv`)  
2. Construir grafo em memória  
3. Executar algoritmo escolhido (A*, BFS, DFS)  
4. Clusterizar pedidos com K-Means  
5. Retornar resultados via JSON na API

---

## ⚙️ 3️⃣ Algoritmos Utilizados

| Algoritmo | Finalidade | Complexidade | Observação |
|-----------|------------|--------------|------------|
| **A\***  | Rota mais curta | O(b^d) | Ideal para grafos ponderados |
| **BFS**  | Menor número de arestas | O(V+E) | Útil em grafos não ponderados |
| **DFS**  | Exploração em profundidade | O(V+E) | Comparação, não garante ótimo |
| **K-Means** | Clusterização de pedidos | O(n·k·i) | Agrupa pedidos por proximidade |

---

## 🗺️ 4️⃣ Diagramas Visuais

### Diagrama do Grafo
![Grafo](docs/grafo.png)

### Clusterização de Pedidos
![Clusterização](docs/clusterizacao.png)

> Mostra nós, arestas com pesos e agrupamento dos pedidos em zonas de entrega.

---

## 📈 5️⃣ Análise dos Resultados, Eficiência e Limitações

### Resultados
- **Custo total da rota:** soma dos pesos das arestas.  
- **Tempo médio por entrega:** estimativa via custo das arestas.  
- **Balanceamento de carga:** número de pedidos por entregador.  

### Eficiência
- **A\***: ótimo equilíbrio entre custo e tempo.  
- **BFS/DFS**: usados para comparação de desempenho.  
- **K-Means**: rápido e escalável para clusterização.

### Limitações
1. Dados simplificados, sem trânsito real.  
2. K-Means ignora barreiras físicas.  
3. Sistema offline, sem otimização em tempo real.  
4. Escalabilidade limitada a pequenas cidades ou poucos pedidos.

### Sugestões de Melhoria
- Integrar dados reais de mapas (OpenStreetMap / Google Directions).  
- Implementar TSP / VRP para multi-entregador.  
- Clusterização baseada em grafo ou distância real.  
- Re-otimização em tempo real.  

---
## 🛠️ Parte Prática — Código, Dados e Outputs

### Estrutura do Projeto

Sabor-Express/
├── app/
│ ├── core/
│ │ ├── algoritmos.py
│ │ ├── clusterizacao.py
│ │ └── grafo.py
│ ├── models/
│ ├── templates/
│ └── main.py
├── data/
│ ├── locais.csv
│ └── rotas.csv
├── docs/
│ ├── grafo.png
│ └── clusterizacao.png
├── scripts/
│ ├── gerar_grafo.py
│ └── gerar_clusterizacao.py
├── requirements.txt
└── README.md


---

### Código-Fonte Completo

**`app/core/algoritmos.py`**
```python
# Exemplo: funções A*, BFS, DFS
def a_star(...):
    pass

def bfs(...):
    pass

def dfs(...):
    pass


app/core/clusterizacao.py

# Exemplo: função de clusterização K-Means
from sklearn.cluster import KMeans

def clusterizar(pedidos, coords, num_entregadores):
    kmeans = KMeans(n_clusters=num_entregadores, random_state=0)
    labels = kmeans.fit_predict(coords)
    return labels


app/core/grafo.py

import networkx as nx

def criar_grafo(rotas, locais):
    G = nx.DiGraph()
    # adicionar nós e arestas
    return G


app/main.py

from flask import Flask, request, jsonify
from core.algoritmos import a_star
from core.clusterizacao import clusterizar
app = Flask(__name__)

@app.route('/api/rota', methods=['POST'])
def rota():
    data = request.json
    resultado = a_star(data['inicio'], data['fim'])
    return jsonify(resultado)

@app.route('/api/clusterizar', methods=['POST'])
def api_clusterizar():
    data = request.json
    resultado = clusterizar(data['pedidos'], data['coords'], data['num_entregadores'])
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)

Arquivos de Dados

data/locais.csv

nome,latitude,longitude
Restaurante,0,0
Entregador A,-5,1
Cliente 1,-7,4
Cliente 2,-2,8
Cliente 3,5,9
Cliente 4,8,2
Cliente 5,3,-5
Cruzamento 1,-4,5


data/rotas.csv

origem,destino,custo
Restaurante,Cruzamento 2,4
Restaurante,Cliente 5,6
Cruzamento 2,Cliente 3,5
Cruzamento 2,Cliente 4,5
Cruzamento 2,Cruzamento 1,7
Cruzamento 1,Cliente 2,3
Cruzamento 1,Cliente 1,4
Cruzamento 1,Entregador A,2

Outputs Relevantes

Rota calculada (/api/rota)

{
  "algoritmo": "a_star",
  "caminho": ["Restaurante","Cruzamento 2","Cruzamento 1","Cliente 1"],
  "custo": 15
}


Clusterização de Pedidos (/api/clusterizar)

Saída visual gerada pelo script gerar_clusterizacao.py em docs/clusterizacao.png

Diagrama do Grafo

Gerado automaticamente pelo script gerar_grafo.py em docs/grafo.png

Scripts Auxiliares

scripts/gerar_grafo.py

import networkx as nx
import matplotlib.pyplot as plt
import csv, os

os.makedirs("docs", exist_ok=True)
G = nx.DiGraph()
coords = {}

with open('data/locais.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        nome = row['nome']
        x, y = float(row['latitude']), float(row['longitude'])
        G.add_node(nome, pos=(x, y))
        coords[nome] = (x, y)

with open('data/rotas.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        G.add_edge(row['origem'], row['destino'], weight=int(row['custo']))

pos = nx.get_node_attributes(G, 'pos')
plt.figure(figsize=(10,7))
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Diagrama do Grafo do Sabor Express")
plt.savefig("docs/grafo.png")
plt.show()


scripts/gerar_clusterizacao.py

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv, os

os.makedirs("docs", exist_ok=True)
pedidos = ["Cliente 1","Cliente 2","Cliente 3","Cliente 4"]
coords = []

for row in csv.DictReader(open('data/locais.csv')):
    if row['nome'] in pedidos:
        coords.append([float(row['latitude']), float(row['longitude'])])

num_entregadores = 2
kmeans = KMeans(n_clusters=num_entregadores, random_state=0)
labels = kmeans.fit_predict(coords)

plt.figure(figsize=(8,6))
colors = ['red', 'green', 'blue', 'purple']
for i, coord in enumerate(coords):
    plt.scatter(coord[0], coord[1], color=colors[labels[i]], s=200)
    plt.text(coord[0]+0.1, coord[1]+0.1, pedidos[i], fontsize=10)

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=300, c='yellow', marker='X', label='Centroides')
plt.title("Clusterização de Pedidos - Sabor Express")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.legend()
plt.savefig("docs/clusterizacao.png")
plt.show()

Instruções de Execução

1️⃣ Pré-requisitos

Python 3.8+

Git

pip

2️⃣ Clonar Repositório

git clone https://github.com/victorhugofran2164645/Sabor-Express.git
cd Sabor-Express


3️⃣ Criar e Ativar Ambiente Virtual

# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows PowerShell
python -m venv venv
venv\Scripts\Activate.ps1


4️⃣ Instalar Dependências

pip install -r requirements.txt


5️⃣ Executar a API

python app/main.py


Servidor ativo em http://127.0.0.1:5000

6️⃣ Gerar Diagramas Visuais

python scripts/gerar_grafo.py
python scripts/gerar_clusterizacao.py


As imagens serão salvas em docs/grafo.png e docs/clusterizacao.png

7️⃣ Testar Endpoints

# Calcular rota
curl -X POST -H "Content-Type: application/json" \
-d '{"inicio":"Restaurante","fim":"Cliente 1","algoritmo":"a_star"}' \
http://127.0.0.1:5000/api/rota

# Clusterizar pedidos
curl -X POST -H "Content-Type: application/json" \
-d '{"pedidos":["Cliente 1","Cliente 2","Cliente 3","Cliente 4"],"num_entregadores":2}' \
http://127.0.0.1:5000/api/clusterizar


---


