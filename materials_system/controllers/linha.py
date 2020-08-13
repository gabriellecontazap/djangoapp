from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import LinhadeProducaoForm
from materials_system.models import LinhadeProducao
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse


class LinhaListView(ListView):
	template_name = 'materials_system/linhadeprod.html'
	context_object_name = 'prodlines'

	def get_queryset(self):
		queryset = LinhadeProducao.objects.all()
		return queryset

	def get_context_data(self, **kwargs):
		context = super(LinhaListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Linhas de Producão'
		context['create_link'] = reverse("linha_create")
		return context

class LinhaCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = LinhadeProducaoForm

	def get_context_data(self, **kwargs):
		context = super(LinhaCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'Linhas de Producão'
		context['form_title'] = 'Criar Linhas de Producão'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("linha_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = LinhadeProducao(
		  brand= request.POST['brand'],
		  prodline= request.POST['prodline'],
		  deleted_flag=False
		)
		values.save()

		return HttpResponseRedirect(reverse_lazy("linha_list"))
