from django.db import models
#Criará as tabelas para o banco de dados


class Brand(models.Model): #Nome da classe que criará na tabela do banco de dados
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=200) 

    def __str__(self):
        return self.name #definir o nome da marca como representação do objeto no admin


class Car(models.Model): #Nome da classe que criará na tabela do banco de dados
    id = models.AutoField(primary_key=True) #Campo de identificação único para cada carro, chave primaria do banco de dados
    model = models.CharField(max_length=200) # Campo de texto, max_lenght-max de caracters
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars') #Campo de chave estrangeira, relaciona o carro com a marca, on_delete=models.PROTECT impede que uma marca seja deletada se houver carros relacionados a ela
    factory_year = models.IntegerField(blank=True, null=True) #numeros inteiros
    plate = models.CharField(max_length=20, blank=True, null=True) # Campo de texto, max_lenght-max de caracters, blank=True, null=True torna obrigatório valor
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True) #numero decimal
    #blank=True, null=True torna obrigatório valor
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) #campo de imagem, upload_to define o diretório onde as imagens serão salvas, blank=True, null=True torna obrigatório valor

#toda alteração de tabelas, models e banco atualizar o banco python manage.py makemigrations, python manage.py migrate

    def __str__(self):
        return self.model #definir o nome do carro como representação do objeto no admin