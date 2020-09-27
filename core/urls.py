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
from materials_system.controllers import tensao, corrente, graudeprotecao, formacontrutiva, icc, fornecedores, cliente, vendedor, componente
from armarios_system.controllers import armarios, obra

urlpatterns = [
	path('', TemplateView.as_view(template_name="core/index.html"), name='home'),
	path('materiais/', TemplateView.as_view(template_name="materials_system/index.html"), name='materiais'),
    
    path('materiais/corrente/list', corrente.CorrenteListView.as_view(), name='corrente_list'),
	path('materiais/corrente/create', corrente.CorrenteCreateView.as_view(), name='corrente_create'),
    path('materiais/corrente/remove/<int:corrente_pk>', corrente.CorrenteRemoveView.as_view(), name='corrente_remove'),

    path('materiais/tensao/list', tensao.TensaoListView.as_view(), name='tensao_list'),
    path('materiais/tensao/create', tensao.TensaoCreateView.as_view(), name='tensao_create'),
    path('materiais/tensao/remove/<int:tensao_pk>', tensao.TensaoRemoveView.as_view(), name='tensao_remove'),

    path('materiais/icc/list', icc.ICCListView.as_view(), name='icc_list'),
    path('materiais/icc/create', icc.ICCCreateView.as_view(), name='icc_create'),
    path('materiais/icc/remove/<int:icc_pk>', icc.ICCRemoveView.as_view(), name='icc_remove'),

    path('materiais/graudeprotecao/list', graudeprotecao.GraudeProtecaoListView.as_view(), name='graudeprotecao_list'),
    path('materiais/graudeprotecao/create', graudeprotecao.GraudeProtecaoCreateView.as_view(), name='graudeprotecao_create'),
    path('materiais/graudeprotecao/remove/<int:grau_pk>', graudeprotecao.GrauRemoveView.as_view(), name='grau_remove'),

    path('materiais/formaconstrutiva/list', formacontrutiva.FormaConstrutivaListView.as_view(), name='formaconstrutiva_list'),
    path('materiais/formaconstrutiva/create', formacontrutiva.FormaConstrutivaCreateView.as_view(), name='formaconstrutiva_create'),
    path('materiais/formaconstrutiva/remove/<int:forma_pk>', formacontrutiva.FormaRemoveView.as_view(), name='forma_remove'),

    path('materiais/fornecedores/list', fornecedores.FornecedoresListView.as_view(), name='fornecedores_list'),
    path('materiais/fornecedores/create', fornecedores.FornecedoresCreateView.as_view(), name='fornecedores_create'),
    path('materiais/fornecedores/remove/<int:fornecedor_pk>', fornecedores.FornecedoresRemoveView.as_view(), name='fornecedor_remove'),
    path('materiais/fornecedores/edit/<int:fornecedor_pk>', fornecedores.FornecedoresUpdateView.as_view(), name='fornecedores_edit'),

    path('materiais/cliente/list', cliente.ClienteListView.as_view(), name='cliente_list'),
    path('materiais/cliente/create', cliente.ClienteCreateView.as_view(), name='cliente_create'),
    path('materiais/cliente/remove/<int:cliente_pk>', cliente.ClienteRemoveView.as_view(), name='cliente_remove'),
    path('materiais/cliente/edit/<int:cliente_pk>', cliente.ClienteUpdateView.as_view(), name='cliente_edit'),

    path('materiais/vendedor/list', vendedor.VendedorListView.as_view(), name='vendedor_list'),
    path('materiais/vendedor/create', vendedor.VendedorCreateView.as_view(), name='vendedor_create'),
    path('materiais/vendedor/remove/<int:vendedor_pk>', vendedor.VendedorRemoveView.as_view(), name='vendedor_remove'),
    path('materiais/vendedor/edit/<int:vendedor_pk>', vendedor.VendedorUpdateView.as_view(), name='vendedor_edit'),

    path('materiais/componente/list', componente.ComponenteListView.as_view(), name='componente_list'),
    path('materiais/componente/create', componente.ComponenteCreateView.as_view(), name='componente_create'),
    path('materiais/componente/remove/<int:componente_pk>', componente.ComponenteRemoveView.as_view(), name='componente_remove'),
    path('materiais/componente/edit/<int:componente_pk>', componente.ComponenteUpdateView.as_view(), name='componente_edit'),

    path('armarios/', TemplateView.as_view(template_name="armarios_system/index.html"), name='armarios'),

    path('materiais/obra/list', obra.ObraListView.as_view(), name='obras_list'),
    path('materiais/obra/create', obra.ObraCreateView.as_view(), name='obras_create'),
    path('materiais/obra/remove/<int:obra_pk>', obra.ObraRemoveView.as_view(), name='obras_remove'),

    path('armarios/<int:obra_pk>/list', armarios.ArmariosListView.as_view(), name='armarios_list'),
    path('armarios/<int:obra_pk>/create', armarios.ArmariosCreateView.as_view(), name='armarios_create'),
    path('armarios/<int:obra_pk>/remove/<int:armario_pk>', armarios.ArmariosRemoveView.as_view(), name='armarios_remove'),
    path('armarios/colunas/<int:armario_pk>/list', armarios.ArmariosFullListView.as_view(), name='armario_columns_list'),
    path('armarios/colunas/<int:armario_pk>/remove/<int:coluna_pk>', armarios.ArmarioColunaRemoveView.as_view(), name='armario_columns_remove'),
    
    path('admin/', admin.site.urls, name='admin'),
]



