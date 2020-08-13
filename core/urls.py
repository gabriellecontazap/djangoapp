"""core URL Configuration

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 
from materials_system.controllers import tensao, corrente, fabricantes, linha

urlpatterns = [
	path('', TemplateView.as_view(template_name="core/index.html"), name='home'),
	path('materiais/', TemplateView.as_view(template_name="materials_system/index.html"), name='materiais'),
    
    path('materiais/corrente/list', corrente.CorrenteListView.as_view(), name='corrente_list'),
	path('materiais/corrente/create', corrente.CorrenteCreateView.as_view(), name='corrente_create'),
    
    path('materiais/tensao/list', tensao.TensaoListView.as_view(), name='tensao_list'),
    path('materiais/tensao/create', tensao.TensaoCreateView.as_view(), name='tensao_create'),
    
    path('materiais/fabricantes/list', fabricantes.FabricantesListView.as_view(), name='fabricantes_list'),
    path('materiais/fabricantes/create', fabricantes.FabricantesCreateView.as_view(), name='fabricantes_create'),
    
    path('materiais/linha/list', linha.LinhaListView.as_view(), name='linha_list'),
    path('materiais/linha/create', linha.LinhaCreateView.as_view(), name='linha_create'),
    
    path('armarios/', TemplateView.as_view(template_name="armarios_system/index.html"), name='armarios'),
    path('admin/', admin.site.urls, name='admin'),
]



