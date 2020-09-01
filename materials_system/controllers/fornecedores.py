from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import FornecedoresForm
from materials_system.models import Fornecedores
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
import json

class FornecedoresListView(ListView):
	template_name = 'materials_system/fornecedores_list.html'
	context_object_name = 'fornecedores'

	def get_queryset(self):
		queryset = Fornecedores.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(FornecedoresListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Fornecedores'
		context['create_link'] = reverse("fornecedores_create")
		return context

class FornecedoresCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = FornecedoresForm

	def get_context_data(self, **kwargs):
		context = super(FornecedoresCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'Fornecedores'
		context['form_title'] = 'Criar Fornecedor'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("fornecedores_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Fornecedores(
		  name= request.POST['name'],
		  brand= request.POST['brand'],
		  deleted_flag=False
		)
		values.save()
		return HttpResponseRedirect(reverse_lazy("fornecedores_list"))

class FornecedoresRemoveView(RedirectView):
	pk_url_kwarg = 'fornecedor_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = Fornecedores.objects.get(pk=kwargs['fornecedor_pk'])
		values.deleted_flag = True
		values.save()
		self.url = reverse_lazy("fornecedores_list")
		return super(FornecedoresRemoveView, self).get_redirect_url(*args, **kwargs)

class FornecedoresUpdateView(TemplateView):
	template_name = 'materials_system/form.html'
	pk_url_kwarg = 'fornecedor_pk' # Nome da pk na url

	def get_initial(self):
		values = Fornecedores.objects.get(pk=self.kwargs['fornecedor_pk'])
		initial = {}
		initial.update({'name': values.name,
			'brand': values.brand})
		return initial

	def get_context_data(self, **kwargs):
		context = super(FornecedoresUpdateView, self).get_context_data(**kwargs)
		pk = self.kwargs['fornecedor_pk']
		context['page_title'] = 'Editar Fornecedor'
		context['form_title'] = 'Editar Fornecedor'
		context['form_button'] = 'Salvar'
		context['editable'] = True
		context['form'] = FornecedoresForm(self.get_initial())
		context['initial'] = self.get_initial()
		context['action_link'] = reverse("fornecedores_edit", kwargs={'fornecedor_pk': self.kwargs['fornecedor_pk']})
		context['back_link'] = reverse("fornecedores_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Fornecedores.objects.get(pk=self.kwargs['fornecedor_pk'])
		values.name = request.POST['name']
		values.brand = request.POST['brand']
		values.save()
		return HttpResponseRedirect(reverse_lazy("fornecedores_list"))
