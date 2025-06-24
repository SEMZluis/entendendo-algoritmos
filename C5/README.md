# Funções hash
- Uma função *hash* é uma função na qual uma *string* é inserida e um número é retornado.
- Para existir um padrão indicando qual número deve ser retornado após a inserção de uma *string*, a função *hash* precisa seguir alguns requisitos:
    - Todas as vezes que determinada *string* for inserida, a função deverá retornar o mesmo número que sempre se refere àquela *string*.
    - Cada palavra diferente deve ser mapeada e ligada a um número diferente.

# Tabelas hash
- Uma tabela *hash* é um *array* + funções *hash*. Ou seja, o *array* vai armazenar determinados valores que estão relacionados a determinadas *strings*, enquanto que a função *hash* vai relacionar os valores e nomes ao conectar as *strings* com as posições do *array*.
- Com isso, pesquisas podem ser feitas com o tempo de execução O(1), já que a função *hash* elimina a fase de procura/leitura de valores.
- A primeira execução da função *hash* serve para ela identificar onde guardar o valor que se refere a determinado nome.
- A função *hash* tem noção do tamanho do *array*. Se o *array* tem um limite de 5 itens, ela irá retornar apenas números dentro desse limite.
- Uma tabela *hash* contém chaves e valores, também podendo ser chamada, então, de dicionário.
- No geral, as tabelas *hash* são ótimas para modelar relações entre dois itens, filtrar por duplicatas e para *caching* de dados.

# Colisões
- Colisões acontecem em uma tabela *hash* quando duas chaves são indicadas para o mesmo espaço no *array*. Ou seja, elas não são iguais entre si, mas, por alguma lógica, elas deveriam ocupar o mesmo espaço no *array* ao qual a função *hash* vai se referir.
- Uma solução para as colisões é colocar uma lista encadeada no espaço referido do *array*. Então, será possível alocar o valor das duas chaves naquele espaço. O problema disso é que uma pesquisa em uma lista encadeada pode ser muito lenta quando ela é muito grande.
- Desse modo, quando uma colisão acontece, a tabela *hash* realiza todas as suas operações (busca, inserção e remoção) no pior caso, O(*n*). Enquanto que, normalmente, ela opera em tempo constante e costuma ser chamada de "melhor dos dois mundos" quando comparada à *arrays* e listas.
- Para evitar colisões, são necessários um baixo fator de carga e uma boa função *hash*.

## Fator de Carga
- Fator de Carga = Número de itens na tabela / Número total de espaços
- Um baixo fator de carga significa que há poucos itens na tabela e muitos espaços sobrando no *array*.
- Um alto fator de carga significa que há muitos itens na tabela e poucos espaços sobrando no *array*.
- Para que não ocorra sobrecarga, é necessário redimensionar o *array* quando o fator de carga começa a crescer, aumentando a quantidade de espaços sobrando.
- **Redimensionamento**: primeiro, dobra-se o tamanho do *array* original. Depois, todos os itens são reinseridos na nova tabela *hash* usando a função *hash*. Uma boa prática é que esse processo ocorra quando o fator de carga for maior que 0,7.
- Com um fator de carga baixo, haverá menos colisões e a tabela terá melhor desempenho.
- O redimensionamento é caro e não deve ser feito com muita frequência. Porém, apesar disso, as tabelas *hash* ainda assim funcionam mais no médio caso, ou seja, no tempo constante O(1).

## Uma boa função *hash*
- Uma boa função *hash* distribui os valores pelo *array* de forma simétrica.
- Uma função *hash* ruim agrega valores e causa várias colisões.
- Sendo assim, no pior caso, a função *hash* mapeia todos os itens para o mesmo espaço da tabela *hash*, sobrando uma grande lista encadeada e denotando uma péssima distribuição.