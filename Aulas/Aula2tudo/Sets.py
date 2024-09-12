#Set: um tipo de lista que pode ser manipulada,mas não aceita valores iguais
#representado por set()
# posteriormente ao representar utilize {} caso deseje manipular
unicos = set()
unicos.add(100)
unicos.add(200)
unicos.add(3)
unicos.add(400)
print(unicos)
unicos.add(3)#veja que ele não vai adicionar o valor
print(unicos)#não adiciona o 3
unicos.add(40)
print(unicos)

primos = set([x for x in range(-1,21,2)])
print(primos)
somados  = primos.union(unicos)#uniu elementos
print(somados)
somados.pop()
somados.pop()
print(somados)

lista = list(somados)
print(type(lista))

