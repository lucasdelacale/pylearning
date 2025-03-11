"""primeiro_valor = input("digite o primeiro valor: ")
segundo_valor = input("digite o segundo valor: ")

#if primeiro_valor > segundo_valor:
#    print(f'{primeiro_valor} é maior do que {segundo_valor}')

#elif segundo_valor > primeiro_valor:
#    print(f'o {segundo_valor} é maior que o {primeiro_valor}')

#else:
#    print(f'o {primeiro_valor} e o {segundo_valor} são iguais')


if primeiro_valor > segundo_valor:
    print('primeiro valor é maior do que segundo valor')

elif segundo_valor > primeiro_valor:
    print('ó segundo valor é maior que o primeiro valor')

else:
    print('os valores são iguais')"""

Idade = input('qual a sua idade? ')
int_idade = int(f'{Idade}')

if int_idade >= 18:
    print('voce pode dirigir')

elif int_idade < 18:
    print('voce nao pode dirigir')