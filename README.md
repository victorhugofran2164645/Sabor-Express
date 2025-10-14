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
