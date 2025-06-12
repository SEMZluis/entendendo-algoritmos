# Odenação por seleção: ordenar uma array do maior para o menor

# Função para encontrar o índice do menor elemento do array
def buscaMenor(array): 
    menor = array[0]                # Declara a varíaval para guardar o menor elemento do array, começando pelo 1º.
    menor_indice = 0                # Declara a varíavel para guardar o menor índice do array, começando pelo 1º.
    for i in range(1, len(array)):  # Para cada elemento que existir no array:
        if array[i] < menor:        # Se o elemento do índice "i" do array for menor do que o valor da varíavel "menor"
            menor = array[i]        # A variável "menor" passa a guardar o novo menor valor do array
            menor_indice = i        # E a variável "menor_indice" passa a guardar o índice referente a esse novo menor valor
    return menor_indice             # Depois de percorrer todos os itens do array, O(n), a função retorna o índice encontrado.

# Função para realizar a ordenação por seleção
def ordenacaoporSelecao(array):
    novoArray = []                          # Declara a variável para guardar o array ordenado
    for i in range(len(array)):             # Para cada elemento que exsitir no array:
        menor = buscaMenor(array)           # Procure o menor elemento que existir no array naquele momento
        novoArray.append(array.pop(menor))  # Adicione o menor elemento encontrado no novo array e retire-o do array antigo 
    return novoArray                        # Depois de percorrer todos os itens do array n vezes, O(n^2), a função retorna o array ordenado.

# Testes
print(ordenacaoporSelecao([5, 3, 6, 2, 10]))