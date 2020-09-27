from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User, Permission
from django.conf import settings
import requests, json
from armarios_system.models import Obra, Armario
from materials_system.models import Cliente, Vendedor, ICC, Tensao, FormaConstrutiva, GraudeProtecao, Componente

def get_name(objs, response):
	for obj in response:
		objs.append((obj[u'name'], obj['name']))
	return objs

def get_value(objs, response):
	for obj in response:
		objs.append((obj[u'value'], obj['value']))
	return objs

def get_prodline(objs, response):
	for obj in response:
		objs.append((obj[u'prodline'], obj['prodline']))
	return objs

def get_armario(objs, response):
	for obj in response:
		objs.append((obj[u'id'], 'Id: ' + str(obj['id']) + ' - Vendedor: ' + obj['vendedor'] + ' - Cliente: ' + obj['cliente']+ ' - Data: ' + str(obj['date'])))
	return objs
	
class ObraForm(forms.Form):
	cliente_list = list()
	cliente_response = Cliente.objects.filter(deleted_flag=False)
	try:
		cliente_response = cliente_response.values('name')
		cliente_options = get_name(cliente_list, cliente_response)
	except:
		cliente_list.append((cliente_response.name, cliente_response.name))
		cliente_options = cliente_list

	vendedor_list = list()
	vendedor_response = Vendedor.objects.filter(deleted_flag=False)
	try:
		vendedor_response = vendedor_response.values('name')
		vendedor_options = get_name(vendedor_list, vendedor_response)
	except:
		vendedor_list.append((vendedor_response.name, vendedor_response.name))
		vendedor_options = vendedor_list

	vendedor = forms.ChoiceField(label='Vendedor',choices=vendedor_options,widget=forms.Select(attrs={'class': 'form-control'}))
	cliente = forms.ChoiceField(label='Cliente',choices=cliente_options,widget=forms.Select(attrs={'class': 'form-control'}))

class ArmarioForm(forms.Form):
	linha_list = list()
	linha_response = Componente.objects.filter(deleted_flag=False)
	try:
		linha_response = linha_response.values('prodline')
		linha_options = get_prodline(linha_list, linha_response)
	except:
		linha_list.append((linha_response.prodline, linha_response.prodline))
		linha_options = linha_list

	tensao_list = list()
	tensao_response = Tensao.objects.filter(deleted_flag=False)
	try:
		tensao_response = tensao_response.values('value')
		tensao_options = get_value(tensao_list, tensao_response)
	except:
		tensao_list.append((tensao_response.value, tensao_response.value))
		tensao_options = tensao_list

	graudeprotecao_list = list()
	graudeprotecao_response = GraudeProtecao.objects.filter(deleted_flag=False)
	try:
		graudeprotecao_response = graudeprotecao_response.values('value')
		graudeprotecao_options = get_value(graudeprotecao_list, graudeprotecao_response)
	except:
		graudeprotecao_list.append((graudeprotecao_response.value, graudeprotecao_response.value))
		graudeprotecao_options = graudeprotecao_list

	icc_list = list()
	icc_response = ICC.objects.filter(deleted_flag=False)
	try:
		icc_response = icc_response.values('value')
		icc_options = get_value(icc_list, icc_response)
	except:
		icc_list.append((icc_response.value, icc_response.value))
		icc_options = icc_list

	formaconstrutiva_list = list()
	formaconstrutiva_response = FormaConstrutiva.objects.filter(deleted_flag=False)
	try:
		formaconstrutiva_response = formaconstrutiva_response.values('value')
		formaconstrutiva_options = get_value(formaconstrutiva_list, formaconstrutiva_response)
	except:
		formaconstrutiva_list.append((formaconstrutiva_response.value, formaconstrutiva_response.value))
		formaconstrutiva_options = formaconstrutiva_list

	linha = forms.ChoiceField(label='Linha',choices=linha_options,widget=forms.Select(attrs={'class': 'form-control'}))
	tensao = forms.ChoiceField(label='Tensão',choices=tensao_options,widget=forms.Select(attrs={'class': 'form-control'}))
	graudeprotecao = forms.ChoiceField(label='Grau de Protecão',choices=graudeprotecao_options,widget=forms.Select(attrs={'class': 'form-control'}))
	instalacao = forms.ChoiceField(label='Instalacão',choices=[(u"abrigado", "Abrigado"), (u"aotempo", "Ao Tempo")],widget=forms.Select(attrs={'class': 'form-control'}))
	icc = forms.ChoiceField(label='ICC',choices=icc_options,widget=forms.Select(attrs={'class': 'form-control'}))
	formaconstrutiva = forms.ChoiceField(label='Forma Construtiva',choices=formaconstrutiva_options,widget=forms.Select(attrs={'class': 'form-control'}))
	chapa = forms.ChoiceField(label='Chapa',choices=[(u"12", "12#"), (u"14", "14#"), (u"16", "16#")],widget=forms.Select(attrs={'class': 'form-control'}))