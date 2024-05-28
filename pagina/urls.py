from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('cart/', views.cart, name='cart'),
    path('perfil/', views.perfil, name='perfil'),
    path('producto/', views.producto, name='producto'),
]
