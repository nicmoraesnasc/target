def count_a(text):
    text = text.lower()

    counter = text.count('a')

    a_exists = counter > 0

    return a_exists, counter

string = input('Digite qualquer coisa para verificar a existência e quantidade de letras A: ')
a_exists, counter = count_a(string)

if a_exists:
    print('A letra "a" está presente')
else:
    print('Não há letra "a" na frase')

print(f'A qantidade de vezes que "a" ocorre é: {counter}')

    

