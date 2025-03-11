'''
Projeto: Calculadora Básica
Versão 2

Atualizações: Loop while para diminuir a quantidade de try-except
para receber o input e corrigir a string para inteiro.

'''
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#Função para pedir o primeiro valor ao usuário.

def get_number (message): #O parâmetro é a mensagem personalizada a ser imputada
    #Substitui utilizar diversos try-except como feito na v1
    while True: #While por padrão, é infinito e para somente quando a condição é False
        #Neste caso, while True, repete a função até que o valor seja True
        try:
            return float(input(message)) 
        #Aqui está a solicitação de um número e tenta converter para inteiro
        except ValueError: #ValueError é um erro específico de valor, torna o código mais seguro
            print('Você não digitou um número, tente novamente.') #Trata o erro e repete um novo input
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#Função para pedir um operador de cálculo ao usuário
def get_operator (): #O operador está vazio pois a mensagem sempre será a mesma
    valid_operators = ['*','+','-','/'] #Lista com os operadores válidos
    while True: #Loop infinito que para quando a condição for falsa
        operator = input('Digite um operador de cálculo: ')
        if operator in valid_operators:
        #Confere se o operador digitado está na lista permitida
            return operator #Retorna o operador
        else:
            print('O operador digitado não é permitido, tente novamente.') 
        #Se o operador não for válido
        #O else printa a mensagem e o loop while retorna até que a condição seja verdadeira.
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
while True:
#Obtendo os inputs do usuário
    print('-')
    number_one = get_number ('Digite um número que deseja calcular: ') #Mensagem personalizada para a função get_number
    operator = get_operator() #Chamada da função get_operator
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#Mensagem personalizada de acordo com o operador
    if operator == '*':
        number_two = get_number ('Digite o valor que deseja multiplicar: ')
#-----------------------------------------------------------------------------------------------#
    elif operator == '+':
        number_two = get_number ('Digite o valor que deseja somar: ')
#-----------------------------------------------------------------------------------------------#
    elif operator == '-':
        number_two = get_number ('Digite o valor que deseja subtrair: ')
#-----------------------------------------------------------------------------------------------#
    elif operator == '/': #A divisão por 0 em Python dá erro.
    #Portanto, vamos utilizar um loop while para o caso do usuário digitar errado
    #O código poderá rodar novamente de forma automática, sem voltar do início
        while True:
            number_two = get_number ('Digite o valor que deseja dividir: ')
            if number_two == 0:
                print('Ops, não podemos dividir por zero, tente outro número.')
            else:
                break #Sai do loop se o número for diferente de zero.
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#Obtendo os cálculos
    if operator == '*': #Multiplicação
        result = number_one * number_two
        print(f'A multiplicação de {number_one} e {number_two} é {result:.2f}')
#-----------------------------------------------------------------------------------------------#
    elif operator == '+': #Adição
        result = number_one + number_two
        print(f'A soma de {number_one} e {number_two} é {result:.2f}')
#-----------------------------------------------------------------------------------------------#
    elif operator == '-': #Subtração
        result = number_one - number_two
        print(f'A subtração de {number_one} menos {number_two} é {result:.2f}')
#-----------------------------------------------------------------------------------------------#
    elif operator == '/': #Divisão
        result = number_one / number_two
        print(f'A divisão de {number_one} por {number_two} é {result:.2f}')
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#Final do cálculo
#Iniciaremos um loop para caso o usuário queira continuar ou finalizar
    while True:
        print('-')
        print('Deseja continuar calculando?')
        loop_calculate = input('Digite S para continuar ou N para sair: ').strip().upper()
        #Variável que pergunta se o usuário quer continuar
        if loop_calculate == 'N': #Não
                print('Tudo bem, até a próxima!')
                exit() #Finaliza o programa
        elif loop_calculate == 'S': #Sim
                break #O break para apenas o loop em que o código está
                    #Dessa forma, ele retorna ao início.
        else: #Caso a opção seja inválida
            print('Opção inválida. Digite apenas S ou N.')
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
