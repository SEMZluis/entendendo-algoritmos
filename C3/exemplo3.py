# Exemplo para explicar recursão

# Função recursiva errada (sem caso-base)
def regressiva_infinita(i):  # Recebe um número aleatório como parâmetro
    print(i)                 # Imprime o número enviado
    regressiva_infinita(i-1) # Descresce o número enviado e entra na função de novo
# É um loop infinito porque, obviamente, existem infinitos números. Desse modo, a função sempre irá chamar ela própria.

# Função recursiva corrigida (com caso-base)
def regressiva_correta(i):   # Recebe um número aleatório como parâmetro
    print(i)                 # Imprime o número enviado
    if i <= 1:               # Se o número for menor do que 1 
        return               # Acabe o programa -> Caso-base
    regressiva_correta(i-1)  # Enquanto o número for maior do que 1, continue descrescendo-o. -> Caso Recursivo
# Dessa forma, existe uma condição limitando o loop da função, tornando a recursão útil.

