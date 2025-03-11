a = 'A'
b = 'B '
c = 1.1

#Tudo no Python é um objeto
#e cada objeto tem o seu método.
#Em uma string, após aspas, se você colocar um .
#voê tem a opção de escolher o método disponível
#neste exercício vamos usar o .format

#chave é o valor determinado pelo formato
#chave vázia seleciona o valor
#na ordem do formato
#sendo:

string = 'a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)

print(formato)

#Parâmetro nomeado

string = 'a={nome0} b={nome1} c={nome2:.2f}'
formato = string.format(
    nome0=a, nome1=b, nome2=c)

print(formato)
