🛵 Sabor Express — Sistema Inteligente de Roteamento e Entregas


📖 1. **Descrição do Problema**

O aumento da demanda por serviços de delivery exige soluções eficientes para planejar rotas de entrega, reduzindo o tempo de deslocamento, custos de combustível e impacto ambiental.
Empresas que não otimizam suas rotas enfrentam atrasos, entregas incorretas e insatisfação dos clientes.

O desafio central é encontrar o caminho mais rápido e eficiente entre múltiplos pontos de entrega, levando em consideração fatores como:

Distâncias variáveis entre locais;

Trânsito e restrições de vias;

Distribuição geográfica dos pedidos.


🎯 2. **Desafio Proposto**

Desenvolver um aplicativo inteligente de roteamento de entregas chamado Sabor Express, capaz de:

Calcular automaticamente a rota ótima entre restaurante, entregador e cliente;

Integrar diferentes perfis de usuários (administrador, restaurante, entregador, cliente);

Exibir um mapa de rotas em formato de grafo, mostrando conexões e custos de deslocamento;

Servir como base para futuras integrações com Google Maps API, GPS e bancos de dados geográficos.


🎯 3. **Objetivos do Projeto**

Objetivo Geral

Criar um sistema inteligente de gerenciamento e otimização de rotas para entregas de alimentos, aplicando algoritmos clássicos de Inteligência Artificial.

Objetivos Específicos

Implementar o algoritmo A* para encontrar o caminho mais curto entre dois pontos;

Comparar o desempenho com BFS e DFS;

Utilizar K-Means para agrupar entregas por região;

Fornecer uma API funcional (Flask) para cálculo de rotas;



Estruturar o código de forma modular, testável e documentada;

Disponibilizar o projeto publicamente no GitHub com testes automatizados e pipeline CI/CD.


**Explicação detalhada da abordagem adotada**


O sistema "Sabor Express" adota uma abordagem multifacetada e inteligente para resolver o complexo problema de roteamento de entregas. A estratégia central combina algoritmos de otimização de rotas, clusterização de dados geográficos e uma arquitetura de microsserviços robusta para criar uma solução completa e eficiente. A seguir, detalhamos cada pilar da abordagem adotada.

**1.Modelagem do Problema como um Grafo**
A base para qualquer sistema de roteamento é a representação do mundo real em um formato que um computador possa entender. O "Sabor Express" modela a área de entrega como um grafo. Nesta estrutura:

Nós (Vértices): Representam os pontos de interesse: a localização do restaurante, a posição atual dos entregadores e os endereços dos clientes.

Arestas (Conexões): Representam os possíveis trajetos entre os nós. Cada aresta possui um peso, que pode simbolizar a distância, o tempo estimado de viagem (considerando trânsito) ou o custo de combustível.

Essa representação em grafo é fundamental para a aplicação dos algoritmos de busca de caminho.

**2. Otimização de Rotas com Algoritmo A* (A-Star)**
Para a principal tarefa de encontrar o caminho mais curto e eficiente entre dois pontos (restaurante-cliente, entregador-cliente), o projeto implementa o algoritmo A*.

O que é o A?:* É um algoritmo de busca informada, considerado um dos mais eficientes para encontrar o caminho de menor custo em um grafo. Ele é uma extensão do algoritmo de Dijkstra, mas com uma melhoria crucial: o uso de uma heurística.

Como funciona: O A* avalia qual nó explorar a seguir com base em dois fatores:

g(n): O custo real do caminho desde o nó inicial até o nó atual n.

h(n): O custo heurístico estimado do nó atual n até o nó de destino. No contexto de mapas, uma heurística comum é a distância Euclidiana (a distância em linha reta), que é uma estimativa otimista e nunca superestima o custo real.
A decisão é tomada com base na função f(n) = g(n) + h(n). Ao priorizar os nós com o menor valor de f(n), o A* explora de forma inteligente as direções mais promissoras, evitando caminhos que já são longos ou que se afastam do objetivo.

