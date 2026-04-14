from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #listar os campos na tabela do admin
    search_fields = ('model','brand', 'factory_year', 'model_year', 'value') # vai poder buscar o modelo criado

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',) #listar o campo name na tabela do admin
    search_fields = ('name',) # vai poder buscar a marca criada


admin.site.register(Car, CarAdmin) #registrando a classe criada no admin
admin.site.register(Brand, BrandAdmin) #registrando a classe criada no admin

