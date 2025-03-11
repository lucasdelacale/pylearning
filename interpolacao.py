''''
Interpolação básica de strings
s - string
d e i - int
f - float
x e x - hexadecimal (ABCDEF0123456789)
'''
#Para fazer a interpolação podemos
#utiizar % antes da letra de formatação
# a interpolação por si, vem após o fechamento
#da string

nome = 'Lucas'
preco = 169.95897643
variavel = '%s, o preco total foi de R$%.2f' %(nome, preco)
print(variavel)

#utilizando hexadecial
#são numero com letras de A a F e de 0 a 9

print('o hexadecimal de %d é %.2x' %(10, 10))