Por que o A?:* Foi escolhido por ser ótimo (garante encontrar o menor caminho se a heurística for admissível) e completo (sempre encontrará uma solução se ela existir), além de ser significativamente mais rápido que algoritmos não informados em grafos grandes, como os que representam cidades.

**3. Análise Comparativa com BFS e DFS**
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


Algoritmos Utilizados

De forma a construir uma solução robusta e eficiente, o projeto "Sabor Express" emprega uma combinação estratégica de algoritmos de Inteligência Artificial, cada um com uma função específica dentro do ecossistema de roteamento. A seguir, detalhamos cada um dos algoritmos utilizados.

1. Algoritmo A* (A-Star): A Busca Inteligente pela Rota Ótima
O A* é o coração do sistema de otimização de rotas do "Sabor Express". Ele é responsável por encontrar o caminho mais rápido e de menor custo entre dois pontos, como do restaurante ao cliente.

O que é? O A* é um algoritmo de busca de caminho em grafos que se destaca por sua eficiência. Ele é considerado uma "busca informada" porque utiliza uma heurística (uma "estimativa inteligente") para guiar sua exploração, evitando caminhos que claramente não levarão à solução ótima.

Como funciona? A cada passo, o A* avalia os próximos nós a serem explorados com base na seguinte função:
f(n) = g(n) + h(n)
Onde:

g(n) é o custo real do caminho percorrido desde o ponto de partida até o nó atual (n).

h(n) é o custo estimado (heurística) do nó atual (n) até o destino. No contexto de mapas, a heurística mais comum é a distância em linha reta, pois é a menor distância possível e nunca superestima o custo real.

Ao priorizar os nós com o menor valor de f(n), o A* explora de forma muito mais direcionada do que uma busca "cega", convergindo rapidamente para a melhor rota possível, considerando fatores como distância e tempo de tráfego (incorporados nos pesos das arestas do grafo).

Aplicação no Projeto: É o algoritmo principal para calcular a rota de entrega individual, garantindo a rota mais eficiente para cada pedido.

2. Busca em Largura (BFS - Breadth-First Search): A Base de Comparação
O BFS é implementado no projeto principalmente para fins de análise e validação, servindo como um ponto de referência para demonstrar a superioridade do A*.

O que é? O BFS é um algoritmo de busca que explora um grafo de maneira "camada por camada". A partir de um nó inicial, ele visita todos os seus vizinhos diretos, depois os vizinhos desses vizinhos, e assim por diante, expandindo-se uniformemente em todas as direções.

Como funciona? Ele utiliza uma estrutura de dados de fila (FIFO - First-In, First-Out) para manter o controle dos nós a serem visitados. Isso garante que ele encontre o caminho mais curto em termos de número de arestas, mas não necessariamente o caminho de menor custo total (pois ignora os pesos das arestas).

Aplicação no Projeto: Serve como um benchmark. Ao comparar o tempo de execução e os recursos computacionais gastos pelo BFS com os do A*, o projeto pode quantificar a eficiência ganha ao usar uma busca informada.

3. Busca em Profundidade (DFS - Depth-First Search): O Explorador Profundo
Assim como o BFS, o DFS é implementado para fins comparativos, ilustrando uma abordagem de busca diferente e, geralmente, inadequada para otimização de rotas.

O que é? O DFS é um algoritmo que explora o grafo seguindo um caminho o mais "profundo" possível. Ele avança por um ramo do grafo até não poder mais e, então, retrocede (faz o backtracking) para explorar o próximo ramo disponível.

Como funciona? Ele utiliza uma estrutura de dados de pilha (LIFO - Last-In, First-Out), seja de forma explícita ou implícita através de recursão. Essa abordagem faz com que ele se aprofunde rapidamente no grafo.

Aplicação no Projeto: É usado para comparar estratégias de busca. A natureza do DFS o torna inadequado para encontrar a rota mais curta, pois ele pode facilmente se perder em um caminho muito longo antes de explorar opções mais curtas. Sua inclusão serve para fins acadêmicos e para justificar a escolha de algoritmos mais sofisticados.

