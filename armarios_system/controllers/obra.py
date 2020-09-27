from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from armarios_system.models import Obra
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from armarios_system.forms import ObraForm

class ObraListView(ListView):
	template_name = 'armarios_system/obras_list.html'
	context_object_name = 'obras'

	def get_queryset(self):
		queryset = Obra.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ObraListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Obras'
		context['create_link'] = reverse("obras_create")
		return context

class ObraRemoveView(RedirectView):
	pk_url_kwarg = 'obra_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = Obra.objects.get(pk=kwargs['obra_pk'])
		values.deleted_flag = True
		values.save()
		self.url = reverse_lazy("obras_list")
		return super(ObraRemoveView, self).get_redirect_url(*args, **kwargs)

class ObraCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = ObraForm

	def get_context_data(self, **kwargs):
		context = super(ObraCreateView, self).get_context_data(**kwargs)
		context['page_title'] = 'Obras'
		context['form_title'] = 'Criar Obras'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("obras_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Obra(
		  vendedor= request.POST['vendedor'],
		  cliente= request.POST['cliente'],
		  date= datetime.now().strftime("%Y-%m-%d"),
		  deleted_flag=False
		)
		values.save()
		return HttpResponseRedirect(reverse_lazy("obras_list"))
