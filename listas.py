# > Listas


# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2
"""
Nesta parte do codigo estamos voltando ao ponta pe inicial, como aprendemos no começo,
criando uma lista declarando 3 variaveis diferente (nota1, nota2, nota3)
com valores separado, pensa em uma situação em que agilidade e produtividade manda
não acha que valores separados não sera pessimo para a agilidade e produtividade?
"""

# Com lista
notas = [7.9, 9.7, 8.2]
"""
Nesta parte ja estamos com o codigo reduzido com os mesmo numero que o metodo anterior
mas notamos que agora so contém uma variavel, então para criar uma lista precisamos declarar
a varivel e abrir um colchetes informar os valores e separar todos por virgula seguido do espaço;
"""



# Criando Listas
lista = [] # lista tradicional, declarando variavel para receber valores abrindo colchetes para informar os valores da lista;
lista = list() # função list() e muito importante, pois ela tem o poder de criar ou converter valores em listas;
lista = [23, 'Mateus', 2.55, True] # Aqui estamos apresentando que uma lista pode receber todo tipo de valor, int(), str(), float(), bool();
lista_de_listas = [ 1, 2, [3, 4]] # neste caso temos uma lista dentro de outra lista;



# Indexação e Slices (fatiamento)

lista = [20, 'Nath', 1.59, True] # Lista com elementos dentro da mesma;

# Todos esses prints são para consutar elementos separados da nossa lista;
print(lista[0]) # Ponto importante que toda lista ela se inicia pelo numero 0 ou seja o primerio elemento da lista podera ser chamado informando o numero 0;
print(lista[1])
print(lista[2])
print(lista[3]) # Como o total de itens na lista e quatro começamos a contar do numero zero então teremos que acabar no número três para totalizar 4 itens;
#print(lista[4]); lembrando que se passarmos da quantidade de itens da lista, o interpretador ira nos retornar erro, informando que o item não existe;

print(lista[-1]) # ponto extremamente inportante: para puxar o ultimo item da lista teremos que trabalhar com numeros negativos, assim para o ultimo numero usamos -1 penultimo -2


# Slices

lista = [10, 20, 30, 40, 50, 60, 70] # Variavel (lista) recebendo uma lista[];

print( lista[0:3]) 
"""
Vamos anotar este ponto importante estamos imprimindo a lista acima so que de uma forma mais automatizada pois agora temos somente 1 print()
lembrando que o simbolo ' : ' ele e utilizado para realizar uma ação de continuidade ou seja neste print ira chamar do 0 ao 3,
lembrando tambem que não ira puxar 4 numero pois se resume a menor que 3 ou seja sera impresso o item 0, 1, 2 o três não sera considerado;
"""

print( lista[0:6:2]) # estamos informando que queremos os itens do 0 a 6 pulando de 2 em 2 itens;

# > Iterações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)
# Lembrando que da mesma forma que fizemos com range() iremos fazer agora utilizando o for, so que desta vez a lista ja tem uma variavel;


# 2. Utilizando os indices

print('Comprimento da lista:', len(lista)) # Este codigo len(), serve para verificarmos o tamanho da lista informada;

for i in range(len(lista)):
    print(i) #Nesta parte vamos imprimir a variavel 'i'  que esta recebendo o comprimento da lista e exibindo de forma continua graças ao range();
# lembrando que sera exibido os indices do array da lista = []
    
    
    print(lista[i])#Vamos imprimir a lista na posição 'i'
# Agora será impresso todos os itens da nossa lista pelos indices;
