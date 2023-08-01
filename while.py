numero_sorteado = 15 # numero ganhador do sorteio;

numero_escolhido = int(input('Informe um número entre 1 e 20:')) # entrada de números dos candidatos;


# Este exemplo e sem o laço de repetção, solicitando apenas uma vez do usuario se ele errar;

"""if numero_sorteado == 15:
    print('Parabéns! você acertou.')
else:
    print('Não foi desta vez, vamos tentar novamente...')"""


while numero_escolhido != numero_sorteado: # Utilizando laço de repetição, para se caso o usuario digitar o numero diferente do que queremos repetir a ação;
    print("Você errou, tente novamente...") # Imprimir o tente novamente;

    numero_escolhido = int(input('Informe um número entre 1 e 20:')) # Requisição para o usuario digitar um número novamente;

print('Parabéns! Você acertou. ;)') # Se caso o numero que o usuario digitar for == a 15, ele me trara esta mensagem; 


# Informe dados do candidato;

# Dados para o dono do sorteio entrar em contato posteriormente;
nome = input('Digite seu nome completo: ')
email = input('Digite seu email: ')
telefone = input('Digite seu telefone: ')

print('Enviaremos um email com mais informações sobre o seu produto, aguarde!') # Menssagem para o usuario, entender que em breve ira obter retorno;