"""Monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls
     import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from recursos.api import viewsets as registrosviewsets
from recursos import views

route = routers.DefaultRouter()
route.register(r'registros', registrosviewsets.RegistroViewSet,basename='Registros') 

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/', include(route.urls), name='api'),
    path('', views.home, name='home'),
    path('graph/<str:equipamento>/', views.graph, name='graph'),    
    path('lista_equipamentos/', views.lista_equipamentos, name='lista_equipamentos')
]
