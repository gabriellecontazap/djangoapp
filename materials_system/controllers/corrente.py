from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import CorrenteForm
from materials_system.models import Corrente
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse


class CorrenteListView(ListView):
	template_name = 'materials_system/corrente_list.html'
	context_object_name = 'correntes'

	def get_queryset(self):
		queryset = Corrente.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(CorrenteListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Correntes'
		context['create_link'] = reverse("corrente_create")
		return context

class CorrenteCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = CorrenteForm

	def get_context_data(self, **kwargs):
		context = super(CorrenteCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'Correntes'
		context['form_title'] = 'Criar Corrente'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("corrente_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Corrente(
		  value= request.POST['value'],
		  deleted_flag=False
		)
		values.save()
		return HttpResponseRedirect(reverse_lazy("corrente_list"))

class CorrenteRemoveView(RedirectView):
	pk_url_kwarg = 'corrente_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = Corrente.objects.get(pk=kwargs['corrente_pk'])
		values.deleted_flag = True
		values.save()
		self.url = reverse_lazy("corrente_list")
		return super(CorrenteRemoveView, self).get_redirect_url(*args, **kwargs)
