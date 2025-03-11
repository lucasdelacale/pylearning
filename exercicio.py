nome = input ('digite o seu nome: ')
idade = input ('digite a sua idade: ')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('seu nome contém espacos')
    else:
        print('seu nome não contém espaços')
        
    print(f'seu nome contem {len(nome)} letras')
    print(f'a primeira letra do seu nome é: {nome[0]}')
    print(f'a ultima letra do seu nome é: {nome[4]}')

else:
    print('Desculpe, você deixou campos vázios.')