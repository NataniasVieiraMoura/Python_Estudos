l = []
cc = 0
while True:
    cc+=1
    x = int(input('Digite um número:  '))
    l.append(x)
    ctn = str(input('Deseja continuar?  '))
    if ctn in 'nNãÃoO':
        break
print(l)
l.sort(reverse=True)
print(f'Você digitou {cc} números')
print(l)
if 5 in l[:]:
    print(f'O número 5 aparece na lista.')
else:
    print('O número 5 não aparece na lista.')
print('Fim!')