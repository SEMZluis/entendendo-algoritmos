# Dividir para conquistar (DC)
- É uma técnica recursiva que ajuda a pensar sobre um determinado problema. Ela é recursiva porque você fica dividindo o problema várias vezes até "conquistar" uma solução.
- Existem dois passos para aplicar essa estratégia:
    - Descubra o caso-base, que deve ser o caso mais simples possível (*Qual seria o caso mais fácil para solucionar esse tipo de problema?*).
    - Descubra como reduzir o problema para que ele se torne o caso-base (*Como reduzo/divido esse problema até chegar no caso mais fácil?*).
- Quando uma função recursiva envolver um *array* e a técnica DC está sendo utilizada, geralmente o caso-base da função será um *array* vazio ou um *array* com um elemento.

# Quicksort
- É um algoritmo de ordenação.
- Constitui-se por 3 elementos principais:
    - Um pivô, que será um número que servirá para comparações.
    - Um *subarray* para números maiores que o pivô.
    - Um *subarray* para números menores que o pivô.
- O *Quicksort* utiliza a estratégia DC, identificando o caso-base e o caso recursivo para funcionar.
    - O caso-base, ou o caso mais simples, é um *array* vazio ou com apenas um número, já que não precisam de ordenação.
    - O caso recursivo acontece quando você precisa ordenar os *subarrays* (**quicksort(menores) + pivô + quicksort(maiores)**).
- Para aplicar o *Quicksort*, deve-se realizar os seguintes passos:
    - Escolher um pivô da lista de números.
    - Particionar o *array* em dois *subarrays*, separando-os entre menores e maiores que o pivô.
    - Executar o *Quicksort* recursivamente em ambos os arrays.
- O desempenho do algoritmo depende bastante da escolha do pivô.
- Na pior situação, o algoritmo *Quicksort* tem tempo de execução O(*n*²). Um exemplo típico disso é quando o algoritmo sempre escolhe o primeiro elemento de um *array* como pivô e ele já está ordenado.
    - A cada chamada recursiva, apenas um elemento é separado (o pivô), e o resto do *array* continua sendo processado.
    - Isso gera *n* chamadas recurivas, uma para cada elemento.
    - Em cada chamada, o algoritmo ainda percorre o *array* restante para reorganizar os elementos, o que leva tempo O(*n*).
    - O algoritmo faz n chamadas de função, e cada uma percorre até n elementos → Tempo total: O(*n* × *n*) = O(*n*²).
- Na melhor situação, ou seja, no médio caso, o algoritmo *Quicksort* tem tempo de execução O(*n*log*n*). Um exemplo típico disso é quando o algoritmo sempre escolhe o elemento central de um *array* e ele já está ordenado.
    - A cada chamada recursiva, o *array* é dividido ao meio.
    - Isso gera cerca de log *n* níveis de chamadas recursivas (como acontece em uma pesquisa binária).
    - Em cada nível, o algoritmo percorre o *array* inteiro, reorganizando os elementos em torno dos pivôs, e isso leva tempo O(*n*).
    - log *n* níveis de chamadas, cada um com custo O(*n*) → Tempo total: O(*n* × log *n*).

![comparaqcsort](https://github.com/user-attachments/assets/c9fb66d7-22da-4d51-b7c8-23d6ac9f7ea4)


# Notação Big O revisada
- Quando escrevemos algo na notação Big O, estamos representando a seguinte expressão: *c * n*, em que *n* é o número de etapas necessárias para executar o algoritmo e *c* uma determinada quantidade de tempo que o algoritmo leva para ser executado.
- Desse modo, quando os algoritmos possuem tempos de execução diferentes, como a pesquisa binária (*log n*) e a pesquisa simples (*n*), por exemplo, a constante *c* é normalmente ignorada. (Exemplo: tente comparar os dois algoritmos citados usando os mesmos valores de *c* e *n* para ambos).
- No entanto, às vezes, a constante faz diferença. Por exemplo, o *Quicksort* tem uma constante menor que o *Merge sort*, e como ambos possuem o mesmo tempo de execução O(*n log n*) no caso médio do *Quicksort*, o *Quicksort* acaba sendo mais rápido. Além do mais, o *Quicksort* funciona mais vezes no caso médio do que no pior dos casos.
