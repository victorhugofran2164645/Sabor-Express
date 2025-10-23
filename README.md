# Sabor Express — Sistema Inteligente de Roteamento e Entregas

Este projeto implementa um backend inteligente para otimização de rotas de entrega, utilizando algoritmos clássicos de Inteligência Artificial e expondo a funcionalidade através de uma API RESTful construída com Flask.

## 📌 Descrição do Problema, Desafio Proposto e Objetivos

**Problema:** otimizar a operação de entregas para uma pequena rede de restaurantes, reduzindo tempo e custo total das rotas e balanceando a carga de trabalho entre entregadores.  
**Desafio:** projetar um sistema que, com dados limitados (lista de locais e conexões com custo), seja capaz de:
- Calcular rotas individuais eficientes entre pontos (origem → destino);
- Agrupar pedidos geograficamente em zonas para atribuição a entregadores;
- Permitir comparações entre estratégias de busca para análise didática e experimental.  

**Objetivos do projeto:**
1. Implementar uma API RESTful que exponha serviços de cálculo de rota e clusterização de pedidos.  
2. Aplicar algoritmos clássicos de IA (A*, BFS, DFS) para busca em grafos e K-Means para clusterização geográfica.  
3. Criar um formato de dados simples (CSV) para facilitar testes offline e reprodutibilidade.  
4. Fornecer documentação, exemplos e ferramentas para que qualquer usuário consiga rodar o sistema localmente.

---

## 🧭 Explicação Detalhada da Abordagem Adotada

### 1) Modelagem dos Dados
- **Nós:** cada local (restaurante, cliente, entregador, cruzamento) é um nó no grafo, identificado por nome e coordenadas (latitude, longitude).  
- **Arestas:** as conexões entre nós têm um atributo `custo` que representa tempo/energia/distância entre os pontos (valor arbitrário definido em `rotas.csv`).  

### 2) Rotas (Busca em Grafos)
- Para calcular uma rota entre dois nós, o sistema carrega o grafo (lista de nós + arestas) e aplica um algoritmo de busca:
  - **A\***: usa heurística (distância euclidiana entre nó atual e objetivo) para guiar a busca; retorna caminho de menor custo.  
  - **BFS**: explora por camadas, útil para menor número de arestas (quando arestas têm custo uniforme).  
  - **DFS**: varre profundidade primeiro — incluído para fins comparativos e educacionais.  

### 3) Clusterização de Pedidos
- Para dividir pedidos entre `k` entregadores, usa-se **K-Means** sobre as coordenadas (latitude, longitude) dos pedidos.  
- Após a atribuição, cada cluster representa a zona de entrega de um entregador; rota final dentro do cluster pode usar A* para ordenação de entrega (heurísticas TSP simples podem ser aplicadas).

### 4) API e Fluxo
- Endpoints principais:
  - `POST /api/rota` — recebe `{inicio, fim, algoritmo}` e retorna `{caminho, custo}`.
  - `POST /api/clusterizar` — recebe `{pedidos, num_entregadores}` e retorna clusters por entregador.
- O fluxo padrão: carregar `locais.csv` + `rotas.csv` → construir grafo → executar algoritmo escolhido → devolver JSON.

---

## ⚙️ Algoritmos Utilizados (resumo técnico)

### A* (A-star)
- **Entrada:** grafo, nó inicial, nó objetivo, função heurística (h).
- **Heurística usada:** distância euclidiana entre coordenadas (admissível se custo ≥ distância direta).  
- **Complexidade:** depende da heurística; no pior caso O(b^d) onde b é fator de ramificação e d profundidade, mas geralmente muito mais eficiente que busca cega.

### BFS (Breadth-First Search)
- **Uso:** encontrar caminho com menor número de arestas (quando arestas tem custo uniforme).  
- **Complexidade:** O(V + E) em tempo e O(V) em memória (V = vértices, E = arestas).

### DFS (Depth-First Search)
- **Uso:** comparação; pode encontrar caminhos profundos rapidamente, mas não garante optimalidade.  
- **Complexidade:** O(V + E) em tempo, pode ter uso menor de memória em certos grafos.

