# 🍔 Sabor Express — Sistema Inteligente de Roteamento e Entregas

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-API-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)](#)

---

## 🚀 Descrição Geral

O **Sabor Express** é um sistema de **otimização inteligente de rotas de entrega**, que utiliza algoritmos clássicos de Inteligência Artificial e fornece uma **API RESTful** para:

- Calcular rotas eficientes;
- Clusterizar pedidos por localização;
- Comparar desempenho entre algoritmos de busca.

💡 **Objetivo:** reduzir o tempo e custo de entregas para restaurantes ou serviços de delivery, mantendo equilíbrio entre entregadores.

---

## 📌 1️⃣ Descrição do Problema, Desafio e Objetivos

**Problema:**  
Minimizar o tempo e o custo das entregas, mantendo balanceamento entre entregadores.

**Desafio:**  
Criar um sistema capaz de:

- Calcular rotas individuais eficientes (origem → destino);
- Agrupar pedidos em zonas geográficas;
- Avaliar desempenho de algoritmos de busca e clusterização.

**Objetivos Técnicos:**

- Criar uma API funcional usando **Flask**;
- Implementar algoritmos **A\***, **BFS**, **DFS** e **K-Means**;
- Usar dados simples (CSV) para simulação;
- Documentar o projeto para execução imediata.

---

## 🧭 2️⃣ Abordagem Adotada

### Modelagem dos Dados

- **Nós:** restaurantes, clientes, entregadores e cruzamentos  
- **Arestas:** conexões ponderadas definidas em `rotas.csv`  

### Algoritmos de Roteamento

| Algoritmo | Finalidade | Complexidade | Observação |
|-----------|------------|--------------|------------|
| **A\***  | Rota de menor custo | O(b^d) | Ideal para grafos ponderados |
| **BFS**  | Menor número de arestas | O(V+E) | Útil em grafos não ponderados |
| **DFS**  | Exploração em profundidade | O(V+E) | Comparativo, não ótimo |
| **K-Means** | Clusterização de pedidos | O(n·k·i) | Agrupa por proximidade geográfica |

### Fluxo do Sistema

1. Carregar dados (`locais.csv` e `rotas.csv`)  
2. Construir o grafo  
3. Executar o algoritmo de busca escolhido (**A\***, BFS ou DFS)  
4. Clusterizar pedidos com **K-Means**  
5. Retornar resultados via JSON na API  

---

## ⚙️ 3️⃣ Estrutura do Projeto

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

python
Copiar código

---

## 🧩 4️⃣ Principais Códigos

### API Flask

```python
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
🧮 5️⃣ Dados de Entrada
data/locais.csv
csv
Copiar código
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
📈 6️⃣ Resultados e Visualizações
Rota Calculada (/api/rota)
json
Copiar código
{
  "algoritmo": "a_star",
  "caminho": ["Restaurante","Cruzamento 2","Cruzamento 1","Cliente 1"],
  "custo": 15
}
Clusterização de Pedidos (/api/clusterizar)
Saída visual: docs/clusterizacao.png

Diagrama do grafo: docs/grafo.png




🧪 7️⃣ Instruções de Execução
Pré-requisitos
Python 3.8+

Git

pip

1️⃣ Clonar o Repositório
bash
Copiar código
git clone https://github.com/victorhugofran2164645/Sabor-Express.git
cd Sabor-Express
2️⃣ Criar Ambiente Virtual
bash
Copiar código
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows PowerShell
python -m venv venv
venv\Scripts\Activate.ps1
3️⃣ Instalar Dependências
bash
Copiar código
pip install -r requirements.txt
4️⃣ Executar a API
bash
Copiar código
python app/main.py
Servidor ativo em: http://127.0.0.1:5000

5️⃣ Gerar Diagramas
bash
Copiar código
python scripts/gerar_grafo.py
python scripts/gerar_clusterizacao.py
6️⃣ Testar Endpoints
bash
Copiar código
# Calcular rota
curl -X POST -H "Content-Type: application/json" \
-d '{"inicio":"Restaurante","fim":"Cliente 1","algoritmo":"a_star"}' \
http://127.0.0.1:5000/api/rota

# Clusterizar pedidos
curl -X POST -H "Content-Type: application/json" \
-d '{"pedidos":["Cliente 1","Cliente 2","Cliente 3","Cliente 4"],"num_entregadores":2}' \
http://127.0.0.1:5000/api/clusterizar
🔍 8️⃣ Eficiência e Limitações
Aspecto	Observação
Eficiência	A* apresenta ótimo equilíbrio entre custo e tempo; K-Means é rápido e escalável.
Limitações	Dados simplificados; ausência de trânsito real; K-Means ignora barreiras físicas; sem otimização em tempo real.
Melhorias Futuras	Integração com OpenStreetMap / Google Maps, TSP/VRP multi-entregador, clusterização baseada em grafo.

🧑‍💻 9️⃣ Autor
Desenvolvido por: Victor Hugo Fran
📧 Contato: (adicione seu e-mail ou LinkedIn aqui)

📜 🔟 Licença
Este projeto está licenciado sob a MIT License — veja o arquivo LICENSE para mais detalhes.

🏁 Status do Projeto
🚧 Em desenvolvimento ativo — versão inicial funcional com API Flask, algoritmos de busca e clusterização implementados.
