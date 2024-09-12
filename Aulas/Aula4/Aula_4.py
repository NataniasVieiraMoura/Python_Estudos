'''Parei na aula 4 do curso youtube de AI'''
#Você pode otimizar a linguagem com os recursos que ela possui
#Faça testes, veja até onde o python vai com a lógica
def barra():
    print(f"\033[7m\n\033[m")
'''
n =0
while(False):#Loop padrão
    print(n)
    n+=1
'''

'''
for x in range(11):#laço normal
    print(x)
'''

#print([x for x in range(10)])#testei e o pytho aceitou

lista = [i for i in range(20)]#list comprehension normal
texto = "vai comprar salmão no armazém Adalberto Faria na esquina 4 com a 3º da Magnólia"
'''
for k in lista:#laço sobre elementos de uma list comprehension
    print(k)
'''

for y in set(["Caracter único --> "+u for u in texto]):#laço sobre list comprehension setado
    print(y)
barra()

nomes = ["Carlos", "Vanessa","Alessandra", "Alberta", "Berta","Beatriz","Alemanha"]
idades = [15,26,25,21,23,29,30]


#for x, y in enumerate(nomes):
#    print(f"{x} em {y}")
barra()

'''
indexado = {(x, y) in enumerate(nomes)}
print(indexado)
barra()
'''

#para visualizar dois elementos de mesmo indice para listas diferêntes
'''for nomes, idades in zip(nomes, idades):
    print(f"{nomes} tem {idades}")
barra()'''

#Crie um arquivo txt nesse diretório chamado "arquivo.txt"
with open ("arquivo.txt") as arq:#abre o arquivo em um bloco de código
    num =1
    for n, item in enumerate(arq, start = 1):#você define o inicio de contagem do enumerate com start definido o inicio
        print(f"Linha: {n} Conteúdo: {item}".strip())#strip para não soltar linha
    #Dá erro de utf-8, mas funciona
barra()

bilhar = {nomes[i]: idades[i] for i in range(len(nomes))}
print(bilhar)
barra()

for v in bilhar.values():
    print(v)
barra()

for k in bilhar.keys():
    print(k)
barra()

'''Você insere ambos os elementos da biblioteca com items'''
'''esse recurso não ocorre em todas as versões do python'''
for k,v in bilhar.items():
    print(f"Em {k} tenho {v}")
barra()

#testei e dá certo, o max busca o maior valor dentre os items
print(max(bilhar.items()))#mosta o maior número nos items da lista
#lembre: item é chave-valor
barra()

cols = 5
linhas = 5
#esse código é muito grande
achou = False
for c in range(cols):
    for l in range(linhas):
        if l  and c == 3:
            achou = True
            break
    if achou == True:
        break
barra()
#para reduzir o código acima


