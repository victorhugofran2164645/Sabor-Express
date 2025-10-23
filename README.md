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

## 🛠️ 6️⃣ Parte Prática — Código, Dados e Outputs

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

perl
Copiar código

### Arquivos de Dados

**`data/locais.csv`**
```csv
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

csv
Copiar código
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

json
Copiar código
{
  "algoritmo": "a_star",
  "caminho": ["Restaurante","Cruzamento 2","Cruzamento 1","Cliente 1"],
  "custo": 15
}
Clusterização de pedidos (/api/clusterizar)

⚙️ 7️⃣ Instruções de Execução
1️⃣ Pré-requisitos
Python 3.8+

Git

pip

2️⃣ Clonar Repositório
bash
Copiar código
git clone https://github.com/victorhugofran2164645/Sabor-Express.git
cd Sabor-Express
3️⃣ Criar e Ativar Ambiente Virtual
bash
Copiar código
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows PowerShell
python -m venv venv
venv\Scripts\Activate.ps1
4️⃣ Instalar Dependências
bash
Copiar código
pip install -r requirements.txt
5️⃣ Executar a API
bash
Copiar código
python app/main.py
Servidor ativo em http://127.0.0.1:5000

6️⃣ Gerar Diagramas Visuais
Diagrama do Grafo

bash
Copiar código
python scripts/gerar_grafo.py
Clusterização de Pedidos

bash
Copiar código
python scripts/gerar_clusterizacao.py
As imagens serão salvas automaticamente em docs/grafo.png e docs/clusterizacao.png.

7️⃣ Testar Endpoints
Calcular rota:

bash
Copiar código
curl -X POST -H "Content-Type: application/json" \
-d '{"inicio":"Restaurante","fim":"Cliente 1","algoritmo":"a_star"}' \
http://127.0.0.1:5000/api/rota
Clusterizar pedidos:

bash
Copiar código
curl -X POST -H "Content-Type: application/json" \
-d '{"pedidos":["Cliente 1","Cliente 2","Cliente 3","Cliente 4"],"num_entregadores":2}' \
http://127.0.0.1:5000/api/clusterizar
