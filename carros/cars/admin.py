from django.contrib import admin
from cars.models import Car


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #listar os campos na tabela do admin
    search_fields = ('model',) # vai poder buscar o modelo criado

admin.site.register(Car, CarAdmin) #registrando a classe criada no admin

