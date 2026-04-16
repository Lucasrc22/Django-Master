from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view





urlpatterns = [
    path("admin/", admin.site.urls), #sempre dois parametros, o primeiro é a url e o segundo é a view que vai ser chamada quando acessar essa url
    path("cars/", cars_view), #adicionar a url para acessar a view de carros
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #adicionar a url para acessar as imagens
 