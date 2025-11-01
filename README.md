# 🚚 Projeto Sabor Express — Rotas Otimizadas

## Descrição do Problema
No contexto de entregas urbanas, empresas enfrentam desafios para organizar rotas eficientes, reduzir custos com combustível e tempo, e garantir entregas rápidas para múltiplos clientes. A complexidade aumenta quando há vários veículos e centenas de pedidos espalhados pela cidade.

O problema central é otimizar a distribuição de pedidos entre entregadores e determinar a melhor sequência de entregas, considerando as distâncias reais entre endereços.

---

## Desafio Proposto
O desafio do projeto é criar um sistema que, dado um conjunto de pedidos em uma cidade:

- Agrupe os pedidos de forma eficiente entre múltiplos veículos/entregadores.
- Defina a ordem ideal de entrega de cada veículo, minimizando a distância total percorrida.
- Gere uma visualização interativa das rotas, permitindo acompanhar a sequência de entregas em um mapa.

---

## Objetivos
O projeto visa:

- Simular pedidos aleatórios em uma cidade para testes de roteirização.
- Agrupar pedidos por entregador utilizando o algoritmo **K-Means**.
- Calcular rotas otimizadas para cada cluster de pedidos com o Problema do Caixeiro Viajante (TSP), usando **OR-Tools**.
- Visualizar interativamente as rotas e a ordem de entrega utilizando **Folium**.
- Fornecer uma solução modular e escalável, que possa ser adaptada para cidades, número de pedidos e veículos diferentes.

---

## Funcionalidades
- Geração de pedidos aleatórios em uma cidade (sem necessidade de arquivos externos).
- Agrupamento de pedidos por entregador com **K-Means**.
- Cálculo de rotas mais curtas usando **OR-Tools** e **NetworkX**.
- Visualização interativa das rotas no mapa com ordem numerada de entregas.
- Suporte para múltiplos veículos e clusters.

---

## Dados de Entrada
> **Importante:** Não existem arquivos de dados externos.  
> Todos os pedidos e suas coordenadas são gerados **automaticamente** pelo script `rota_inteligente.py`.

- DataFrame interno `pedidos` com colunas: `id`, `node`, `lat`, `lon`, `cluster`.

---

## Explicação detalhada da abordagem adotada
- **Construção do grafo urbano** — baixa a malha viária da cidade (ex.: São Paulo) com OSMnx, produzindo um grafo dirigido/ponderado onde nós = cruzamentos / pontos e arestas = ruas com atributos (comprimento, velocidade, etc.)
- Geração de pedidos — o script gera pedidos simulados com id, lat, lon e o nó mais próximo no grafo. Não depende de arquivos externos.
- Clustering (K-Means) — agrupa os pedidos em k clusters (k = número de veículos/entregadores). A ideia: formar regiões geográficas para cada entregador.
- Matriz de distâncias por cluster — para cada par de pedidos dentro de um cluster, calcula a distância real na rede (usando Dijkstra sobre o grafo) e monta a matriz de custos que será usada pelo solver.
- Resolver TSP por cluster — para cada cluster, resolve um TSP (sequência ótima de visitas) com OR-Tools (estratégia PATH_CHEAPEST_ARC por padrão). Resultado: ordem a visitar os pedidos do cluster.
- Construção da rota detalhada — entre cada par de pontos sequenciados, constrói o trajeto real no grafo usando A* (para obter a sequência de nós/ruas entre pedidos).
- Visualização — desenha as rotas no mapa (Folium), com cores por entregador e marcadores numerados na ordem de entrega; salva em HTML.

---

## Algoritmos utilizados
- K-Means – agrupamento dos pedidos em clusters.
- Dijkstra – cálculo de distâncias reais na malha viária.
- A* (A-estrela) – traçado do caminho ótimo entre pontos.
- PATH_CHEAPEST_ARC (OR-Tools) – resolução do TSP por cluster.
- Solver TSP (OR-Tools) – busca da sequência ótima de entregas.
- Nearest Node Mapping (OSMnx) – associação de coordenadas ao nó mais próximo do grafo.
- Folium Visualization – renderização de rotas otimizadas em mapa interativo.


---

## Diagrama do grafo/modelo usado na solução



---


## Análise dos resultados, eficiência da solução, limitações encontradas e sugestões de melhorias
- **Análise dos Resultados**
  
- O algoritmo produziu rotas otimizadas de entrega urbana, simulando um cenário real com:
- 20 pedidos distribuídos em São Paulo (ou outra cidade configurada);
- 3 veículos/entregadores, definidos via K-Means;
- Rotas individuais otimizadas para cada entregador via OR-Tools (TSP);
- Mapa interativo exibindo:
- Pedidos numerados na sequência de entrega;
- Rotas coloridas por entregador;
- Visualização geográfica real (coordenadas OSM).
- Cada cluster representa um conjunto de entregas geograficamente próximas, e dentro de cada grupo, o OR-Tools encontra a sequência mais curta possível para visitar todos os pedidos daquele entregador.
O resultado final é um planejamento de rotas minimizando distâncias totais, visualmente validável no mapa HTML


- **Eficiência da Solução**
- Uso de OSMnx + NetworkX → aproveita dados reais da malha urbana (distâncias reais, não euclidianas).
- Agrupamento prévio (K-Means) → divide o problema grande em subproblemas menores (TSPs menores → muito mais rápidos).
- OR-Tools (Google) → solucionador robusto e rápido, especializado em problemas de roteamento e logística.
- Resultados visualmente claros → fácil validar o comportamento e detectar possíveis rotas ineficientes.
- **Eficiência computacional**
- Para 20 pedidos e 3 veículos, a execução é muito eficiente (segundos).
- A etapa mais custosa é a geração das matrizes de distância (nx.single_source_dijkstra_path_length), pois calcula distâncias reais na malha.
- O uso de K-Means reduz drasticamente o custo da otimização global, pois cada veículo trata um subconjunto de pedidos.
- **Complexidade geral aproximada**
- Distâncias: O(n * (E log V))
- TSP por cluster: O(k * n_c²)
onde n = pedidos, k = veículos, n_c = pedidos por cluster.

- **Limitações Encontradas**
- Escalabilidade O cálculo de todas as distâncias com Dijkstra é caro para muitos pedidos (>100)
- Ausência de ponto inicial (depósito) As rotas começam em um nó arbitrário do cluster, não em um ponto fixo (ex: restaurante)
- Distribuição dos clusters O K-Means considera apenas latitude/longitude — não leva em conta o tempo ou tráfego
- Dependência da qualidade do OSM Áreas com dados incompletos no OpenStreetMap podem gerar distâncias incorretas
- Aleatoriedade A geração de pedidos é aleatória, sem cenário realista de demanda (não reprodutível sem seed)
- Critério de otimização único Minimiza apenas a distância, não o tempo nem restrições (janelas de entrega, capacidade etc.)




















