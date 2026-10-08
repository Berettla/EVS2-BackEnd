from django.urls import path
from . import views

app_name = 'home_agustin'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('genero/<str:nombre_genero>/', views.detalle_genero, name='detalle'),
]