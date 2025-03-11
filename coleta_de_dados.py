#Coletando dados do usuário
#utilizando a função input para interação

#nome = input('qual o seu nome?')
#print(f'o seu nome é {nome}')

#utilizando numeros 
#input sempre retorna uma string
#é preciso que essa string seja formatada 
# para chegar no valor real
#utilizando (int ou float) para formatar

numero_1= (input('Digite um número: '))
numero_2= (input('Digite outro número: '))

try:
        int_1 = int(numero_1)
        int_2 = int(numero_2)
        soma = (int_1 + int_2)
        print(f'A soma dos números é: {soma}')

except:
        print('Não é possível fazer esta soma')
