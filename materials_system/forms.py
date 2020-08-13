from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User, Permission
from django.conf import settings
import requests, json


class TensaoForm(forms.Form):
	value = forms.IntegerField(required=True, label=u'Valor', widget=forms.TextInput(attrs={'class': 'form-control'}))

class CorrenteForm(forms.Form):
	value = forms.IntegerField(required=True, label=u'Valor', widget=forms.TextInput(attrs={'class': 'form-control'}))
	
class FabricantesForm(forms.Form):
	name = forms.CharField(label='Nome',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
	brand = forms.CharField(label='Marca',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
	
class LinhadeProducaoForm(forms.Form):
	brand = forms.CharField(label='Marca',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
	prodline = forms.CharField(label='Linha de Producão',required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
	