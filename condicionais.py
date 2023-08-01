# > ESTRUTURAS CONDICIONAIS

# vamos verificar uma estrutura basica de if e else (se ou senão);

idade = 14

if idade >= 18: #aqui estamos perguntando se a variavel(idade) e maior ou igual a 18(idade inicial para maior idade);
    print('Você e maior de idade parabéns, pode prosseguir!')
else:
    print('Você não e maior de idade, volte depois dos 18!')

"""
    Imagina que você queira imprimir "Aprovada(o)", caso o estudante tenha uma média
    superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""
#Aqui estamos utilizando um sistemas de notas manuais, com base nas variaveis(nota_aluno1), (nota_aluno2), (nota_aluno3);
nota_aluno1 = 5
nota_aluno2 = 7
nota_aluno3 = 9

#basicamente estamos perguntando, se a nota deste aluno for maior ou igual a 7 ele estara aprovado;
if nota_aluno1 >= 7:
    print('Aprovado')
#e se a nota do mesmo aluno for inferior a 7, ele sera reprovado;
else:
    print('Reprovado')

if nota_aluno2 >= 7:
    print('Aprovado')
else:
    print('Reprovado')

if nota_aluno3 >= 7:
    print('Aprovado')
else:
    print('Reprovado')


#Nesta parte ja temos uma forma diferente, pois estamos pedindo para o professor digitar a nota do aluno para armazenar na variavel(media);
media = float( input('Informe a média do aluno:') )#Variavel recebendo float(), para numeros decimais;

#se a media que o professor digitar for maior ou igual a 7, o aluno sera aprovado;
if media >=7:
    print('Aprovado')
    print('Parabéns!')
#mas se for inferior a 7 ele sera reprovado;
else:
    print('Reprovado')
    print('Tente novamente! :(')



#Agora temos uma forma diferente de pensar, pois temos a presenca do aluno, sao dois valores a receber, vamos tentar resolver;
nota_aluno = float( input('Informe a nota do aluno: ') )
presenca_aluno = float( input('Informe a presenca do aluno: ') )

#se a nota e a presenca do aluno for maior ou igual a 7 and 70, o aluno sera aprovado;
if nota_aluno >= 7 and presenca_aluno >= 70: #"and" serve para separar 2 ações. EX:mateus "e(and)" Nathalia == Nathalia "e(and)" mateus;
    print('Aprovado')
#elif(else if) represente o meio no caminho do (se e senão), para haver uma 3 opção neste caso uma recuperação;
elif nota_aluno >= 4:
    print('Recuperacao')
#senão, agora que temos o (elif "else if" ) o resultado do senão(else) altera pois temos uma condição que ate o numero 4 temos direito a recuperação;
else:
    print('Reprovado')