4. Algoritmo K-Means: O Agrupador Geográfico Inteligente
Para otimizar a logística quando há múltiplos pedidos simultâneos, o projeto utiliza o K-Means, um poderoso algoritmo de clusterização.

O que é? K-Means é um algoritmo de aprendizado de máquina não supervisionado que agrupa um conjunto de pontos de dados em K clusters (grupos) distintos. O critério para o agrupamento é a proximidade: pontos no mesmo cluster estão mais próximos entre si do que de pontos em outros clusters.

Como funciona? O algoritmo agrupa os endereços de entrega em K regiões geográficas. Por exemplo, se houver 3 entregadores disponíveis, o sistema pode usar o K-Means para dividir todos os pedidos pendentes em 3 clusters. Cada entregador é então designado para um cluster.

Aplicação no Projeto: O K-Means é fundamental para a otimização de múltiplas entregas. Em vez de enviar um entregador para um único ponto distante, o sistema o designa para uma "zona de entrega" (um cluster). Em seguida, o algoritmo A* é novamente utilizado para traçar a rota ótima que conecta todos os pontos de entrega dentro daquele cluster, criando um tour de entrega altamente eficiente. Isso minimiza drasticamente a distância total percorrida e otimiza o tempo de todos os entregadores.


Diagrama do grafo/modelo usado na solução

