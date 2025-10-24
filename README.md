# Sabor Express — Sistema Inteligente de Roteamento de Entregas

## 📌 1. Descrição do Problema e Objetivos

No contexto de entregas urbanas de comida, **otimizar as rotas dos entregadores** é essencial para reduzir tempo e custo de deslocamento. Este projeto oferece uma solução de roteamento inteligente que:

- Determina a **rota mais curta** entre o restaurante e os clientes.
- Agrupa pedidos de forma eficiente entre múltiplos entregadores.
- Visualiza rotas e clusters de pedidos de forma interativa e estática.

**Objetivos do projeto:**

1. Criar um grafo urbano real da cidade (São Paulo por padrão).
2. Gerar pedidos aleatórios e agrupar em clusters (simulando entregadores).
3. Calcular rotas usando algoritmos de caminho mínimo.
4. Exibir resultados em mapas interativos e diagramas estáticos.

---

## 🛠️ 2. Estrutura do Projeto

Sabor-Express/
├── src/
│ └── rota_inteligente.py # Código principal do projeto
├── data/
│ └── pedidos.csv (opcional) # Arquivo CSV de pedidos gerados
├── docs/
│ ├── diagrama_grafo_rotas.png # Diagrama estático do grafo com rotas
│ └── rotas_entrega_real.html # Mapa interativo com rotas e clusters
├── requirements.txt # Dependências do projeto
└── README.md


---

## 🧮 3. Algoritmos Utilizados

| Algoritmo | Função no Projeto |
|-----------|-----------------|
| **A\***  | Calcula a rota mais curta entre nós do grafo, considerando distância das ruas. |
| **K-Means** | Agrupa pedidos em clusters geográficos, simulando zonas de entrega para cada entregador. |
| **BFS / DFS (opcional)** | Poderiam ser usados para estudo acadêmico, mas não garantem rotas mínimas ponderadas. |

---

## 📊 4. Abordagem Detalhada

1. **Criação do grafo urbano**:  
   - Utilizamos **OSMnx** para baixar o grafo de ruas da cidade.  
   - Cada nó representa um cruzamento e cada aresta uma rua com peso baseado na distância.

2. **Geração de pedidos aleatórios**:  
   - Seleção de nós aleatórios do grafo para simular pedidos.

3. **Clusterização de pedidos**:  
   - Aplicamos **K-Means** para dividir pedidos em clusters, cada um representando a área de atuação de um entregador.

4. **Cálculo de rotas**:  
   - Para cada cluster, calculamos a rota entre os pedidos usando **A\***.  
   - Permite otimização de percurso por distância.

5. **Visualização**:  
   - **Mapa interativo Folium** com rotas coloridas por cluster.  
   - **Diagrama estático Matplotlib** mostrando grafo, clusters e rotas.

---

## 📈 5. Outputs Relevantes

- **Mapa interativo**: `docs/rotas_entrega_real.html`  
  - Mostra rotas de cada entregador e marcadores de pedidos.

- **Diagrama estático**: `docs/diagrama_grafo_rotas.png`  
  - Exibe o grafo urbano, rotas A* e clusters de pedidos coloridos.

- **Exemplo de CSV de pedidos (opcional)**: `data/pedidos.csv`  

---

## ⚙️ 6. Instruções de Execução

### 6.1 Pré-requisitos

- Python 3.8 ou superior  
- pip  

### 6.2 Instalar dependências

```bash
pip install osmnx folium networkx scikit-learn ortools matplotlib pandas numpy

### 6.3 Executar o código principal

python src/rota_inteligente.py

### 6.4 Resultado esperado

Mapa interativo gerado: docs/rotas_entrega_real.html

Diagrama estático gerado: docs/diagrama_grafo_rotas.png

---

## 📝 7. Análise dos Resultados

Rotas calculadas com A* garantem o menor percurso total para cada entregador.

Clusterização com K-Means otimiza zonas de entrega.

Sistema escalável para múltiplos pedidos e entregadores.

Limitações:

Ordem de entrega no cluster simplificada (TSP não exato).

BFS/DFS não consideram peso das ruas.

Não considera tráfego em tempo real.

Sugestões de melhoria:

Implementar TSP heurístico ou exato para otimizar a sequência de entregas.

Integrar tráfego em tempo real ou restrições de tempo de entrega.

Permitir personalização de clusters por prioridade de pedido ou distância máxima.