### K-Means
- **Entrada:** coordenadas dos pedidos, k = número de entregadores.  
- **Saída:** k clusters (cada cluster contém índices/nome dos pedidos).  
- **Observação:** K-Means assume clusters convexos; em geografias complexas, pode não refletir rotas reais (considerar clustering via distância por grafo).

---

## 🗺️ Diagrama do Grafo / Modelo (ASCII)

markdown
Copiar código
        Restaurante
        /     \
 (4)  /       \ (6)
    /           \
Cruzamento2 ------ Cliente5
/ |
(7) | (5)
/
Cruzamento1 Cliente3
/ |
(2) (4) (3)
Ent. Cliente1 Cliente2

css
Copiar código

> Legenda: números entre parênteses representam custo da aresta.  
> Observação: para o README, recomendo um arquivo `assets/grafo.png` com o mesmo diagrama gerado por código (ex.: Matplotlib + NetworkX) para visual mais profissional.

**Sugestão de comando** (gera imagem localmente):
```python
# Exemplo rápido (NetworkX + Matplotlib)
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_weighted_edges_from([
  ("Restaurante","Cruzamento2",4),
  ("Restaurante","Cliente5",6),
  ("Cruzamento2","Cliente3",5),
  ("Cruzamento2","Cliente4",5),
  ("Cruzamento2","Cruzamento1",7),
  ("Cruzamento1","Cliente2",3),
  ("Cruzamento1","Cliente1",4),
  ("Cruzamento1","Entregador A",2),
])
pos = nx.spring_layout(G)  # ou pos baseado em coordenadas reais
nx.draw(G, pos, with_labels=True, node_size=800)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.savefig('assets/grafo.png', dpi=200)
📈 Análise dos Resultados, Eficiência, Limitações e Sugestões de Melhoria
Análise de Resultados (o que medir)
Custo total da rota: soma dos pesos das arestas para cada entrega.

Tempo médio por entrega: aproximação com custos convertidos para tempo.

Balanceamento de carga: número de pedidos por entregador após clusterização.

Comparativo A/BFS/DFS:* tempo de execução e custo/qualidade do caminho encontrado.

Eficiência
A* tende a entregar o melhor compromisso entre tempo de busca e custo do caminho se a heurística for informativa.

BFS/DFS são úteis para comparação; BFS é ótima em grafos não ponderados, DFS não é recomendada para busca ótima.

K-Means é rápido e escalável, mas sua qualidade depende da distribuição geográfica dos pedidos.

Limitações conhecidas
Dados discretos e simplificados: custos são fixos em rotas.csv — não refletem trânsito, horários, bloqueios.

Heurística A*: se heurística não for admissível, A* pode não ser ótima.

K-Means não considera estradas: clusterização por coordenada pode agrupar pontos separados por barreiras (rios, rodovias sem ligação direta).

Escalabilidade: para centenas de entregas e restrições (janela de tempo, capacidade), será necessário otimizar ou usar heurísticas avançadas / metaheurísticas.

Estado estático: sistema atual é offline — não lida com pedidos em tempo real nem com reotimizações dinâmicas.

Sugestões de Melhoria
Integrar dados reais de mapa (OpenStreetMap ou Google Directions) para gerar custos baseados em distância/tempo rodoviário.

Adicionar um módulo TSP / VRP (Vehicle Routing Problem) para otimização multi-entregador com restrições reais (capacidade, janelas de tempo).

Clustering baseado em grafo: usar algoritmos que considerem custo em grafo (ex.: spectral clustering com matriz de distâncias por caminho mínimo).

Monitoramento e re-otimização em tempo real: permitir re-roteamento quando um entregador muda de rota ou um pedido é cancelado.

Benchmark automatizado: scripts que rodem A*, BFS, DFS em múltiplos pares (início, fim) e gerem relatório com tempos e custos para análise.

Containerização e CI: Docker + GitHub Actions para testes automatizados e builds reprodutíveis.



## Funcionalidades Principais

* **Cálculo de Rota Ótima**: Utiliza o algoritmo A* para encontrar o caminho mais rápido (menor custo) entre dois pontos em um mapa modelado como um grafo.
* **Comparação de Algoritmos**: Permite o cálculo de rotas usando BFS e DFS para fins de análise e comparação de desempenho.
* **Clusterização de Entregas**: Emprega o algoritmo K-Means para agrupar geograficamente múltiplos pedidos, permitindo a criação de zonas de entrega otimizadas para os entregadores.

## Estrutura do Projeto

O projeto segue uma arquitetura modular para garantir a separação de responsabilidades e a manutenibilidade.

```
Sabor-Express/
├── app/
│   ├── core/              # "Cérebro" do projeto com a lógica de IA
│   │   ├── algoritmos.py
│   │   ├── clusterizacao.py
│   │   └── grafo.py
│   ├── models/            # Modelos de dados da aplicação
│   ├── templates/         # Arquivos de interface (HTML)
│   └── main.py            # Servidor da API Flask e definição das rotas
│
├── venv/                  # Ambiente virtual (ignorado pelo .gitignore)
├── requirements.txt       # Dependências do projeto
└── README.md              # Esta documentação
```

## Como Executar

### 1. Pré-requisitos

* Python 3.8+
* pip

### 2. Instalação

Clone o repositório e instale as dependências:

```bash
git clone [https://github.com/victorhugofran2164645/Sabor-Express.git](https://github.com/victorhugofran2164645/Sabor-Express.git)
cd Sabor-Express
pip install -r requirements.txt
```

### 3. Executando a API

Para iniciar o servidor Flask, execute:

```bash
python app/main.py
```

O servidor estará rodando em `http://127.0.0.1:5000`.

## Como Usar a API

Você pode interagir com a API usando ferramentas como `curl` ou Postman.

### Exemplo 1: Calcular uma Rota

**Endpoint:** `POST /api/rota`

Calcula o caminho entre um ponto de início e um de fim.

**Comando de Exemplo:**

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"inicio": "Restaurante", "fim": "Cliente 1", "algoritmo": "a_star"}' \
[http://127.0.0.1:5000/api/rota](http://127.0.0.1:5000/api/rota)
```

**Resposta Esperada:**

```json
{
  "algoritmo": "a_star",
  "caminho": [
    "Restaurante",
    "Cruzamento 2",
    "Cruzamento 1",
    "Cliente 1"
  ],
  "custo": 15
}
```

### Exemplo 2: Agrupar Pedidos (Clusterizar)

**Endpoint:** `POST /api/clusterizar`

Agrupa uma lista de pedidos em um número definido de clusters (zonas de entrega).

**Comando de Exemplo:**

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
      "pedidos": ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4"],
      "num_entregadores": 2
    }' \
[http://127.0.0.1:5000/api/clusterizar](http://127.0.0.1:5000/api/clusterizar)
```

