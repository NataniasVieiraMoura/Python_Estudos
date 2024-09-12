lanche = ['macarão', 'Arroz', 'Feijão', 'Margarina']#lista
print(lanche[2])

lanche.append('Queijo')#adiciona no final da fila
print(lanche[4])#seleciona a string escolhida

print(lanche)
lanche.insert(1, 'Galinha')#insere na posição escolhida, furando a fila
print(lanche)

del lanche[2]#deleta o elemento da lista escolhido retirando da fila
'''lanche.pop(2)<= Essa faz a mesma função do del, mas é recomendada para
    remover do final da lista elementos 
=>'''
lanche.pop()

#lanche.remove('')remove o primeiro elemento da lista pelo conteúdo escolhido
print(lanche)

'''Quando você manipula listas a posição das demais é alterada
como se fosse fila de espera.'''
if 'Arroz' in lanche:
    lanche.remove('Arroz')

'''Criação de listas:'''
fast = list(range(10,15))#faz um lista sem o último valor
print(fast)
furious = list(range(0, 11, 2))# ele permite determinar os numeros na lista
print(furious)
angel = [1,5,9,6,3,7,8,2,10,4]
print(angel)
angel.sort()#ordena os números
print(angel)
angel.reverse()#ordena de trás para frente os números
'''angel.sort(reverse=True)'''
print(angel)
print(len(angel))#conta a quantidade de elementos na lista.

'''listas'''
#list()
#listas = []
l = []
#for cnt in range(0, 5):
#    l.append(int(input('Digiete um valor? ')))
e = []
while True:
    e.append(int(input('Digite um número:  ')))
    a = str(input('Continuar: '))
    if a in 'nN':
        break
print(e)
#for t, d in enumerate(l):
#    print(f'Em {t} achei {d}')
print('A lista acabou!')

p = l# essas listas se ligam(o que ocorre com uma ocorre com a outra).
p = l[:]#essa lista não se ligam

'''Falta agora começar a fazer exercicios!!!'''
















