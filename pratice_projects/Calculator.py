'''
Meu primeiro projeto pessoal
Calculadora básica, primeira versão.

'''
num_1 = input('Digite o numero que deseja calcular: ')

try:
    int_1 = int(num_1)
    operador = input('Digite o operador que deseja utilizar: ')

    if operador == '*':
        num_2 = input('Agora digite o número que deseja multiplicar: ')

        try:
            int_2 = int(num_2)
            print(f'A multiplicação de {int_1} por {int_2} é: {int_1 * int_2}')
        except:
            print('Você não digitou um numero!')

    elif operador == '+':
        num_2 = input('Agora digite o número que deseja somar: ')
        try:
            int_2 = int(num_2)
            print(f'A soma de {int_1} e {int_2} é: {int_1 + int_2}')
        except:
            print('Você não digitou um numero!')

    elif operador == '-':
        num_2 = input('Agora digite o número que deseja subtrair: ')
        try:
            int_2 = int(num_2)
            print(f'A subtração de {int_1} menos {int_2} é: {int_1 - int_2}')
        except:
            print('Você não digitou nenhum número!')

    elif operador == '/':
        num_2 = input('Agora digite o número que deseja dividir: ')
        try:
            int_2 = int(num_2)
            print(f'A divisão de {int_1} por {int_2} é: {int_1 / int_2}')
        except:
            print('Você não digitou um número!')
    else:
        print('Você não digitou nenhum operador válido.')

except:
    print('Você não digitou um número!')
