# Exercício de DC/recursão: escrever uma função para encontrar o valor mais alto em uma lista
# Caso-base: Comparando somente 2 elementos em uma lista, consigo saber qual o maior
# Caso recursivo: Ir diminuindo o tamanho da lista até sobrar o maior valor

def maiorValor(lista):
    n1 = n2 = maior = 0             # Declara as variáveis, tanto as de comparação quanto a que guardará o maior valor

    if len(lista) >= 2:             # Se a lista possui mais de 2 números:
        n1 = lista[0]               # Guarde o valor do primeiro número
        n2 = lista[1]               # Guarde o valor do segundo número

        # Se o n1 for maior ou igual ao n2, retire o n2 da lista.
        # Se o n2 for maior ou igual ao n1, retire o n1 da lista.
        lista.pop(1) if n1 >= n2 else lista.pop(0)            

        maior = maiorValor(lista)   # Chame a função comparando dois números da lista que foi decrescida até que ela retorne o maior valor -> Caso recursivo
        return maior                # Retorne o maior valor encontrado
    else:                           # Se a lista chegar a possuir somente 1 número: 
        return lista.pop()          # Retorne o último número, que deve ser o maior -> Caso-base
    

print(maiorValor([1,5,3,4,5]))
# O algoritmo vai seguir essa ordem nesse caso:
# 1 - Pilha de chamadas armazena n1 = 1, n2 = 5 e compara ambos.
# 2 - 1 é retirado da lista. Lista agora é armazenada como [5, 3, 4, 5].
# 3 - A variável maior recebe o retorno da chamada de função maiorValor([5,3,4,5])
# 4 - Pilha de chamadas armazena n1 = 5, n2 = 3 e compara ambos.
# 5 - 3 é retirado da lista. Lista nessa função é armazenada como [5, 4, 5].
# 6 - A variável maior recebe o retorno da chamada de função maiorValor([5,4,5]).
# 7 - Pilha de chamadas armazena n1 = 5, n2 = 4 e compara ambos.
# 8 - 4 é retirado da lista. Lista nessa função é armazenada como [5,5].
# 9 - A variável maior recebe o retorno da chamada de função maiorValor([5,5]).
# 10 - Pilha de chamadas armazena n1 = 5, n2 = 5 e compara ambos.
# 11 - Um dos 5 é retirado da lista. Lista nessa função é armazenada como [5].
# 12 - A variável maior recebe o retorno da chamada de função maiorValor([5]).
# 13 - Como a lista tem o tamanho (len) igual a 1, a função maiorValor([5]) retorna o inteiro 5.
# 14 - Com o retorno de maiorValor([5]), a função maiorValor([5, 5]) também retorna 5.
# 15 - Com o retorno de maiorValor([5, 5]), a função maiorValor([5, 4, 5]) também retorna 5.
# 16 - Com o retorno de maiorValor([5, 4, 5]), a função maiorValor([5, 3, 4, 5]) também retorna 5.
# 17 - Com o retorno de maiorValor([5, 3, 4, 5]), a função maiorValor([1, 5, 3, 4, 5]) retorna, por fim, 5.