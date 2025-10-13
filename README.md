🛵 Sabor Express — Sistema Inteligente de Roteamento e Entregas

📖 1. Descrição do Problema

O aumento da demanda por serviços de delivery exige soluções eficientes para planejar rotas de entrega, reduzindo o tempo de deslocamento, custos de combustível e impacto ambiental.
Empresas que não otimizam suas rotas enfrentam atrasos, entregas incorretas e insatisfação dos clientes.

O desafio central é encontrar o caminho mais rápido e eficiente entre múltiplos pontos de entrega, levando em consideração fatores como:

Distâncias variáveis entre locais;

Trânsito e restrições de vias;

Distribuição geográfica dos pedidos.

🎯 2. Desafio Proposto

Desenvolver um aplicativo inteligente de roteamento de entregas chamado Sabor Express, capaz de:

Calcular automaticamente a rota ótima entre restaurante, entregador e cliente;

Integrar diferentes perfis de usuários (administrador, restaurante, entregador, cliente);

Exibir um mapa de rotas em formato de grafo, mostrando conexões e custos de deslocamento;

Servir como base para futuras integrações com Google Maps API, GPS e bancos de dados geográficos.

🎯 3. Objetivos do Projeto
Objetivo Geral

Criar um sistema inteligente de gerenciamento e otimização de rotas para entregas de alimentos, aplicando algoritmos clássicos de Inteligência Artificial.

Objetivos Específicos

Implementar o algoritmo A* para encontrar o caminho mais curto entre dois pontos;

Comparar o desempenho com BFS e DFS;

Utilizar K-Means para agrupar entregas por região;

Fornecer uma API funcional (Flask) para cálculo de rotas;



Estruturar o código de forma modular, testável e documentada;

Disponibilizar o projeto publicamente no GitHub com testes automatizados e pipeline CI/CD.


Explicação detalhada da abordagem adotada

O sistema "Sabor Express" adota uma abordagem multifacetada e inteligente para resolver o complexo problema de roteamento de entregas. A estratégia central combina algoritmos de otimização de rotas, clusterização de dados geográficos e uma arquitetura de microsserviços robusta para criar uma solução completa e eficiente. A seguir, detalhamos cada pilar da abordagem adotada.

1. Modelagem do Problema como um Grafo
A base para qualquer sistema de roteamento é a representação do mundo real em um formato que um computador possa entender. O "Sabor Express" modela a área de entrega como um grafo. Nesta estrutura:

Nós (Vértices): Representam os pontos de interesse: a localização do restaurante, a posição atual dos entregadores e os endereços dos clientes.

Arestas (Conexões): Representam os possíveis trajetos entre os nós. Cada aresta possui um peso, que pode simbolizar a distância, o tempo estimado de viagem (considerando trânsito) ou o custo de combustível.

Essa representação em grafo é fundamental para a aplicação dos algoritmos de busca de caminho.

2. Otimização de Rotas com Algoritmo A* (A-Star)
Para a principal tarefa de encontrar o caminho mais curto e eficiente entre dois pontos (restaurante-cliente, entregador-cliente), o projeto implementa o algoritmo A*.

O que é o A?:* É um algoritmo de busca informada, considerado um dos mais eficientes para encontrar o caminho de menor custo em um grafo. Ele é uma extensão do algoritmo de Dijkstra, mas com uma melhoria crucial: o uso de uma heurística.

Como funciona: O A* avalia qual nó explorar a seguir com base em dois fatores:

g(n): O custo real do caminho desde o nó inicial até o nó atual n.

h(n): O custo heurístico estimado do nó atual n até o nó de destino. No contexto de mapas, uma heurística comum é a distância Euclidiana (a distância em linha reta), que é uma estimativa otimista e nunca superestima o custo real.
A decisão é tomada com base na função f(n) = g(n) + h(n). Ao priorizar os nós com o menor valor de f(n), o A* explora de forma inteligente as direções mais promissoras, evitando caminhos que já são longos ou que se afastam do objetivo.

