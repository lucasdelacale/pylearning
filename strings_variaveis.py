#Calculo de Indice de Massa coporral
nome = 'Lucas Martins'
altura = 1.78
peso = 60
imc = peso / altura ** altura

#Forma 1
#Utilizando variaveis e strings de 
#forma simples
print( nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos e seu imc é')
print(imc)


#Base da forma 2
#Utilizando f-strings
#no inicio de cada string, quando colocamos o f
#utilizamos a possibilidade de usar variaveis
#dentro de strings
linha_1 = f'{nome} tem {altura} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
#:.2f para formatar as casas decimais
#quando for contabil utilizar virgula
#1.499.90

#Forma 2
print(linha_1)
print(linha_2)
print(linha_3)
