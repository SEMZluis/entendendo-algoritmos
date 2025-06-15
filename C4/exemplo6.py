# Função não recursiva
def soma(lista):
    total = 0        
    for x in lista:
        total += x
    return total

# Exercício de DC/recursão: Transforme a primeira função em uma função recursiva 
def somaRecursiva(lista):
    if not lista:                      # Se a lista está vazia
        return 0                       # Acaba a função retornando 0 para a soma total -> Caso-base
    num = lista.pop()                  # Adquire o último item da lista e remove-o
    return num + somaRecursiva(lista)  # Soma o último número da lista ao resultado da própria função quando chamada com a lista decrescida -> Caso recursivo

# Teste
print(somaRecursiva([2, 4, 6]))