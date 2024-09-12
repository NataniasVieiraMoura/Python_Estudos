'''Exercico 072'''
tuplex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Qual número deseja ver entre 0 e 20:  '))
    if numero >= 0 and numero <= 20:
        break
    print('Errou, tente novamente', end=' .')
print('Você digitou : ', tuplex[numero])
