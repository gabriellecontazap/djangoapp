from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import VendedorForm
from materials_system.models import Vendedor
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse


class VendedorListView(ListView):
	template_name = 'materials_system/vendedor_list.html'
	context_object_name = 'vendedores'

	def get_queryset(self):
		queryset = Vendedor.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(VendedorListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Vendedor'
		context['create_link'] = reverse("vendedor_create")
		return context

class VendedorCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = VendedorForm

	def get_context_data(self, **kwargs):
		context = super(VendedorCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'Vendedor'
		context['form_title'] = 'Criar Vendedor'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("vendedor_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Vendedor(
		  name= request.POST['name'],
		  deleted_flag=False
		)
		values.save()
		return HttpResponseRedirect(reverse_lazy("vendedor_list"))

class VendedorRemoveView(RedirectView):
	pk_url_kwarg = 'vendedor_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = Vendedor.objects.get(pk=kwargs['vendedor_pk'])
		values.deleted_flag = True
		values.save()
		self.url = reverse_lazy("vendedor_list")
		return super(VendedorRemoveView, self).get_redirect_url(*args, **kwargs)

class VendedorUpdateView(TemplateView):
	template_name = 'materials_system/form.html'
	pk_url_kwarg = 'vendedor_pk' # Nome da pk na url

	def get_initial(self):
		values = Vendedor.objects.get(pk=self.kwargs['vendedor_pk'])
		initial = {}
		initial.update({'name': values.name})
		return initial

	def get_context_data(self, **kwargs):
		context = super(VendedorUpdateView, self).get_context_data(**kwargs)
		pk = self.kwargs['vendedor_pk']
		context['page_title'] = 'Editar Vendedor'
		context['form_title'] = 'Editar Vendedor'
		context['form_button'] = 'Salvar'
		context['editable'] = True
		context['form'] = VendedorForm(self.get_initial())
		context['initial'] = self.get_initial()
		context['action_link'] = reverse("vendedor_edit", kwargs={'vendedor_pk': self.kwargs['vendedor_pk']})
		context['back_link'] = reverse("vendedor_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Vendedor.objects.get(pk=self.kwargs['vendedor_pk'])
		values.name = request.POST['name']
		values.save()
		return HttpResponseRedirect(reverse_lazy("vendedor_list"))
