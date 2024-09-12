#simples
numeros = [x for x in range(1,30, 3)]
print(numeros)
pares = [p for p in range(0,30,2)]
print(pares)
impares = [i for i in range(-1,30,2)]
print(impares)

#com condição:

five  = [r for r in range(1,50, 1) if r%5 == 0]
print(five)

primo = [pr for pr in range(1,100) if pr%2 !=0 and pr%3!=0]
print(primo)

