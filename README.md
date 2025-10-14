# Sabor Express — Sistema Inteligente de Roteamento e Entregas

Este projeto implementa um backend inteligente para otimização de rotas de entrega, utilizando algoritmos clássicos de Inteligência Artificial e expondo a funcionalidade através de uma API RESTful construída com Flask.

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
