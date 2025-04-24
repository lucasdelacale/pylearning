import random   #Random é uma biblioteca, neste caso import é o código que puxa a biblioteca
#A biblioteca "random" trabalha com números aleatórios
 
numero_secreto = random.randint(1,10)
# random.randint gera uma aleatoriedade sempre entre dois parâmetros == (a,b)

#Mensagem de boas vindas
print('Bem vindo ao jogo de adiviha')
print('Escolha um numero entre 1 e 10')

#Primeiro criamos um loop infinito principal
while True:
    numero_secreto = random.randint(1,10)
    tentativas = 0 #Contador de tentativas em loop
    #Aqui vamos fazer um campo para que o usuário insira o seu palpite
    while True: #para que o jogo continue rodando até o usuário acertar
        try: #tentativa, caso encontre um erro ele pula pro except
            palpite = int(input('Digite o seu palpite: '))
            tentativas += 1 #adiciona uma tentativasempre que o usuário der o palpite
            diferenca = abs(numero_secreto - palpite) #Diferença abs sempre retorna número absoluto 
            #Usaremos para incluirmos uma mensagem
            #personalizada de acordo com o numero do usuário    
            #Agora vamos fazer uma comparação do palpite com o número secreto com condicionais
            #Se o número for menor
            if palpite < numero_secreto:
                if diferenca > 3:
                    print('Muito baixo! Tente novamente.')
                else:
                    print('Quase lá! Um pouco mais.')
            #Se o número for maior
            elif palpite > numero_secreto:
                if diferenca > 3:
                    print('Muito alto! Tente novamente.')
                else:
                    print('Quase lá! Um pouco menos.')
            #Caso o usuário acerte
            else:
                print(f'Parabéns! Você acertou em {tentativas} tentativas! O número secreto era {numero_secreto}.')
                break #sai do loop quando o usuário acerta
            #Importante ressaltar que um break identado, sai apenas do bloco de código
            # em que o usuário esstá, portanto fechamos as condicionais e o loop

            #Na linha abaixo o fechamento de try-except caso o usuário não digite um número válido
        except:
            print('Por favor, digite um número válido')

    #Por fim, iniciaremos outro loop identado para o caso do usuário quiser continuar jogando
    while True:
    #vamos criar uma váriavel com imput para o usuário escolher
        continuar = input('Você quer jogar novamente? Digite S para sim ou N para não: ').strip().upper()
        #.strip() retira espaços
        #.upper() transforma todo o input do usuário em maiúsculas
        #Isso garante a segurança do nosso código
        if continuar == 'N': #para sair
            print('Obrigado por jogar, até a próxima!')
            exit() #Sai do programa!

        elif continuar == 'S': #para jogar novamente
            break #reinicia o jogo
        else:
            print('Opção inválida, digite apenas S ou N.')
                






