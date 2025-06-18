# Exemplo que explica o algoritmo quicksort

def quicksort(array):
    if len(array) < 2:                 # Se o array for vazio ou tiver somente um número
        return array                   # Retorne o array -> Caso-base
    else:                              # Se o array tiver mais de dois números:
        pivo = array.pop()             # Encontre um número pivô, o qual servirá de comparação. Neste caso, utiliza-se o último número da lista.
        menores, maiores = [], []      # Declare os subarrays para guardar os números maiores e menores que o pivô

        for num in array:                                               # Para cada número que exister no array ou subarray:
            menores.append(num) if num <= pivo else maiores.append(num) # Compara os números com o pivô e particiona em subarrays.
        
        return quicksort(menores) + [pivo] + quicksort(maiores) # Retorna a chamada de função para ordenar os números menores, juntando o seu retorno com o pivô e com a chamada de função para ordenar os números maiores -> Caso recursivo

#Testes
print(quicksort([1, 3, 2]))
print(quicksort([2,4,3,6,2]))

print("-------------------")

# Esse exemplo do quicksort serve para comparar a quantidade de etapas necessárias para ter um array ordenado considerando a escolha do pivô

def quicksortTeste(array, centro):
    if len(array) < 2:                 
        return array                   
    else:
        pivo = array.pop(int(len(array)/2) if centro == True else 0) 
        print(f"pivo da vez:{pivo}")
        menores, maiores = [], []      

        for num in array:                                               
            menores.append(num) if num <= pivo else maiores.append(num)
        
        return quicksortTeste(menores, centro) + [pivo] + quicksortTeste(maiores, centro) 
    
# Testes
print(quicksortTeste([1, 2, 3, 4, 5, 6], True))
print(quicksortTeste([1, 2, 3, 4, 5, 6], False))
print(quicksortTeste([1, 2, 3, 4, 5, 6, 7], False))
# Com arrays ordenados e a escolha central sendo feita, percebe-se que o número de chamadas na pilha diminuí, o que diminui também o tempo de execução do algoritmo.
