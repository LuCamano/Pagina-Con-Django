from django.urls import path
from . import views

urlpatterns = [
    path('registrarse/', views.registrarse, name='registrarse'),
    path('login/', views.loginV, name='login'),
    path('logout/', views.logoutV, name='logout'),
]
