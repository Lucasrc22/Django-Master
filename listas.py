lista = []

lista.append('Marea')
lista.append('Fusca')
lista.append('Corsa')
lista.append('Gol')

print(lista)

lista.insert(1, 'Uno')
print(lista)

lista.pop(2)
print(lista)

del lista[0]
print(lista)

lista.remove('Gol')
print(lista)

lista.append('Celta')
lista.append('Palio')
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)