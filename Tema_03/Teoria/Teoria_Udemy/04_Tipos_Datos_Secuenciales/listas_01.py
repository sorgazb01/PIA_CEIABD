lista1 = []
print(type(lista1))

lista2 = [1,"a",True]
lista = [1,2,3,4,5,6]
for num in lista :
    print(num)
    
lista2 = ["a","b","c","d","e"]

for num,letra in zip(lista,lista2):
    print(f'{num} {letra}')
    
print(2 in lista)

print(7 in lista)

lista = lista + [6,7,8]

print(lista)

lista = lista * 2

print(lista)

print(lista[0])