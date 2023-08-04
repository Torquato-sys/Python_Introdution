# > DICIONÁRIOS

# Criando dicionários;

dicionario = {} # Lista vazia abrindo chaves;
dicionario = dict() # Lista vazia usando o dict()

dicionario = { 'nome': 'Mateus', 'idade': 23, 'altura': 1.65 } # Abrimos uma lista com valores dentro dela lembrando que o sempre vamos usar um campo para definir, ex: 'preferred language': 'Python', então sempre vamos atribuir nesta ordem funciona quase como uma variavel um esta sempre recebendo o outro;

print(dicionario) # imprimir todo o nosso dicionario sem exceção;
print(dicionario['idade']) # estamos solicitando para imprimir somente a chave 'idade';


# Adicionando elementos em um dicionario;

dicionario['programador'] = True # estamos adicionando a chave programador recebe True para o nosso dicionario existente, util para adicionar itens;

print(dicionario)

dicionario['altura'] = 2 # neste caso testamos adicionar um valor no dicionario, lembrando que a chave altura ja existe com um valor predefinido por nos, então foi entregue a conclusão que ao adicionarmos esta outra chave com outro valor diferente sera adicionado outro valor por cima então sera substituido do original;

print(dicionario)

# Interando sobre um dicionário

for chave in dicionario: # estamos percorrendo as chaves com esse comando pois e o padrão percorrer as chaves;
    print(chave)

for chave in dicionario: 
    print(chave, dicionario[chave]) # neste caso vamos receber a chave e seu valor, estamos percorrendo as chaves do dicionario e o que contem nelas;


# Testando a existência de uma chave

print('altura' in dicionario) # neste caso estamos solicitando uma confirmação, se contem uma chave com o nome 'altura' como sabemos que tem ele vai retornar 'True';
print('peso' in dicionario) # o mesmo caso mas com uma chave que não existe em nosso dicionario então vamos obter o valor 'False';