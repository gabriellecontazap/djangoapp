from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import TensaoForm
from materials_system.models import Tensao
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse

class TensaoListView(ListView):
	template_name = 'materials_system/tensao_list.html'
	context_object_name = 'tensoes'

	def get_queryset(self):
		queryset = Tensao.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(TensaoListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Tensões'
		context['create_link'] = reverse("tensao_create")
		return context

class TensaoCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = TensaoForm

	def get_context_data(self, **kwargs):
		context = super(TensaoCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'Tensões'
		context['form_title'] = 'Criar Tensão'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("tensao_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Tensao(
		  value= request.POST['value'],
		  deleted_flag=False
		)
		values.save()

		return HttpResponseRedirect(reverse_lazy("tensao_list"))

class TensaoRemoveView(RedirectView):
	pk_url_kwarg = 'tensao_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = Tensao.objects.get(pk=kwargs['tensao_pk'])
		values.deleted_flag = True
		values.save()
		self.url = reverse_lazy("tensao_list")
		return super(TensaoRemoveView, self).get_redirect_url(*args, **kwargs)
