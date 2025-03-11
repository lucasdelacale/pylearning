'''
Complexididade de código, boas práticas
e pensamento de escrever código para outros 
programadores de fácil leitura e compreensão.
• 98% dos códigos são escritos
para outros programadore.

• CONSTANTE: "Variáveis" que não vão mudar 
    Utilizar capslock para indicar constante.
• Muitas condições no mesmo if: ruim
    Ter muitas condições torna o código confuso.
• Contagem de complexidade: ruim
    Quanto mais blocos de código
    dentro de outros blocos de código, a leitura
    e o código se tornam mais complexos.
    (Complexidade não é bom)
'''

# exercício
velocidade = 62 #velocidade do carro
local_carro = 99 #km da estrada em que o carro está

RADAR_1 = 60 #limite de velocidade
LOCAL_1 = 100 #km em que o radar está
RADAR_RANGE = 1 #distância onde o radar pega

#simplificando o código para leitura
velocidade_acima_do_limite = velocidade > RADAR_1
range_abaixo_do_km = LOCAL_1 - RADAR_RANGE
range_acima_do_km = LOCAL_1 + RADAR_RANGE
carro_dentro_do_range = \
    local_carro >= range_abaixo_do_km and \
    local_carro <= range_acima_do_km 
carro_multado = carro_dentro_do_range and \
    velocidade_acima_do_limite   
 
if velocidade_acima_do_limite:
    print('o carro passou do limite de velocidade')

if carro_multado:
    print('O carro foi multado')

