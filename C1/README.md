# Pesquisa simples
- É o algoritmo mais estúpido para realizar pesquisas.
- Consiste em analisar cada elemento de uma lista por vez. Logo, a cada tentativa, apenas um elemento é eliminado.
- Para uma lista de *n* itens, a pesquisa simples precisa de *n* etapas/operações.
- A pesquisa simples tem um **tempo linear** de execução.

# Pesquisa binária  
- É um algoritmo para realizar pesquisas, sua entrada precisa ser uma lista **ordenada** de elementos.
- Se o elemento buscado está na lista, a pesquisa binária retorna a **posição** do elemento.
- Consiste em encontrar um **elemento intermediário** e eliminar metade da lista a cada vez.
- Para uma lista de *n* itens, a pesquisa binária precisa de log₂*n* etapas/operações.
- A pesquisa binária tem um **tempo logarítmico** de execução.

# Notação Big O
- Diz quão rápido é uma algoritmo e o quão rapidamente ele cresce/escala.
- Não fornece o tempo necessário para a execução do algoritmo em segundos, mas em **número de operações**. Sabendo quando tempo uma operação leva para ser realizada, é possível determinar o tempo necessário para a execução do algoritmo.
- A notação Big O considera sempre o **pior dos casos**. Para a *pesquisa simples*, ele é o O(*n*). Para a *pesquisa binária*, a pior das hipóteses é O(log₂*n*).
- A rapidez de um algoritmo é medida pelo aumento do número de etapas/operações que ele deve realizar para ser executado.
- Na vida real, não é ideal converter um tempo de execução na notação Big O em um número de operações. 

# Materiais Adicionais
https://www.youtube.com/watch?v=P3YID7liBug

