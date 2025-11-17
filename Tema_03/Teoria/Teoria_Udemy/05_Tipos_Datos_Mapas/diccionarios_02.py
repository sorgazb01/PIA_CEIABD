dict1 = {'one':1, 'two':2, 'three':3}

dict1.clear()
print(dict1)

dict1 = {'one':1, 'two':2, 'three':3}
dict2 = {'four':4, 'five':5}
dict1.update(dict2)
print(dict1)

print(dict1['one'])
# print(dict1['ones'])
print(dict1.get('one'))
# print(dict1.get('ones'))
print(dict1.get('ones','no existe'))

print(dict1.pop('one'))
print(dict1)
# print(dict1.pop('six'))
print(dict1.pop('six','no existe'))

for clave in dict1.keys():
    print(clave)

for valor in dict1.values():
    print(valor)
    
for clave,valor in dict1.items():
    print(f'Clave: {clave}, Valor: {valor}')