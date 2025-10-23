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
