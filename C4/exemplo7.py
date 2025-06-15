# Exercício de DC/recursão: escrever uma função que conte o número de itens em uma lista
# Caso-base: um elemento na lista
# Caso recursivo: ir diminuindo a lista até sobrar um item

def conteTamanho(lista):
    if not lista:                   # Se não há elementos na lista
        return 0                    # Acabe a função e retorne 0 -> Caso-base
    else:                           # Se ainda há elementos na lista
        lista.pop()                 # Retire o último elemento
        return 1 + conteTamanho(lista)   # E retorne a quantidade de elementos retirados (1) + a quantidade de elementos que serão retirados com a lista decrescida -> Caso recursivo

#Testes
# print(conteTamanho([1, 2, 3]))
# print(conteTamanho(['A', 'B', 'C', 'D', 'E']))
# print(conteTamanho(['A', 'B', 'C', 'D', 1, 7]))

