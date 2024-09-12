lista = ["Coméia","Maça","Pera","Abacate","Uva passa","Carneiro","Ovelha",
         "Frango","Abobora","Castanha"]
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
#Laço de indice por elemento:
'''F strings para referênciar variáveis'''
for indice, elemento in enumerate(soma_listas):
    '''Para indice do elemento na lista'''
    print(f"Indice: {indice} para Elemento: {elemento}")

'''List Comprehension'''
'''Cria uma lista com um laço'''
numerais = [x for x in range(1,11)]
print(numerais)
num_raiz_qdda = [r**-2 for r in numerais]
print(num_raiz_qdda)
num_raiz_cub = [r**-3 for r in numerais]
print(num_raiz_cub)
num_quad = ([r**2 for r in numerais])
num_cub = ([r**3 for r in numerais])
print(f"{num_quad}\n{num_cub}")

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