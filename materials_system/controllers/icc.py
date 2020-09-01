from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import ICCForm
from materials_system.models import ICC
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

class ICCListView(ListView):
	template_name = 'materials_system/icc_list.html'
	context_object_name = 'icc'

	def get_queryset(self):
		queryset = ICC.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ICCListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de ICC'
		context['create_link'] = reverse("icc_create")
		return context

class ICCCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = ICCForm

	def get_context_data(self, **kwargs):
		context = super(ICCCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'ICC'
		context['form_title'] = 'Criar ICC'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("icc_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = ICC(
		  value= request.POST['value'],
		  deleted_flag=False
		)
		values.save()
		return HttpResponseRedirect(reverse_lazy("icc_list"))

class ICCRemoveView(RedirectView):
	pk_url_kwarg = 'icc_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = ICC.objects.get(pk=kwargs['icc_pk'])
		values.deleted_flag = True
		values.save()
		self.url = reverse_lazy("icc_list")
		return super(ICCRemoveView, self).get_redirect_url(*args, **kwargs)
