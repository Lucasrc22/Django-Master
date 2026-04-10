numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []

def dobro(numero):
    return numero * 2
numeros_dobrados = [ dobro(numero)for numero in numeros]

print(numeros_dobrados)

nomes = ['Alice', 'Bob', 'Charlie', 'David','Arnaldo']

nomes_maiusculos = [ nome.upper() for nome in nomes if nome[0]=='A']
print(nomes_maiusculos)