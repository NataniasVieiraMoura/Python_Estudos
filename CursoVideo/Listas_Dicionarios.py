#pp8
lista = ["Coméia","Maça","Pera","Abacate","Uva passa","Carneiro","Ovelha",
         "Frango","Abobora","Castanha"]
dicionário = {"Chave" : "Valor"}
dic = dict
lista_de_compras = list
print(lista)
lista.append("Goiaba")#adiciona elemento no final da lista
print(lista)
lista.insert(2,"Mel")#insere elemento Mel na posição 2(elemento Pera)
print(lista)
lista.remove("Carneiro")#Remove elemento "Carneiro" da lista
print(lista)
print(lista.index("Castanha"))#posição do elemento inserido
print(lista.pop())#elimina o último elemento da lista por padrão, ou seja, a "Goiaba"
print(lista)
print(lista.pop(4))#Vai remover o "Abacate" porque é o quarto indice da lista
print(lista)
lote = ["Manga", "Cenoura","Manga","Cevada","Manga","Manga"]
for it in lote:
    lista.append(it)
print(lista)
print(lista.count("Manga"))
print(lista)
naturais = [3,2,1,5,22,24,1,4,0]
print(naturais)
naturais.sort()#Ordena os valores númericos na lista
print(naturais)
naturais.reverse()
print(naturais)#Inverte a ordem dos números da lista
soma_listas = []
print(soma_listas)
soma_listas.extend(lote)#adiciona lista a lista
print(soma_listas)
soma_listas.extend(lista)
print(soma_listas)
soma_listas.extend(naturais)
print(soma_listas)
print(min(naturais))#menor número da lista
print(max(naturais))#numero máximo da lista
print(sum(naturais))#soma de todos os números da lista
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

#Laço de indice por elemento:
'''F strings para referênciar variáveis'''
for indice, elemento in enumerate(soma_listas):
    '''Para indice do elemento na lista'''
    print(f"Indice: {indice} para Elemento: {elemento}")

'''Comando Help()'''
def contador(nome="Esperando um nome"):
    nome = str(input("Nome?"))
    '''return: retorna um comando'''
    return print(nome)
contador()

'''Tratamento de erros e Execeções'''
#NomeError
#TypeError
#ZeroDivisionError
#TypeError
#IndexError
#KeyEOF
#Keyboardinterrupt
#OSError
#MemoryError
#ConectionError
#RuntimeError

try:#Operação
    ard = int(input("Nome:"))
    dor = int(input("Sobrenome:"))
    rsut = ard/dor
except:#Falhou
    print("Deu erro meu nobre ;(")
else:#Deu certo
    print(f"Deu bom. Pode continuar;). Deu {rsut:.3f}")
finally:#Certo/Falha
    print("Valeu!Tchau.")
kasth = "Andropoalgia"