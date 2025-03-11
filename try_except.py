''''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
 
#Try - tenta executar o código no bloco
#except - caso ocorra um erro no try ele executa o except

# exemplo

num_1 = input ('digite um numero para duplicar: ')

try:
    numint_1 = float(num_1)
    print(f'o dobro de {numint_1} é {numint_1 * 2:.2f}')

except:
    print('você não digitou um número')
