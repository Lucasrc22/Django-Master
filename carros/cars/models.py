from django.db import models
#Criará as tabelas para o banco de dados

class Car(models.Model): #Nome da classe que criará na tabela do banco de dados
    id = models.AutoField(primary_key=True) #Campo de identificação único para cada carro, chave primaria do banco de dados
    model = models.CharField(max_length=200) # Campo de texto, max_lenght-max de caracters
    brand = models.CharField(max_length=200) #Marca
    factory_year = models.IntegerField(blank=True, null=True) #numeros inteiros
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True) #numero decimal
    #blank=True, null=True torna obrigatório valor

#atualizar o banco python manage.py makemigrations, python manage.py migrate

