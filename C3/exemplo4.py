# Exemplo para explicar a pilha de chamadas (Call Stack) que o computador utiliza

# Função para saudar alguém
def sauda(nome):                            
    print("Olá, "+nome+"!")                 
    sauda2(nome)                            # 2 - O computador aloca espaço na pilha de chamadas para a nova função, armazenando o valor enviado(nome=Luís) e entrando no escopo dela para processá-la
    print("Preparando para dizer tchau...") # Para de armazenar a função sauda2 na pilha(utiliza o método pop) depois do seu término
    tchau()                                 # 3 - O computador aloca espaço na pilha de chamadas para a nova função 
# 4 - Ao terminar a função de tchau, o computador para de alocar espaço para ela(pop) e, por fim, termina de alocar espaço para sauda(), pois a função terminou sua execução.

# Função para continuar a saudação
def sauda2(nome):               # Recebe o nome da pessoa
    print("Como vai "+nome+"?")

# Função para se despedir
def tchau():                
    print("Ok, tchau!")        

sauda("Luís") # 1 - O computador atende a primeira função chamada(sauda) e armazena o valor do parâmetro enviado(nome=Luís)