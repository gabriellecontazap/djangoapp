from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import ClienteForm
from materials_system.models import Cliente
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse


class ClienteListView(ListView):
	template_name = 'materials_system/cliente_list.html'
	context_object_name = 'clientes'

	def get_queryset(self):
		queryset = Cliente.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ClienteListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Cliente'
		context['create_link'] = reverse("cliente_create")
		return context

class ClienteCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = ClienteForm

	def get_context_data(self, **kwargs):
		context = super(ClienteCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'Cliente'
		context['form_title'] = 'Criar Cliente'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("cliente_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Cliente(
		  name= request.POST['name'],
		  cpf_cnpj= request.POST['cpf_cnpj'],
		  deleted_flag=False
		)
		values.save()
		return HttpResponseRedirect(reverse_lazy("cliente_list"))

class ClienteRemoveView(RedirectView):
	pk_url_kwarg = 'cliente_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = Cliente.objects.get(pk=kwargs['cliente_pk'])
		values.deleted_flag = True
		values.save()
		self.url = reverse_lazy("cliente_list")
		return super(ClienteRemoveView, self).get_redirect_url(*args, **kwargs)

class ClienteUpdateView(TemplateView):
	template_name = 'materials_system/form.html'
	pk_url_kwarg = 'cliente_pk' # Nome da pk na url

	def get_initial(self):
		values = Cliente.objects.get(pk=self.kwargs['cliente_pk'])
		initial = {}
		initial.update({'name': values.name, 'cpf_cnpj': values.cpf_cnpj})
		return initial

	def get_context_data(self, **kwargs):
		context = super(ClienteUpdateView, self).get_context_data(**kwargs)
		pk = self.kwargs['cliente_pk']
		context['page_title'] = 'Editar Cliente'
		context['form_title'] = 'Editar Cliente'
		context['form_button'] = 'Salvar'
		context['editable'] = True
		context['form'] = ClienteForm(self.get_initial())
		context['initial'] = self.get_initial()
		context['action_link'] = reverse("cliente_edit", kwargs={'cliente_pk': self.kwargs['cliente_pk']})
		context['back_link'] = reverse("cliente_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Cliente.objects.get(pk=self.kwargs['cliente_pk'])
		values.name = request.POST['name']
		values.cpf_cnpj = request.POST['cpf_cnpj']
		values.save()
		return HttpResponseRedirect(reverse_lazy("cliente_list"))
