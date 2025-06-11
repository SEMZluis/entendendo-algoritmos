def pesquisa_binaria(array, item):
    baixo = 0               # Primeira posição do array
    alto = len(array) - 1   # Última posição do array

    while baixo <= alto:             # Enquanto a posição mais baixa for diferente da mais alta:
        meio = int((baixo+alto)/2)   # Encontre a média das posições 
        chute = array[meio]          # E selecione o item que está na média das posições (ou seja, o meio entre a mais alta e a mais baixa)

        if chute < item:             # Se o item chutado for menor que o item pesquisado
            baixo = meio + 1         # Elimine os números/itens menores aumentando a posição mais baixa do array (que passará a ser a média anterior + uma posição)
        elif chute > item:           # Se o item chutado for maior que o item pesquisado
            alto = meio - 1          # Elimine os números/itens maiores diminuindo a posição mais alta do array (que passará a ser a média anterior - uma posição)
        else:                        # Se o item chutado for igual ao item pesquisado
            return meio              # Retorne a posição do item 

    return None

# Testes 

# 1 - Ordem númerica crescente e decrescente
l1 = [1, 3, 7, 9, 13]
print(pesquisa_binaria(l1, 9))
print(pesquisa_binaria(l1, 13))

l2 = [12, 10, 6, 4, 2]
print(pesquisa_binaria(l2, 6))
print(pesquisa_binaria(l2, 2)) # Nesse caso, ocorre um erro, pois os elementos da lista não estão ordenados conforme a ordem dos índices. 

# 2 - Ordem alfabética
la = ['A', 'B', 'C', 'D']
print(pesquisa_binaria(la, 'C'))
print(pesquisa_binaria(la, 'B'))