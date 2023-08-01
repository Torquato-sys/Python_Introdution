# ESTRUTURA FOR(LAÇO DE REPETIÇÃO)

"""
para variavel dentro de uma faixa (10), lembrando que essa faixa vai começar a partir do número 0 e ir até o numero menor que 10 ou seja
número 9;

for variavel in range(10): 
    print(variavel)
"""


"""
nesta parte temos o mesmo conceito so que no range() temos 2 numeros separado por uma virgula, sendo que o primeiro numero equivale o começo da contagem
e o segundo numero equivale ate o numero 10 que é menor que 11;

for variavel in range(1, 11):
    print(variavel)
"""


"""
nesta parte temos o mesmo conceito dos dois acima so que dentro do range() temos 3 numeros agora separado por virgula, sendo que o primeiro
numero equivale o ponto de inicio da contagem, o segundo numero equivale 10 porque ele e o ultimo numero antes do 11 declarado dentro do range()
e o terceiro numero equivale a de quantos em quantos numero iremos pular fazendo essa contagem neste caso estamos pulando de 2 em 2,
vai ser então começando do numero 1 ate o numero 11, ex: 1, 3, 5, 7, 9. Para a contagem no 9 porque o 11 não se conta somente o antecessor dele
que seria o numero 10;

for variavel in range(1, 11, 2):
    print(variavel)
"""




nota = 0 # variavel(nota) recebe valor 0

for N in range(1, 4): # para variavel(N) dentro de uma faixa, começando do numero 1 e parando no numero 3 que e menor que 4;

    notas = float(input(f'Digite sua nota aqui {N}: ')) # variavel(notas) recebe float(numero decimal) input(coleta da interação do usuario); 
    # para inserir uma variavel em uma string precisamos colocar (f) antes da string;
    nota = nota + notas # variavel(nota) recebe a soma de nota + a variavel(notas), entao ela inicia em 0 vai contando as notas inserida pelo professor;

print(nota / 3) # imprimir a variavel(nota) com o resultado da soma das 3 notas inseridas pelo professor e dividindo ela por 3, para obter a media;
