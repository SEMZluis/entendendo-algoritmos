# Exemplo para explicar como as funções recursivas usam a pilha de chamadas

# Função para calcular o fatorial de um número
def fatorial(num):                   # Recebe um número
    if(num == 1):                    # Se o número for igual a 1
        return 1                     # Acaba a função retornando 1 -> Caso-base
    else:                            # Se o número for diferente de 1
        return num * fatorial(num-1) # O número enviado é multiplicado pelo retorno da própria função, a qual irá receber o número decrescido de 1. -> Caso recursivo
    
#Teste
print(fatorial(3))
# O algoritmo vai seguir essa ordem nesse caso:
# 1 - Pilha de chamadas armazena fatorial(3)
# Processando a função, percebe-se que 3 é diferente de 1. Logo, multiplica-se 3 com a chamada de função fatorial(3-1=2).
# 2 - A função fatorial(3) pausa sua execução. A pilha de chamadas armazena fatorial(2) e inicia sua execução.
# Processando a função, percebe-se que 2 é diferente de 1. Logo, multiplica-se 2 com a chamada de função fatorial(2-1=1).
# 3 - A função fatorial(2) pausa sua execução. A pilha de chamadas armazena fatorial(1) e inicia sua execução.
# Processando a função, percebe-se que o parâmetro recebido pela função é 1. Logo, a função fatorial(1) RETORNA 1.
# 4 - Quando a função fatorial(1) retorna o valor 1, a função é retirada da pilha de chamadas.
# 5 - A pilha de chamadas volta a executar a função fatorial(2), que multiplica 2x1 e RETORNA 2.
# 6 - Quando a função fatorial(2) retorna o valor 2, a função é retirada da pilha de chamadas.
# 7 - A pilha de chamadas volta a executar a função fatorial(3), que multiplica 3x2 e RETORNA 6.
# 8 - Quando a função fatorial(3) retorna o valor 6, a função é retirada da pilha de chamadas.