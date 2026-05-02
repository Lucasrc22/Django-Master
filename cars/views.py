from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required #decorator para proteger as views, ou seja, para que apenas usuários logados possam acessar as views, e caso o usuário não esteja logado, ele será redirecionado para a página de login
from django.utils.decorators import method_decorator #decorator para proteger as views baseadas em classe




class CarListView(ListView):

    model = Car #Dizendo que a view é baseada no modelo Car, para que ela saiba de onde puxar os dados
    template_name = 'cars.html' #Dizendo qual template usar para renderizar a página, caso não seja especificado, o Django irá procurar por um template com o nome do modelo em minúsculo, seguido de '_list.html', ou seja, 'car_list.html'
    context_object_name = 'cars' #Dizendo qual nome usar para acessar os dados no template, caso não seja especificado, o Django irá usar 'object_list' como nome padrão para acessar os dados, ou seja, {{ object_list }} no template
    def get_queryset(self): #Sobrescreve o método get_queryset() da classe ListView, para personalizar a forma como os dados são recuperados do banco de dados, ou seja, para adicionar a funcionalidade de busca
#super() é usado para chamar o método get_queryset() da classe pai (ListView), que retorna o queryset padrão, que é Car.objects.all(), ou seja, todos os objetos do modelo Car, e depois ordena por modelo usando order_by('model')
        queryset = super().get_queryset().order_by('model') #Chama o método get_queryset() da classe pai (ListView) para obter o queryset padrão, que é Car.objects.all(), e depois ordena por modelo
        search = self.request.GET.get('search') #Pega o valor do parâmetro 'search' da requisição
        if search:
            queryset = queryset.filter(model__contains=search)
        return queryset

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

    
@method_decorator(login_required, name='dispatch') #Adiciona o decorator login_required para proteger a view, ou seja, para que apenas usuários logados possam acessar a view, e caso o usuário não esteja logado, ele será redirecionado para a página de login
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/' #Redireciona para a página de listagem de carros após criar um novo carro, usando a url definida em urls.py




@method_decorator(login_required, name='dispatch') #Adiciona o decorator login_required para proteger a view, ou seja, para que apenas usuários logados possam acessar a view, e caso o usuário não esteja logado, ele será redirecionado para a página de login
class CarUpdateView(UpdateView):
    
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/' #Redireciona para a página de listagem de carros após editar um carro, usando a url definida em urls.py
    
    def get_success_url(self): #Self é a instância da classe CarUpdateView, ou seja, o objeto que está sendo editado, e self.object é o objeto que foi editado, ou seja, o carro que foi editado, e self.object.pk é o id do carro que foi editado, ou seja, a chave primária do carro que foi editado
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk}) #Redireciona para a página de detalhes do carro editado, usando a url definida em urls.py, passando o id do carro como parametro
    
@method_decorator(login_required, name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/' #Redireciona para a página de listagem de carros após deletar um carro, usando a url definida em urls.py

#ORM é uma forma de interagir com o banco de dados usando objetos em vez de escrever SQL diretamente, 
# o Django ORM é uma camada de abstração que permite criar, recuperar, 
# atualizar e excluir objetos do banco de dados usando código Python, 
# sem precisar escrever consultas SQL complexas. 
# Ele traduz as operações em consultas SQL subjacentes, facilitando o desenvolvimento e a manutenção do código.