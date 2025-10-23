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

