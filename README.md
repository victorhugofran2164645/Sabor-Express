# Sabor Express — Sistema Inteligente de Roteamento de Entregas

## 📌 1. Descrição do Problema e Objetivos

No contexto de entregas urbanas de comida, **uma das maiores dificuldades é otimizar as rotas dos entregadores** para reduzir tempo e custo de deslocamento. Este projeto propõe uma solução de roteamento inteligente para:

- Determinar a **rota mais curta** entre o restaurante e os clientes.
- Agrupar pedidos de forma eficiente entre múltiplos entregadores.
- Visualizar as rotas e clusters de pedidos de forma interativa e estática.

**Objetivos do projeto:**

1. Criar um grafo urbano real da cidade para modelar ruas e cruzamentos.
2. Gerar pedidos aleatórios e agrupar em clusters (simulando entregadores).
3. Calcular rotas utilizando algoritmos de caminho mínimo.
4. Exibir resultados de forma interativa e gerar diagramas estáticos para análise.

---

## 🛠️ 2. Abordagem Detalhada

A abordagem adotada é dividida em etapas:

1. **Criação do grafo urbano**:  
   - Usamos a biblioteca **OSMnx** para baixar o grafo de ruas da cidade (São Paulo neste exemplo).  
   - Cada nó do grafo representa um cruzamento ou ponto de interesse, e cada aresta representa uma rua com peso baseado no comprimento.

2. **Geração de pedidos aleatórios**:  
   - Foram selecionados nós aleatórios do grafo para representar pedidos.  
   - Cada pedido tem coordenadas (latitude, longitude) associadas.

3. **Clusterização de pedidos**:  
   - Aplicamos **K-Means** para agrupar os pedidos em clusters correspondentes ao número de entregadores.  
   - Cada cluster representa a área de atuação de um entregador.

4. **Cálculo de rotas**:  
   - Para cada cluster, calculamos a rota entre os pedidos usando **A\*** (camino mínimo ponderado).  
   - Também é possível usar BFS ou DFS para fins de comparação acadêmica, mas **A\*** garante rotas otimizadas por distância.

5. **Visualização**:  
   - Criamos um **mapa interativo com Folium**, mostrando rotas coloridas por cluster e marcadores para cada pedido.  
   - Geramos um **diagrama estático com Matplotlib**, exibindo o grafo, clusters e rotas.

---

## 🧮 3. Algoritmos Utilizados

| Algoritmo | Função no Projeto |
|-----------|-----------------|
| **A\***  | Calcula a rota mais curta entre nós do grafo, considerando distância das ruas. |
| **K-Means** | Agrupa pedidos em clusters geográficos, simulando zonas de entrega. |
| **BFS / DFS (opcional)** | Poderiam ser usados para busca em grafos não ponderados ou comparação acadêmica. |

---

## 📊 4. Diagrama do Grafo / Modelo da Solução

- **Mapa interativo (Folium)**:  
  - Rotas coloridas por cluster.  
  - Marcadores indicando pedidos e centroids.  
  - Salvo como: `rotas_entrega_real.html`.

- **Diagrama estático (Matplotlib)**:  
  - Mostra o grafo, rotas e clusters.  
  - Salvo como: `diagrama_grafo_rotas.png`.

---

## 📈 5. Análise dos Resultados e Eficiência

- As rotas geradas pelo algoritmo **A\*** garantem que cada entregador percorra o menor caminho total dentro do cluster.  
- A clusterização com **K-Means** cria zonas de entrega geograficamente coerentes, reduzindo tempo e distância.  
- O sistema é escalável para múltiplos entregadores e diferentes números de pedidos.  

**Limitações:**

1. O TSP dentro de cada cluster é simplificado; a ordem dos pedidos segue a sequência no DataFrame.  
2. BFS/DFS não são otimizados para distância, apenas para conexão de nós.  
3. Não considera tráfego em tempo real ou restrições como horários de entrega.  

**Sugestões de melhoria:**

- Implementar **TSP exato ou heurístico** para minimizar distância percorrida.  
- Integrar dados de **tráfego em tempo real** (Google Maps API ou OpenStreetMap atualizações).  
- Adicionar otimização baseada em **tempo de entrega e prioridade de pedidos**.  

---

## 🛠️ 6. Parte Prática — Código, Dados e Outputs

### Estrutura do Projeto
Sabor-Express/
├── src/
│ └── rota_inteligente.py # Código principal
├── data/
│ └── pedidos.csv (opcional)
├── docs/
│ ├── diagrama_grafo_rotas.png
│ └── rotas_entrega_real.html
├── requirements.txt
└── README.md


### Instruções de Execução

1. **Pré-requisitos:**

```bash
Python 3.8+
pip

Instalar dependências:

pip install osmnx folium networkx scikit-learn ortools matplotlib pandas numpy


Executar código principal:

python src/rota_inteligente.py


Gera:

rotas_entrega_real.html → mapa interativo

diagrama_grafo_rotas.png → diagrama estático do grafo

✅ 7. Conclusão

Este projeto demonstra uma solução completa para otimização de entregas urbanas, integrando:

Modelagem de grafo real da cidade

Clusterização de pedidos

Cálculo de rotas com A*

Visualização interativa e estática

Ele é flexível, escalável e pronto para testes com diferentes cidades, números de pedidos e entregadores.
