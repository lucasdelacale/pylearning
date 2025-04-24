# Prática de funções

def show_podium (podium):
    print(f'1º Place: {podium[0]}')
    print (f'2º Place: {podium[1]}')
    print(f'3º Place: {podium[2]}')
    print('')
    return podium    
    
match_1 = ["Lucas", 'Renan', 'Hugo', 'Antônio', 'Helcio']
match_2 = ['Renan', 'Antônio', 'Helcio', 'Lucas', 'Hugo']

print('Podium of first match')
show_podium(match_1)

print('Podium of second match')
show_podium(match_2)