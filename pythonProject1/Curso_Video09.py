soh = "Nomes_pessoa"
gso = "Outras Coisa a mais"
print(f"{soh:>20}")
print(f"{gso:<40}",end="")
print(f"loren ipson dor met")
'''O camando break finaliza o bloco de execução, serve no caso de interronper loop'''
if "oO" in soh:
    print("Sim, há")
else:
    print("Não há")

lista = [1,2,3,4,5,6,7,8,9]
prot_lis = lista.copy()#Para copiar uma lista
'''Use o método copy() para copiar todos os elementos da outra lista sem ficar
ligado a ela. A lista "prot_lis" se torna uma lista independente da lista "lista"
sem que uma se altere quando outra for manipulada.'''
outro = lista
'''A lista "outro" fica ligada a lista "lista". Tudo que acontecer com um, 
acontece com o outro.'''
print(lista)
lista.clear()#Limpa uma lista
print(lista)
print(prot_lis[:])#Dois pontos serve para requisitar todos os elementos da lista
print(prot_lis[3:7])#invervalo de elementos requisitados

dicionário = dict()
fala = str
fala = input("M ou F:").upper()[0]
print(fala)
comenta = str(input("Homem ou Mulher?")).upper()[:]
print(comenta)