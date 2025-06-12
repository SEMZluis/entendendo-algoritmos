# Como funciona a memória
- A memória é como um grande mapa de casas. Cada casa é um *slot* na memória, um espaço reservado para guardar informações. Cada *slot* possui um endereço, para que seja possível se referenciar às informações guardadas. 

# Array
- É uma estrutura para armazenar dados que consiste em uma listas de elementos que são armazenados sequencialmente na memória (um do lado do outro). É uma estrutura estática, ou seja, é necessário fixar o número de elementos que serão armazenados no total.
    - Desvantagens:
        - Se todos os espaços reservados para o *array* não forem utilizados, a memória será desperdiçada.
        - Se precisar aumentar ou diminuir o tamanho do *array*, todos os itens precisarão ser movidos, o que implica em um custo computacional.
        - O tempo de execução para realizar uma inserção ou uma deleção em um array na notação Big O é O(*n*).
        - Todos os elementos do array devem ser de mesmo tipo.
    - Vantagens:
        - São boas para realizar pesquisas, pois possuem um índice (afinal, todos os elementos estão listados em uma sequência na memória).
        - O tempo de execução para realizar uma leitura na notação Big O é O(1).
        - Podem lidar tanto com o acesso sequencial quanto com o acesso aleatório (localizar um item no meio da lista, por exemplo).

# Lista encadeada
- É uma estrutura para armazenar dados na qual consiste em uma lista de elementos que são armazenados em diferentes espaços de memória, porém, cada elemento guarda a referência de memória, - um ponteiro para o endereço -, do elemento que foi adicionado depois dele próprio. É uma estrutura dinâmica, ou seja, contanto que exista espaço na memória, novos elementos podem ser alocados.
    - Desvantagens:
        - Não são boas para pesquisa, tendo em vista que os elementos não possuem índice (é necessário ir verificando o endereço de cada um dos elementos até chegar no elemento desejado).
        - O tempo de execução para realizar uma leitura na notação Big O é O(*n*).
        - Só podem lidar com o acesso sequencial.
    - Vantagens:
        - Não há desperdício de memória.
        - Os itens armazenados nunca vão precisar ser movidos de lugar, pois precisam somente mudar para onde direcionam seus ponteiros quando há modificações na lista.
        - São boas para inserções e remoções de elementos da lista.
        - O tempo de execução para realizar uma inserção ou deleção na notação Big O é O(1).

# Ordenação por seleção
- Na ordenação por seleção, você ordena uma lista de elementos selecionando por vez qual deve seguir o outro.
- Em uma lista de números que precisa ser ordenada de maneira crescente, por exemplo, você precisa verificar o menor número que existe em uma lista e removê-lo para outra lista. Cada operação de leitura tem um tempo de execução linear de O(*n*). Desse modo, como você precisa verificar essa lista *n* vezes, então o tempo de execução para a ordenação será de O(*n*²).
- O livro explica que, a cada verificação, o número de elementos da lista anterior decai e, desse modo, o tempo de execução será diferente. Porém, existem condições para a notação BigO, as quais serão explicadas no capítulo 4, que resumem esse tempo de verificação em O(*n*²).
- Em resumo, a ordenação por seleção é um algoritmo bom, mas não muito rápido.