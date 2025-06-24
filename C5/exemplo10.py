# Exemplo de votação para explicar entradas duplicadas em tabelas hash

votaram = {}

def verifica_eleitor(nome):
    if votaram.get(nome):       # Função que procura na tabela hash o valor que está associado a string passada
        print("Já votou!")
    else:                   
        votaram[nome] = True    # Se o nome ainda não está inserido na tabela e associado a um valor, essa linha faz isso.
        print("Deixe votar!")

verifica_eleitor("Tom")
verifica_eleitor("Tom")