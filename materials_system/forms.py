from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User, Permission
from django.conf import settings
import requests, json
from materials_system.models import Tensao, Corrente, Fornecedores, ICC

def get_value(objs, response):
	for obj in response:
		objs.append((obj[u'value'], obj['value']))
	return objs

def get_name(objs, response):
	for obj in response:
		objs.append((obj[u'name'], obj['name']))
	return objs

class TensaoForm(forms.Form):
	value = forms.IntegerField(required=True, label=u'Valor', widget=forms.TextInput(attrs={'class': 'form-control'}))

class CorrenteForm(forms.Form):
	value = forms.IntegerField(required=True, label=u'Valor', widget=forms.TextInput(attrs={'class': 'form-control'}))
	
class ICCForm(forms.Form):
	value = forms.FloatField(required=True, label=u'Valor - use ponto para decimal', widget=forms.TextInput(attrs={'class': 'form-control'}))
	
class FormaConstrutivaForm(forms.Form):
	value = forms.CharField(label='Valor',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class GraudeProtecaoForm(forms.Form):
	value = forms.CharField(label='Valor',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class FornecedoresForm(forms.Form):
	name = forms.CharField(label='Nome',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
	brand = forms.CharField(label='Marca',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class ClienteForm(forms.Form):
	name = forms.CharField(label='Nome',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
	cpf_cnpj = forms.CharField(label='CPF/CNPJ',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class VendedorForm(forms.Form):
	name = forms.CharField(label='Nome',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

class ComponenteForm(forms.Form):
	corrente_list = list()
	corrente_response = Corrente.objects.all()
	corrente_response = corrente_response.values('value')
	corrente_options = get_value(corrente_list, corrente_response)

	supplier_list = list()
	supplier_response = Fornecedores.objects.all()
	supplier_response = supplier_response.values('name')
	supplier_options = get_name(supplier_list, supplier_response)

	tensao_list = list()
	tensao_response = Tensao.objects.all()
	tensao_response = tensao_response.values('value')
	tensao_options = get_value(tensao_list, tensao_response)

	icc_list = list()
	icc_response = ICC.objects.all()
	icc_response = icc_response.values('value')
	icc_options = get_value(icc_list, icc_response)

	suppliername = forms.ChoiceField(label='Nome do Fornecedor',choices=supplier_options,widget=forms.Select(attrs={'class': 'form-control'}))
	prodline = forms.CharField(label='Linha de Producao',required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	# corrente = forms.ChoiceField(label='Corrente',choices=[('-', u'-')],widget=forms.Select(attrs={'class': 'form-control'}))
	corrente = forms.ChoiceField(label='Corrente',choices=corrente_options,widget=forms.Select(attrs={'class': 'form-control'}))
	tensao = forms.ChoiceField(label='Tensão',choices=tensao_options,widget=forms.Select(attrs={'class': 'form-control'}))
	altura = forms.IntegerField(required=True, label=u'Altura (cm)', widget=forms.TextInput(attrs={'class': 'form-control'}))
	largura = forms.IntegerField(required=True, label=u'Largura (cm)', widget=forms.TextInput(attrs={'class': 'form-control'}))
	profundidade = forms.IntegerField(required=True, label=u'Profundidade (cm)', widget=forms.TextInput(attrs={'class': 'form-control'}))
	peso = forms.FloatField(required=True, label=u'Peso (Kg) - use ponto para decimal', widget=forms.TextInput(attrs={'class': 'form-control'}))
	icc127 = forms.ChoiceField(label='ICC 127',choices=icc_options,widget=forms.Select(attrs={'class': 'form-control'}))
	icc220 = forms.ChoiceField(label='ICC 220',choices=icc_options,widget=forms.Select(attrs={'class': 'form-control'}))
	icc380 = forms.ChoiceField(label='ICC 380',choices=icc_options,widget=forms.Select(attrs={'class': 'form-control'}))
	icc440 = forms.ChoiceField(label='ICC 440',choices=icc_options,widget=forms.Select(attrs={'class': 'form-control'}))
	icc480 = forms.ChoiceField(label='ICC 480',choices=icc_options,widget=forms.Select(attrs={'class': 'form-control'}))
	

