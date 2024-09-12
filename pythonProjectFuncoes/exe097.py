frase = str(input('Digite uma frase: '))


def txt(frase):
    print('~~'+'~'*int(len(frase))+'~~')
    print(f'  {frase}')
    print('~~'+'~' * int(len(frase))+'~~')


txt(frase)