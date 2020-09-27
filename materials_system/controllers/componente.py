from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import ComponenteForm
from materials_system.models import Componente
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
import json

class ComponenteListView(ListView):
	template_name = 'materials_system/componente_list.html'
	context_object_name = 'componentes'

	def get_queryset(self):
		queryset = Componente.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ComponenteListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Componente'
		context['create_link'] = reverse("componente_create")
		return context

class ComponenteCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = ComponenteForm

	def get_context_data(self, **kwargs):
		context = super(ComponenteCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'Componente'
		context['form_title'] = 'Criar Componente'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("componente_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Componente(
		  suppliername= request.POST['suppliername'],
		  prodline= request.POST['prodline'],
		  corrente= request.POST['corrente'],
		  tensao= request.POST['tensao'],
		  altura= request.POST['altura'],
		  largura= request.POST['largura'],
		  profundidade= request.POST['profundidade'],
		  peso= request.POST['peso'],
		  icc127= request.POST['icc127'],
		  icc220= request.POST['icc220'],
		  icc380= request.POST['icc380'],
		  icc440= request.POST['icc440'],
		  icc480= request.POST['icc480'],
		  deleted_flag=False
		)
		values.save()
		return HttpResponseRedirect(reverse_lazy("componente_list"))

class ComponenteRemoveView(RedirectView):
	pk_url_kwarg = 'componente_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = Componente.objects.get(pk=kwargs['componente_pk'])
		values.deleted_flag = True
		values.save()
		self.url = reverse_lazy("componente_list")
		return super(ComponenteRemoveView, self).get_redirect_url(*args, **kwargs)

class ComponenteUpdateView(TemplateView):
	template_name = 'materials_system/form.html'
	pk_url_kwarg = 'componente_pk' # Nome da pk na url

	def get_initial(self):
		values = Componente.objects.get(pk=self.kwargs['componente_pk'])
		initial = {}
		initial.update({'suppliername': values.suppliername,
			'prodline': values.prodline,
			'corrente': values.corrente,
			'tensao': values.tensao,
			'altura': values.altura,
			'largura': values.largura,
			'profundidade': values.profundidade,
			'peso': values.peso,
			'icc127': values.icc127,
			'icc220': values.icc220,
			'icc380': values.icc380,
			'icc440': values.icc440,
			'icc480': values.icc480})
		return initial

	def get_context_data(self, **kwargs):
		context = super(ComponenteUpdateView, self).get_context_data(**kwargs)
		pk = self.kwargs['componente_pk']
		context['page_title'] = 'Editar Componente'
		context['form_title'] = 'Editar Componente'
		context['form_button'] = 'Salvar'
		context['editable'] = True
		context['form'] = ComponenteForm(self.get_initial())
		context['initial'] = self.get_initial()
		context['action_link'] = reverse("componente_edit", kwargs={'componente_pk': self.kwargs['componente_pk']})
		context['back_link'] = reverse("componente_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Componente.objects.get(pk=self.kwargs['componente_pk'])
		values.suppliername= request.POST['suppliername']
		values.prodline= request.POST['prodline']
		values.corrente= request.POST['corrente']
		values.tensao= request.POST['tensao']
		values.altura= request.POST['altura']
		values.largura= request.POST['largura']
		values.profundidade= request.POST['profundidade']
		values.peso= request.POST['peso']
		values.icc127= request.POST['icc127']
		values.icc220= request.POST['icc220']
		values.icc380= request.POST['icc380']
		values.icc440= request.POST['icc440']
		values.icc480= request.POST['icc480']
		values.save()
		return HttpResponseRedirect(reverse_lazy("componente_list"))
