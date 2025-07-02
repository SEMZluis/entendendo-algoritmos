# Exemplo de como implementar grafos e de como usar a pesquisa em largura
# Contexto: encontrar um vendedor de manga a partir de vizinhos

from collections import deque # Importação da estrutura double ended queue (fila de dois finais)

def pessoa_e_vendedor(nome): # Função que verifica quem é um vendedor de manga
    return nome[-1] == 'm'   # Se o nome da pessoa terminar em m, retorna True. Se não, retorna False.

grafo = {}                                  # Inicialização da hash table
grafo["voce"] = ["alice", "bob", "claire"]  # Conexão dos vizinhos de 1º grau
grafo["alice"] = ["peggy"]                  # Conexão dos vizinhos de 2º grau
grafo["bob"] = ["anuj", "peggy"]            # Conexão dos vizinhos de 2º grau
grafo["claire"] = ["thom", "jonny"]         # Conexão dos vizinhos de 2º grau
grafo["peggy"] = []                         # Conexão dos vizinhos de 3º grau
grafo["anuj"] = []                          # Conexão dos vizinhos de 3º grau
grafo["thom"] = []                          # Conexão dos vizinhos de 3º grau
grafo["jonny"] = []                         # Conexão dos vizinhos de 3º grau

# Função que de fato realiza a pesquisa
def pesquisa(nome):
    fila = deque()       # Inicializa a fila
    fila += grafo[nome]  # Coloca os valores que existirem na hash table referentes ao nome pesquisado
    verificadas = []     # Inicializa o array para registrar as pessoas já verificadas

    # Enquanto houver nome na fila
    while fila:                        
        pessoa = fila.popleft() # Pessoa é igual ao primeiro nome que entrou na fila

        if not pessoa in verificadas: # Se a pessoa selecionada ainda não foi verificada
            
            if pessoa_e_vendedor(pessoa): # E se a pessoa selecionada for um vendedor de manga
                print(pessoa+" é um vendedor de manga!")
                return True # Fim da pesquisa
            else: # Mas se a pessoa selecionada não for
                fila += grafo[pessoa] # Adiciona os nomes dos vizinhos dela à hash table

    return False # Se não há vendedor de manga, a função retorna False.

pesquisa("voce")