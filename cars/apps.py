from django.apps import AppConfig

#Signals são usados para executar código automaticamente em resposta a certos eventos, como a criação, 
# atualização ou exclusão de um objeto no banco de dados.
#Eles permitem que você conecte funções a esses eventos, para que elas sejam executadas automaticamente quando o evento ocorrer, 
# sem precisar modificar o código do modelo ou da view.
#Ou seja, são comandos ao banco de dados para que ele execute uma função quando um evento ocorrer, 
# como a criação, atualização ou exclusão de um objeto no banco de dados.

class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    def ready(self):
        import cars.signals #Importa o módulo de signals para que ele seja executado quando a aplicação for carregada, ou seja, quando o servidor for iniciado, para que as funções de signals sejam conectadas aos eventos do banco de dados, como a criação, atualização ou exclusão de um objeto no banco de dados.

    