Por que o A?:* Foi escolhido por ser ótimo (garante encontrar o menor caminho se a heurística for admissível) e completo (sempre encontrará uma solução se ela existir), além de ser significativamente mais rápido que algoritmos não informados em grafos grandes, como os que representam cidades.

3. Análise Comparativa com BFS e DFS
Para validar a escolha do A* e demonstrar a superioridade de uma busca informada, o projeto realiza uma comparação de desempenho com dois algoritmos clássicos de busca não informada:

Busca em Largura (BFS - Breadth-First Search): Explora o grafo "camada por camada". A partir de um nó inicial, visita todos os seus vizinhos diretos, depois os vizinhos dos vizinhos, e assim por diante. O BFS é ótimo para encontrar o caminho mais curto em termos de número de arestas (não de custo/peso), mas é ineficiente em grafos grandes, pois explora em todas as direções de forma "cega".

Busca em Profundidade (DFS - Depth-First Search): Explora o grafo seguindo um caminho até o seu "fundo" antes de retroceder (backtracking) e tentar outro. O DFS não garante encontrar o caminho mais curto e pode ser muito ineficiente se seguir por um ramo muito longo e incorreto do grafo.

A comparação evidenciará como o A* economiza recursos computacionais (tempo e memória) ao direcionar a busca, um fator crítico para uma aplicação em tempo real.

4. Agrupamento de Entregas com K-Means
Para otimizar a logística de múltiplos pedidos, o "Sabor Express" utiliza o algoritmo de clusterização K-Means.

O que é o K-Means?: É um algoritmo de aprendizado de máquina não supervisionado que agrupa um conjunto de dados em K clusters (grupos) distintos. O agrupamento é feito com base na similaridade, que, neste caso, é a proximidade geográfica.

Como funciona:

O administrador define o número K de clusters desejado (por exemplo, correspondendo ao número de entregadores disponíveis).

O algoritmo posiciona K centróides (pontos centrais) aleatoriamente no mapa.

Cada ponto de entrega é atribuído ao centróide mais próximo.

A posição de cada centróide é recalculada para ser a média de todos os pontos de entrega que lhe foram atribuídos.

Os passos 3 e 4 são repetidos até que a posição dos centróides se estabilize.

Aplicação no "Sabor Express": O K-Means será usado para agrupar geograficamente os pedidos pendentes. Isso permite criar "zonas de entrega". Em vez de calcular rotas individuais para pedidos dispersos, o sistema pode atribuir um cluster inteiro de entregas a um único entregador, que então terá sua rota otimizada (usando A*) para atender a todos os clientes daquele cluster. Essa abordagem reduz drasticamente as distâncias percorridas e o tempo total de operação.

5. Arquitetura Baseada em API com Flask
Para garantir que o sistema seja modular, escalável e acessível por diferentes plataformas (aplicativo móvel, painel web), toda a lógica de negócio será encapsulada em uma API (Interface de Programação de Aplicações) desenvolvida com Flask.

O que é Flask?: É um microframework para desenvolvimento web em Python, conhecido por sua simplicidade, flexibilidade e leveza.

Função no Projeto: A API Flask atuará como o "cérebro" do sistema. Ela receberá requisições dos diferentes perfis de usuário e orquestrará as operações:

Cliente/Restaurante: Um restaurante solicita o cálculo de uma rota para uma nova entrega. A API recebe as coordenadas, executa o algoritmo A* e retorna a rota ótima.

Administrador: Um administrador solicita o agrupamento de todas as entregas pendentes. A API executa o K-Means e retorna os clusters de entrega.

Entregador: O aplicativo do entregador consulta a API para obter sua próxima rota otimizada, que pode incluir múltiplos pontos de entrega dentro de seu cluster.

Essa arquitetura desacopla a lógica complexa dos algoritmos da interface do usuário (front-end), facilitando a manutenção, os testes e futuras integrações, como a conexão com o Google Maps para visualização e navegação em tempo real.
