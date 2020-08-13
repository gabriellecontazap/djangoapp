from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import FabricantesForm
from materials_system.models import Fabricantes
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse


class FabricantesListView(ListView):
	template_name = 'materials_system/fabricantes_list.html'
	context_object_name = 'fabricantes'

	def get_queryset(self):
		queryset = Fabricantes.objects.all()
		return queryset

	def get_context_data(self, **kwargs):
		context = super(FabricantesListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Fabricantes'
		context['create_link'] = reverse("fabricantes_create")
		return context

class FabricantesCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = FabricantesForm

	def get_context_data(self, **kwargs):
		context = super(FabricantesCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'Fabricantes'
		context['form_title'] = 'Criar Fabricante'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("fabricantes_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Fabricantes(
		  name= request.POST['name'],
		  brand= request.POST['brand'],
		  deleted_flag=False
		)
		values.save()
		return HttpResponseRedirect(reverse_lazy("fabricantes_list"))
