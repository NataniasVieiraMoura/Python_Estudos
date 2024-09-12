from random import randint
codigo = ""
lista = list()
for x in range(1,20):
    for y in range(1,3):
        num = randint(1, 999)
        codigo += str(num)
    lista.append(codigo)
    codigo = ""
    num = 0
#print(lista)


from random import choice
alfabeto = "abcdefghijklmnopqrstuvwxyz"
nomes = list()
palavra = ""
for x in range(1,20):
    for y in range(1,7):
        letra = choice(alfabeto)
        palavra += letra
    nomes.append(palavra)
    palavra = ""
    letra = ""
#print(nomes)

#Você pode criar uma dict comprehension para criar dicionários
#No exemplo abaixo o dicionário recebe o respectivo elemento de cada lista
#e transforma em chave e valor do dicionário.
def codigo_cliente(nomes,lista):
    return print({nomes[c]: lista[c] for c in range(len(nomes))})
#codigo_cliente(nomes,lista)



numeros = lista.copy()
textos = nomes.copy()
def diciOnarizador(numeros,textos):
    lista_tupla_pares =[(nomes[c],lista[c]) for c in range(len(nomes))]
    dicionario = dict(lista_tupla_pares)
    print(f"A lista de pares de tuplas: {lista_tupla_pares}"
          f"\nPode ser transformada em dicionário : {dicionario}\n"
          f"respectivamente chave:valor")
diciOnarizador(nomes,lista)
