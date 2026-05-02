from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import NewCarCreateView, CarListView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view



urlpatterns = [
    path("admin/", admin.site.urls), #sempre dois parametros, o primeiro é a url e o segundo é a view que vai ser chamada quando acessar essa url
    path("cars/", CarListView.as_view(), name='cars_list'), #adicionar a url para acessar a view de carros, dando o nome para puxar o html, as_view() é necessário para usar a classe CarListView como view, pois ela é uma classe e não uma função
    path("cars/<int:pk>/", CarDetailView.as_view(), name='car_detail'), #adicionar a url para acessar a view de detalhes do carro, usando o id do carro como parametro, dando o nome para puxar o html
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name='car_delete'), #adicionar a url para acessar a view de deletar o carro, usando o id do carro como parametro, dando o nome para puxar o html
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name='car_update'), #adicionar a url para acessar a view de edição do carro, usando o id do carro como parametro, dando o nome para puxar o html
    path("new_car/", NewCarCreateView.as_view(), name='new_car'), #adicionar a url para acessar a view de criar um novo carro, dando o nome para puxar o html
    path("register/", register_view, name = 'register'), #adicionar a url para acessar as urls do app de contas
    path("login/", login_view, name ='login'), #adicionar a url para acessar a view de login, dando o nome para puxar o html
    path("logout/",logout_view, name ='logout'),#adicionar a url para o usuário realizar logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #adicionar a url para acessar as imagens
