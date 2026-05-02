from django.db.models.signals import pre_save, post_save, post_delete #Importando os sinais de pós-salvamento e pós-exclusão do Django
from django.dispatch import receiver #Importando o decorador receiver do Django, que é usado para conectar uma função a um sinal específico, ou seja, para que a função seja executada automaticamente quando o sinal for disparado, ou seja, quando um evento ocorrer, como a criação, atualização ou exclusão de um objeto no banco de dados. 
from cars.models import Car, CarInventory
from django.db.models import Sum #Importando o módulo models do Django, que é usado para definir os modelos de dados e realizar operações de banco de dados, como consultas, agregações, etc.
from openai_api.client import generate_car_description #Importando a função get_car_description do módulo openai_api, que é usada para gerar uma descrição de venda para um carro usando a API da OpenAI, ou seja, para criar uma descrição automática para os carros que não tiverem uma descrição específica.


def car_inventory_update():
    cars_count = Car.objects.count() #consultou no ORM do Django a quantidade total de objetos do modelo Car no banco de dados, ou seja, a quantidade total de carros no banco de dados, e armazenou esse valor na variável cars_count.
    cars_value = Car.objects.aggregate(
        total_value = Sum('value') #calculou a soma dos valores de todos os objetos do modelo Car no banco de dados, ou seja, o valor total de todos os carros no banco de dados, e armazenou esse valor na variável cars_value, usando o método aggregate do ORM do Django, que permite realizar operações de agregação em um conjunto de objetos, como soma, média, contagem, etc., e o models.Sum é uma função de agregação que calcula a soma dos valores de um campo específico, neste caso, o campo 'value' do modelo Car.
    
    )['total_value'] #acessou o valor total calculado na etapa anterior, usando a chave 'total_value', que é o nome do campo definido na função aggregate, e armazenou esse valor na variável cars_value.
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value) #Criou um novo objeto do modelo CarInventory no banco de dados, usando o método create do ORM do Django, que permite criar um novo registro no banco de dados com os valores especificados para os campos, neste caso, os valores de cars_count e cars_value calculados nas etapas anteriores, ou seja, a quantidade total de carros e o valor total dos carros no banco de dados, respectivamente.

@receiver(pre_save, sender = Car)
def car_pre_save(sender, instance, **kwargs): #Função que será executada antes
    if instance.bio == "": #Verificando se o campo de descrição (bio) do objeto Car está vazio, ou seja, se não tem nenhum valor atribuído, e se estiver vazio, atribui o valor "Sem descrição" ao campo bio do objeto Car, ou seja, define uma descrição padrão para os carros que não tiverem uma descrição específica.
        ai_bio = generate_car_description(instance.model, instance.brand, instance.model_year) #Gerando uma descrição de venda para o carro usando a função generate_car_description, passando como parâmetros o modelo, a marca e o ano do modelo do carro, e armazenando o resultado na variável ai_bio.
        instance.bio = ai_bio #Verificando se o campo de descrição (bio) do objeto Car está vazio, ou seja, se não tem nenhum valor atribuído, e se estiver vazio, atribui o valor "Sem descrição" ao campo bio do objeto Car, ou seja, define uma descrição padrão para os carros que não tiverem uma descrição específica.


@receiver(post_save, sender = Car)
def post_save_car(sender, instance, created, **kwargs): #Função que será executada após salvar um objeto do modelo Car no banco de dados, ou seja, após criar ou atualizar um carro no banco de dados, e o sender é o modelo Car, ou seja, a função será executada apenas para objetos do modelo Car, e o instance é o objeto que foi salvo, ou seja, o carro que foi criado ou atualizado, e o created é um booleano que indica se o objeto foi criado (True) ou atualizado (False), e os kwargs são os argumentos adicionais que podem ser passados para a função, como o usuário que está realizando a ação, ou a data e hora da ação.
    car_inventory_update()


 
@receiver(post_delete, sender = Car)
def post_delete_car(sender, instance, **kwargs): #Função que será executada após excluir um objeto do modelo Car no banco de dados, ou seja, após remover um carro do banco de dados, e o sender é o modelo Car, ou seja, a função será executada apenas para objetos do modelo Car, e o instance é o objeto que foi excluído, ou seja, o carro que foi removido, e os kwargs são os argumentos adicionais que podem ser passados para a função, como o usuário que está realizando a ação, ou a data e hora da ação.
    car_inventory_update()



