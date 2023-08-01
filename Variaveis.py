#Vamos aprender a manipular variaveis

idade = 26 #variavel (int)
altura = 1.55 # variavel (float)
nome = 'Nathalia Cristinne' #variavel (str)
medicina = True #variavel (bool)

"""
    Tipos de variáveis

    1. int: números inteiros, ou seja, números sem parte decimal: 0, 5, -, 1000
    2. float: números reias, ou seja, números com parte decimal: 1.0, -2.7, 3.14
    3. str(string): cadeias de caracteres, ou seja, dados textuais
    4. bool: valores lógicos (booleanos): True ou False
"""

#Vamos aprender a verificar os tipos das variaveis

print(type(idade))
print(type(altura))
print(type(nome))
print(type(medicina))


#Ja sabemos que (input) solicitamos alguma informação do usuario, agora vamos aprender a armazenar estas informações;

casamento = input('Em que data você pretende se casar com Nathalia Cristinne?')# variavel (casamento) recebe o (input);

#Agora que sabemos armazenar uma informação do usuario, vamos aprender a imprimir essas informações para o usuario;

print('Parabéns sua data de casamento esta marcada para,', casamento)# estamos imprimindo uma (str) junto a variavel (casamento);

