# > Operações Matemáticos (Aritméticas)

"""
    - Soma: +
    - Subtração: -
    - Multiplicação: *
    - Divisão: /
    - Divisão inteira: //
    - Resto da divisão: %
    - Potêsncia: **

    todos esses são os simbolos para operações;
"""

numero1 = 20
numero2 = 30

print(numero1 + numero2) #Estamos realizando uma soma entre o numero 1 e 2
print(numero1 - numero2) #Estamos subtraindo o numero 1 e 2
print(numero1 / numero2) #Estamos realizando uma divisão
print(numero1 * numero2) #Estamos realizando uma contra de multiplicação
print(numero1 // numero2) #Estamos realizando uma operação de divisão de numeros inteiros
print(20 % 6) #Exemplo de operação de Resto da divisão
print(2 ** 3) #Exemplo de potencia na matematica então temos o numero 2 elevado ao cubo.


# Agora vamos trabalhar com operadores (Booleanos);

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2

print(idade1 > idade2)           #falso 'False', (idade 1 e maior que a idade 2?)
print(idade1 <= idade2)          #verdadeiro 'True', (idade 1 é menor ou igual a idade 2?)
print('Python' == 'python')      #falso 'False', (a string Python é igual a string python?)
print('banana' != 'abacaxi')     #verdadeiro 'True', (a string banana é diferente da string abacaxi?)
print(altura1 >= altura2)        #verdadeiro 'True', (altura 1 é maior ou igual que a altura 2?)
print(altura2 > altura3)         #falso 'False', (a altura 2 e maior que a altura 3?)


# Lembrando que todo operador (booleano) retorna somente verdadeiro ou falso, representando a linguagem binaria 0100111000, nomeados entre o numero 0 e 1