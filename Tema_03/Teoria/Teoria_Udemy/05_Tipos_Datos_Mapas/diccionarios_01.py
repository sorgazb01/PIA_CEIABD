diccionario = {'one' : 1, 'two': 2, 'three' : 3}

print(type(diccionario))
print(diccionario)

print(diccionario['two'])

dict1 = {}
dict1['nombre'] = 'jose'
dict1['edad'] = 20
print(dict1)
print(dict1['nombre'])
print(len(dict1))

del diccionario['one']
print(diccionario)

print('nombre' in dict1)

dict1['nombre'] = 'maria'
dict2 = dict1.copy()
print(dict2)
print(dict1)

dict1['edad'] = 30
print(dict1)