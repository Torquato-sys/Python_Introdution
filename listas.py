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



# > Metodos de listas

lista = [1, 5, 6, 8, 95, 45]

print(lista) # Estamos imprimindo a lista inteira sem separação;


# append
lista.append(3) # estamos informando que vamos adicionar um numero a talbela so que ele ira para o final da tabela;

print('Depois do append:', lista)


# inset
lista.insert(1, 3) # estamos adicionando um objeto na lista, neste caso o primeiro numero informado significa o local aonde vai ficar o objeto, depois o segundo item que vem seprado por virgula sera indexada na posição que pedimos, neste calo ele ira adicionar o numero 3 na posição 1 da tabela;

print('Depois do insert:', lista)


# extend
lista1 = [35, 37, 40, 45, 35]
lista2 = [49, 53, 56]

lista1.extend(lista2) # comando extend fara a junção das listas neste caso a lista1() ira receber a lista2(), tudo que for da lista2 ira para o final da lista1(), isso fara junção das duas tabelas;

print('Depois do extend: ', lista1)

#pop (remover elemento);
lista.pop() #veja que não foi informado um valor neste caso sera removido automaticamente o ultimo item da lista;

print('Lista após o pop:', lista)

lista.pop(2)# neste caso eu estou definindo o local a qual quero remover o objeto da lista, informando o valor do array como 2 então ira eliminar o 3° ojeto da lista;

print('Lista após o pop:', lista)

# remove
lista1.remove(35) # neste caso ele e mais especifico que o .pop() pois ele elimina pelo nome do objeto, podendo informar um int(), str(), float(), bool(), lembrando que o mesmo ira eliminar o primeiro que encontrar, então se você que eliminar o nome Mateus da lista e contem 2 Mateus recomendo usar o pop se caso quiser eliminar o segundo Mateus;

print('Depois do remove:', lista1)

# count

print('Quantidade de 35 na lista:', lista1.count(35)) #neste caso vamos contar quantas vezes o int 35 aparece na lista, como sabemos ele vai retornar o valor 2 pois contem 2 numeros 35;

# index

print('Índice do elemento 40:', lista1.index(40)) # aqui ele vai nos informar o indice do objeto a qual buscarmos sendo ele, int, str, float ou bool.

# exemplo: lista = [10, 20, 30], usando o .index(20) ele vai nos voltar o valor 1 pois e a posição exata do indice 20, ja que iniciamos com o numero 0;

#sort

lista.sort() # neste caso sem informar nenhum parametro vamos receber a lista organizada de forma crescente;
print(lista)

lista.sort(reverse=True) # ja neste caso usando o reverse=True, estamos pedindo para a listar ser exibida de maneira decrescente;
print(lista)

# FUNÇÕES PARA LISTAS

# len
print(len(lista))
# usada para saber quantos elementos contém em nossa lista;

#sum
print(sum(lista))
# usada para somar todos os elementos da nossa lista;

#max
print('Maior elemento da Lista:', max(lista))
# como o proprio nome sugere estamos pedindo o maior elemento desta lista ou seja o maior valor dela;

#min
print('Menor elemento da Lista:', min(lista))
# como o proprio nome sugere estamos pedindo o menor elemento da nossa lista;
