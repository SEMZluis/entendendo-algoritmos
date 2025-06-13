# Recursão
- É quando uma função chama a si mesma.
- Não há nenhum benefício de desempenho usar recursão, ela só torna a resposta de um problema mais clara.
- É fácil escrever uma função que usa recursão erroneamente e entra num loop infinito (vide exemplo3.py). Por isso, a função deve informar quando a recursão deve parar. Logo, a função deve ser dividida em duas partes:
    - *Caso recursivo*: é o momento da função em que ela chama a si própria.
    - *Caso-base*: é o momento da função em que ela não chama a si mesmo novamente, evitando o loop de se tornar infinito.

# Stack (Pilha)
- A pilha é uma estrutura de dados simples: os dados são inseridos no topo da pilha e são retirados/lidos a partir do topo também. Visualmente, é como uma estrutura vertical.
- Para inserir dados é utilizado o método *push* e para remover dados é utilizado o método *pop*.
- O computador utiliza uma pilha para controlar o funcionamento de funções, ela é chamada de *Call Stack* (Pilha de chamada).
- A *Call Stack* é um espaço da memória que salva as variáveis utilizadas quando uma função é chamada. Quando uma nova função é chamada a partir de outra, a pilha também guarda os dados dessa nova função, só que em uma camada "acima". Enquanto isso, a chamada de função inicial fica pausada até que a nova função chamada termine o seu processamento. Em resumo, a pilha de chamada guarda as variáveis de múltiplas funções e para de guardá-las conforme a ordem que as funções foram chamadas.

# Recursividade + Pilha de Chamada
- Quando uma função recursiva chama a si própria, ela está criando uma nova chamada de função. Desse modo, a pilha irá armazenar e tratar tanto das variáveis da função original chamada quanto da função filha que foi chamada. Numa função recursiva que calcula o fatorial de números, por exemplo(5), se você passa como parâmetro o número 3, a pilha vai armazenar 3 chamadas que vão ter diferentes valores para suas variáveis e vão terminar sua execução quando cada uma der seu retorno para a outra.
- Desse modo, muita informação precisa ser alocada na memória quando a recursividade é utilizada, o que pode tornar a pilha muito grande e ocupar muita memória por consequência.