**Resposta Esperada:**

```json
{
    "clusters_de_entrega": {
        "0": [
            "Cliente 3",
            "Cliente 4"
        ],
        "1": [
            "Cliente 1",
            "Cliente 2"
        ]
    }
}
```
**Arquivos de dados utilizados**

locais.csv

nome,latitude,longitude
Restaurante,0,0
Entregador A,-5,1
Cliente 1,-7,4
Cliente 2,-2,8
Cliente 3,5,9
Cliente 4,8,2
Cliente 5,3,-5
Cruzamento 1,-4,5

rotas.csv

origem,destino,custo
Restaurante,Cruzamento 2,4
Restaurante,Cliente 5,6
Cruzamento 2,Cliente 3,5
Cruzamento 2,Cliente 4,5
Cruzamento 2,Cruzamento 1,7
Cruzamento 1,Cliente 2,3
Cruzamento 1,Cliente 1,4
Cruzamento 1,Entregador A,2
Cliente 1,Entregador A,3
Cruzamento 2,3,4


### Diagrama do Modelo de Grafo
![Diagrama do Grafo do Sabor Express](https://github.com/user-attachments/assets/b24bdfb2-c271-4ad1-936d-ff3fa9f1eda7)


**Instruções claras para execução do projeto, com bibliotecas necessárias, comandos
e passo a passo.**

🚀 Guia de Execução e Uso do Sabor Express
Este guia fornece um passo a passo detalhado para configurar o ambiente, instalar as dependências e executar o sistema Sabor Express em seu computador local.

📋 Pré-requisitos
Antes de começar, garanta que você tenha os seguintes softwares instalados em seu sistema:

Python: Versão 3.8 ou superior.

Para verificar, abra um terminal e digite: python --version

Git: O sistema de controle de versão para baixar o código.

Para verificar, abra um terminal e digite: git --version

⚙️ Instalação (Passo a Passo)
Siga estes comandos no seu terminal para configurar o projeto.

1. Clonar o Repositório
Este comando fará o download de uma cópia completa do projeto do GitHub para sua máquina.

Bash

git clone https://github.com/victorhugofran2164645/Sabor-Express.git
2. Entrar na Pasta do Projeto
É crucial executar todos os comandos seguintes de dentro da pasta do projeto.

Bash

cd Sabor-Express
3. Criar e Ativar um Ambiente Virtual (Recomendado)
Isso cria um ambiente Python isolado para o projeto, evitando conflitos com outras bibliotecas do seu sistema.

Bash

# Criar o ambiente virtual (venv é o nome da pasta)
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS ou Linux:
source venv/bin/activate
Após ativar, você verá (venv) no início da linha do seu terminal.

4. Instalar as Bibliotecas Necessárias
Este comando lê o arquivo requirements.txt e instala todas as bibliotecas que o projeto utiliza.

Bash

pip install -r requirements.txt
▶️ Executando a Aplicação
Com o ambiente configurado e as dependências instaladas, você já pode iniciar o servidor da API.

1. Iniciar o Servidor Flask
Execute o seguinte comando a partir da pasta raiz do projeto (Sabor-Express):

Bash

python app/main.py
2. Verificar a Saída
Se tudo correu bem, você verá uma saída no seu terminal indicando que o servidor está rodando, geralmente em http://127.0.0.1:5000.

 * Serving Flask app 'main'
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
Deixe este terminal aberto! O servidor precisa continuar rodando para que a API funcione.

🛠️ Usando a API (Testando os Endpoints)
Para interagir com a API, abra um novo terminal (deixe o primeiro rodando o servidor) e use os comandos curl abaixo.

1. Testar o Cálculo de Rota (/api/rota)
Este comando envia uma requisição POST para calcular a rota mais curta do "Restaurante" até o "Cliente 1" usando o algoritmo A*.

Bash

curl -X POST -H "Content-Type: application/json" \
-d '{"inicio": "Restaurante", "fim": "Cliente 1", "algoritmo": "a_star"}' \
http://127.0.0.1:5000/api/rota
Resposta Esperada:

JSON

{
  "algoritmo": "a_star",
  "caminho": [
    "Restaurante",
    "Cruzamento 2",
    "Cruzamento 1",
    "Cliente 1"
  ],
  "custo": 15
}
2. Testar a Clusterização de Pedidos (/api/clusterizar)
Este comando pede para o sistema agrupar 4 pedidos em 2 zonas de entrega para 2 entregadores.

Bash

curl -X POST -H "Content-Type: application/json" \
-d '{
      "pedidos": ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4"],
      "num_entregadores": 2
    }' \
http://127.0.0.1:5000/api/clusterizar
Resposta Esperada:

JSON

{
    "clusters_de_entrega": {
        "0": [
            "Cliente 3",
            "Cliente 4"
        ],
        "1": [
            "Cliente 1",
            "Cliente 2"
        ]
    }
}
⏹️ Parando a Aplicação
Para desligar o servidor, volte para o primeiro terminal (onde o servidor está rodando) e pressione as teclas Ctrl + C.
