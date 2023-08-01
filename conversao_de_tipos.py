# CONVERSAO DE TIPOS

#exemplo
#numero inteiro declarado como String (SRT)
#Lembrando que havera erro ao tentar fazer uma operação com um numero 'int' e com numero 'str'
idade = '26'
numero1 = '10'
numero2 = '20'

print(numero1 + numero2) 
"""
Desta forma recebemos um valor de contatenação juntando os dois valores,
entao o que era pra ser uma soma de 10 + 20 ira juntar 10 com 20 ficando assim 1020 inteiro no final da operação;

"""

idade = '26'

print(idade, type(idade)) #agora vamos imprimir a variavel (idade) e verificar o tipo desta variavel;



idade_inteira = int('27') #Lembrando que a conversao deve ser na variavel, para que o print possa fazer seu papel de imprimir;

print(idade_inteira, type(idade_inteira)) #imprimindo a variavel( idade_inteira ) e o tipo dela;



"""
str(), converte qualquer tipo de variavel para string(texto);
int(), converte qualquer tipo de variavel para inteiro(numero inteiro);
float(), converte qualquer tipo de variavel para decimal(numeros decimais);
bool(), converte qualquer tipo de variavel para booleano(True or False); 
"""


meu_amor = input(' quantos % você ama a nathalia? ') 
#aqui estamos solicitando um valor inteiro, consequentemente o (input) lê o valor digitado pelo usuario em (STR), então precisamos que o valor da mesma seja convertido em (Int);
  
print(meu_amor, type(meu_amor))
#aqui estamos imprimindo a variavel (meu_amor) e pedindo o tipo da mesma;



meu_amor2 = int( input(' quantos % você ama a nathalia? ') ) #adicionamos int() para converter o valor que o input() coletar para type(inteiro);

print(meu_amor2, type(meu_amor2)) #vamos imprimir a variavel(meu_amor2) e coletar o seu tipo;






#Praticando...
idade_inteira2 = int('28')

print( idade_inteira2, type(idade_inteira2) )