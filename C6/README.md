# Problema do Caminho Mínimo
- É um problema que precisa do menor caminho ou do menor número de etapas possível para que algo seja realizado.
- Para resolver problemas desse tipo, basta:
    - Modelar o problema com grafos
    - Usar a pesquisa em largura na modelagem para encontrar a solução.

# Grafos
- Um modelo de grafos é um conjunto de conexões. 
- Cada grafo é constituído por vértices e arestas. 
- Um vértice, mediante arestas, pode ser conectado a outros vértices, que são chamados de vizinhos.
- Um grafo que tem setas direcionadas a ele mas não há nenhuma seta partindo dele é chamado de dígrafo.
- Também há grafos não direcionados, em que a relação acontece nos dois sentidos pois não há setas.

# Pesquisa em largura
- É um algoritmo que utiliza grafos e busca responder dois tipos de pergunta:
    - Existe algum caminho do vértice A até o vértice B?
    - Qual o caminho mínimo do vértice A até o vértice B?
- Para saber se há algum caminho entre os vértices, é necessário verificar as conexões que existem entre os vizinhos do vértice A. Se nenhum dos vizinhos do vértice A for o vértice B, então pesquisa-se nas conexões dos vizinhos do vértice A. Se o vértice B não for encontrado, significa que ele não foi modelado nessa rede de grafos. 
- Quando o vértice B é encontrado na pesquisa, o menor caminho também é encontrado. Afinal, primeiro pesquisa-se os vizinhos mais próximos do vértice A e depois *os vizinhos dos vizinhos* e assim por diante. Então, quando o vértice B for encontrado, considerando que todas as conexões mais próximas possíveis do vértice A já foram investigadas, o menor caminho também será.
- Considerando a possibilidade de haver pesquisas repetidas, também é necessário a existência de uma lista que registre os vértices que já foram verificados. Ou seja, se um vizinho de A não é o vértice B, ele é registrado nessa lista e retirado da sequência de pesquisa.
- Desse modo, para que a pesquisa funcione, é necessário que os vértices sejam pesquisados na ordem em que são adicionados na busca. Logo, é necessário utilizar uma estrutura de dados específica: a fila.

# Filas
- Filas funcionam como na vida real: o primeiro dado que entra numa fila é o primeiro dado que será atendido/retirado dela. 
- Não é possível acessar elementos aleatórios de uma fila, pois a ordem precisa ser seguida.
- É uma estrutura de dados FIFO (*First In, First Out*), ou seja, primeiro a entrar, primeiro a sair.

# Tempo de Execução
- O tempo de execução para encontrar um determinado vértice em todo o mapa de grafos é igual a quantidade de conexões que precisam ser verificadas. Desse modo, é um tempo de O(*quantidade de arestas*).
- O tempo de execução para adicionar todos os vértices verificados à lista é igual a O(*quantidade de vértices*) .
- Sendo assim, o tempo de execução da pesquisa em largura costuma ser descrito como O(*A+V*), A para o número de arestas e V para o número de vértices.

# Ordenação topológica
- É uma maneira de criar uma lista ordenada a partir de um grafo.
- Considerando que existem dependências entre os vértices do grafo, os vértices que são mais dependentes de outros aparecem no final da lista, pois precisam que primeiro os outros vértices sejam verificados para que eles sejam verificados também.
- Para melhor compreensão, basta imaginar o grafo nesse caso como uma lista de tarefas.

# Árvores
- É um tipo especial de grafo em que nenhuma aresta jamais aponta de volta.
- Em uma árvore genealógica, por exemplo, não tem como você descender da sua mãe e também ser pai ou mãe dela.
