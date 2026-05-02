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
    bio = models.TextField(blank=True, default= "") #campo de texto longo, blank=True, null=True torna obrigatório valor
#toda alteração de tabelas, models e banco atualizar o banco python manage.py makemigrations, python manage.py migrate

    def __str__(self):
        return self.model #definir o nome do carro como representação do objeto no admin
    
class CarInventory(models.Model):
    cars_count = models.IntegerField() # Campo de número inteiro para armazenar a quantidade de carros no inventário
    cars_value = models.FloatField() # Campo de número decimal para armazenar o valor total dos carros no inventário
    created_at = models.DateTimeField(auto_now_add=True) # Campo de data e hora para armazenar a data de criação do registro, auto_now_add=True define que o valor será definido automaticamente quando o registro for criado

    class Meta: #Meta é uma classe interna que define opções de configuração para o modelo
        ordering = ['-created_at'] # Define a ordenação dos registros, neste caso, os registros mais recentes aparecerão primeiro

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}' #definir a quantidade de carros e o valor total como representação do objeto no admin