![unnamed](https://github.com/user-attachments/assets/98df8248-fb88-4356-b2f4-bd0d76691152)


Análise dos resultados, eficiência da solução, limitações encontradas e sugestões
de melhoria.


1. Análise dos Resultados Esperados
Assumindo a implementação bem-sucedida dos objetivos propostos, os resultados do projeto seriam altamente positivos e mensuráveis em diferentes frentes.

Validação da Escolha do Algoritmo: A comparação de desempenho demonstraria inequivocamente a superioridade do A* sobre o BFS e o DFS. Enquanto BFS e DFS explorariam um número muito maior de nós (caminhos) desnecessários, o A* convergiria para a rota ótima com uma redução drástica no tempo de computação e no uso de memória. O resultado seria um gráfico comparativo claro mostrando que o A* é a única opção viável para uma aplicação em tempo real.

Eficiência Logística com K-Means: A aplicação do K-Means resultaria na criação de clusters de entrega geograficamente coesos. Na prática, isso se traduziria em um administrador visualizando o mapa de pedidos e, com um clique, agrupando-os em zonas otimizadas. O resultado direto é a capacidade de atribuir múltiplas entregas a um único entregador de forma lógica, maximizando a eficiência de cada viagem.

Funcionalidade da API (Flask): O resultado seria uma API robusta e funcional, com endpoints claros (ex: /calcular-rota, /clusterizar-pedidos). A API seria capaz de receber coordenadas geográficas, processá-las através dos algoritmos e retornar a solução (uma sequência de coordenadas da rota ou a atribuição de pedidos a clusters) em um formato padrão como JSON, pronta para ser consumida por qualquer front-end (aplicativo móvel, painel web).

2. Eficiência da Solução
A eficiência do "Sabor Express" pode ser analisada sob duas óticas: computacional e operacional.

Eficiência Computacional: A escolha do A* é o pilar da eficiência computacional. Ao usar uma heurística para guiar a busca, ele evita a "explosão combinatória" de rotas possíveis que tornaria uma abordagem de força bruta (como o BFS em grafos com pesos) impraticável para mapas de cidades reais. A solução é rápida o suficiente para fornecer rotas em segundos, atendendo aos requisitos de uma operação de delivery dinâmica.

Eficiência Operacional (Impacto no Negócio): Esta é a consequência mais importante da eficiência computacional.

Redução de Tempo: Rotas otimizadas significam menos tempo no trânsito e chegada mais rápida ao cliente.

Economia de Custos: Menor distância percorrida se traduz diretamente em economia de combustível e menor desgaste dos veículos.

Aumento da Capacidade: Entregadores mais eficientes podem realizar um número maior de entregas por hora, aumentando a receita e a capacidade de atendimento do restaurante sem a necessidade de contratar mais pessoal.

Satisfação do Cliente: Entregas mais rápidas resultam em comida chegando mais quente e em uma melhor experiência para o cliente, fomentando a fidelidade.

3. Limitações Encontradas (e Potenciais)
Nenhuma solução é perfeita, e um projeto robusto deve reconhecer suas limitações.

Modelo de Grafo Estático e Trânsito: A principal limitação do modelo proposto é que os "custos" (pesos das arestas, ex: 5 min) são estáticos. O mundo real é dinâmico. O trânsito varia drasticamente dependendo do horário, dia da semana ou eventos inesperados. A solução atual não conseguiria, por exemplo, desviar de um congestionamento súbito.

O "Problema do Caixeiro Viajante" (PCV/TSP): Ao usar o K-Means para criar um cluster, o próximo desafio é encontrar a rota ótima que visita todos os pontos dentro daquele cluster. Este é um problema clássico e muito mais complexo (NP-difícil) do que encontrar o caminho entre dois pontos. A solução de simplesmente ir do ponto A ao B, depois do B ao C usando A* não garante a rota geral mais curta. A abordagem atual é uma boa heurística (aproximação), mas não é a solução matematicamente ótima para o tour.

Qualidade dos Dados Geográficos: A precisão do sistema depende inteiramente da qualidade dos dados de entrada. Endereços incorretos, erros de geocodificação (converter endereço em latitude/longitude) ou um mapa base impreciso levariam a rotas ineficientes ou incorretas.

Fatores Externos não Modelados: O sistema não considera variáveis operacionais cruciais, como:

O tempo de preparo de cada pedido no restaurante.

A capacidade do veículo do entregador (quantos pedidos ele pode carregar).

Janelas de tempo de entrega prometidas aos clientes.

4. Sugestões de Melhoria e Próximos Passos
As limitações identificadas abrem caminho para uma série de melhorias poderosas.

Integração com APIs em Tempo Real (Alta Prioridade): A melhoria mais impactante seria substituir os pesos estáticos do grafo por dados dinâmicos. Integrar a solução com a API do Google Maps Directions ou Waze permitiria que os custos das rotas fossem calculados com base no trânsito em tempo real, tornando o "Sabor Express" verdadeiramente inteligente e adaptativo.

Algoritmos de Roteamento de Veículos (VRP): Para resolver a limitação do "Caixeiro Viajante" de forma mais eficaz, o projeto poderia evoluir para usar algoritmos ou solvers específicos para o Problema de Roteamento de Veículos (VRP). Ferramentas como o Google OR-Tools são projetadas para otimizar rotas com múltiplos pontos, considerando restrições como capacidade e janelas de tempo.

Machine Learning para Previsão de Tempos: Um passo ainda mais avançado seria coletar dados históricos de entregas e usar Machine Learning para treinar um modelo que prevê o tempo de deslocamento. Esse modelo poderia considerar variáveis como hora do dia, dia da semana, clima e feriados, fornecendo estimativas de tempo ainda mais precisas do que as APIs públicas.

Inclusão de Restrições Operacionais: Evoluir a API para aceitar e processar restrições de negócio, como capacidade_maxima_entregador, tempo_preparo_pedido e janela_entrega_cliente. Isso tornaria o planejamento logístico muito mais completo e alinhado à realidade da operação.

Melhoria da Experiência do Usuário (UX):

Para o Cliente: Integrar um mapa de acompanhamento em tempo real.

Para o Entregador: Fornecer a rota otimizada diretamente em um aplicativo de navegação (Google Maps, Waze) através de deep linking.

Para o Administrador: Criar um dashboard com métricas de desempenho (tempo médio de entrega, distância percorrida por entregador, etc.).

