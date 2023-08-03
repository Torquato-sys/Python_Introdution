# > FUNÇÕES

# 1. O que são funções e por que utilizá-las?

# Funlçoes que ja utilizamos anteriormente...

print() # - Imprimi uma mensagem (int, float, str) no console (terminal, cmd);
input() # - Retorna um dado informado pelo usuário (entrada padrão), podendo ser armazenado os dados digitados pelo usuario em uma variavel;
len() # - Recebe uma lista e retorna o tamanho da mesma;
max() # - Retorna o maior valor da lista informada;

# 2- Criação de funções

# Função inicial

def saudacao():
    print('Seja bem-vindo!')
    print('E um prazer ter você aqui conosco!')

#saudacao()

# Função com parâmetros

# Esta parte do codigo esta solicitando um nome que no caso so podera ser atribuido pelo desenvolvedor ou dono da aplicação;
# Util somente quando você tem um contrato pronto e so quer atribuir o nome do seu cliente;
def saudacao(nome):
    print(f'Seja bem-vindo {nome}!')
    print('É um prazer ter voce aqui conosco!')

saudacao("Mateus")


# Função com parâmetros default

def saudacao(nome, curso='Python'): # ja estamos definindo por padrão que o parametro curso sempre ira retornar o valor 'Python';
    print(f'Seja bem vindo, {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Walisson') # agora quando eu chamar a função saudacao ele vai me retornar por padrão o nome 'Python' assim como foi informado la em cima;

# Funções com retorno

def soma(num1, num2):
    return num1 + num2
    print(soma) # lembrando que quando usado a função return não sera possivel declarar mais nada dentro def, portanto use sempre no final da operação;

resultado = soma(5, 7)
print('O resultado da soma é', resultado)


# Conceito calculadora
def calculadora(num1, num2, operacao='+'): # Estamos praticamente criando uma calculadora que dentro da variavel resultado, informamos os numeros e a operação que sera realizada;
    if operacao == '+': # Se operação for igual a +;
        return num1 + num2 # Retorne uma soma de adição;
    elif operacao == '-': # Se a operação for igual a -;
        return num1 - num2 # Retorne uma soma de subtração;

resultado = calculadora(10, 20, '-') # informando num1, num2, e a operação(+,-,*,/);

print(resultado) # Imprimir a variavel resultado;


# Já este codigo ele solicita que o usuario informe o nome dele e assim que feito ele retorna a mensagem de seja bem vindo seguido do nome informado pelo usuario;
# Bastante util para chat-bot pois ele coleta o nome do usuario e armazena em uma variavel, para retornar uma mensagem de saudacao;
nome = input('Digite seu nome: ')
curso = input('Digite o curso desejado: ')

def saudacao(nome, curso):
    print(f'Seja bem-vindo {nome}!')
    print(f'É um prazer ter você aqui conosco, vamos passar tudo sobre o curso de {curso}!')

saudacao(nome, curso)