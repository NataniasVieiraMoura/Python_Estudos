"""
Playlist do YouTube Python intermediário e avançado
Sim, é possível usar if e else dentro de uma list comprehension no Python. A sintaxe é a seguinte:

Exemplo com if e else:
"""
lista = [x if x % 2 == 0 else -x for x in range(10)]
print(lista)
"""
Neste exemplo, para cada número na lista, se o número for par (x % 2 == 0), ele será adicionado normalmente, e se for ímpar, ele será adicionado como seu valor negativo.

Exemplo sem else (apenas com if):

Se você quiser apenas incluir elementos que satisfaçam uma condição, sem modificar os outros, o else não é necessário:
"""
lista2 = [x for x in range(10) if x % 2 == 0]
print(f"\n{lista2}")
"""
Aqui, apenas os números pares serão incluídos na lista.

Resumindo:

Para usar if e else na list comprehension, eles vêm antes da parte do for.

Se não houver else, o if é colocado no final, após o for.
"""
#lista3 = (x for x in range(6E4_000_000))#gerador
#print(f"\n{lista3}")