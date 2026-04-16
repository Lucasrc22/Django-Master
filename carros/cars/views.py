from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all() 
    print(cars)#retorna todos os objetos do modelo Car, equivalente a SELECT * FROM Car
    return render(
        request, 
        'cars.html',
        {'cars': cars} #dicionário de contexto, onde a chave 'cars' é usada para acessar os dados no template, e o valor é outro dicionário com a chave 'model' e o valor 'Civic'}
    )
#ORM é uma forma de interagir com o banco de dados usando objetos em vez de escrever SQL diretamente, 
# o Django ORM é uma camada de abstração que permite criar, recuperar, 
# atualizar e excluir objetos do banco de dados usando código Python, 
# sem precisar escrever consultas SQL complexas. 
# Ele traduz as operações em consultas SQL subjacentes, facilitando o desenvolvimento e a manutenção do código.