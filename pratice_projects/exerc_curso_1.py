'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
'''
# try:
#     numero = int(input('Digite um número inteiro: '))
#     if numero % 2 == 0:
#         print(f'O número {numero} é par')
#     else:
#         print(f'O número {numero} é impar')
# except:
#     print('Por favor, digite um número inteiro')
#
# Exercício finalizado!

#----------------------------------------------------------
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# try:
#     hora = int(input('Que horas são?: '))
#     if hora >= 0 and hora <= 11:
#         print('Boa dia!')
#     if hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     if hora >= 18 and hora <= 23:
#         print('Boa noite!')
#     if hora > 23:
#         print('Digite um horário válido')
# except:
#     print('Digite um horário válido')
#----------------------------------------------------------

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# nome = input('Por favor, digite o seu nome: ')
# caracteres = len(nome)
# if caracteres <= 4:
#     print('O seu nome é curto.')
# elif caracteres >= 5  and caracteres <= 6 :
#     print('O seu nome é normal.')
# elif caracteres > 6: 
#     print('O seu nome é muito grande.')