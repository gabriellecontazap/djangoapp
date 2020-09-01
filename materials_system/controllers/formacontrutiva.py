from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import FormaConstrutivaForm
from materials_system.models import FormaConstrutiva
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse

class FormaConstrutivaListView(ListView):
	template_name = 'materials_system/formaconstrutiva_list.html'
	context_object_name = 'formas'

	def get_queryset(self):
		queryset = FormaConstrutiva.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(FormaConstrutivaListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Formas Construtivas'
		context['create_link'] = reverse("formaconstrutiva_create")
		return context

class FormaConstrutivaCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = FormaConstrutivaForm

	def get_context_data(self, **kwargs):
		context = super(FormaConstrutivaCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'Forma Construtiva'
		context['form_title'] = 'Criar Forma Construtiva'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("formaconstrutiva_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = FormaConstrutiva(
		  value= request.POST['value'],
		  deleted_flag=False
		)
		values.save()

		return HttpResponseRedirect(reverse_lazy("formaconstrutiva_list"))

class FormaRemoveView(RedirectView):
	pk_url_kwarg = 'forma_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = FormaConstrutiva.objects.get(pk=kwargs['forma_pk'])
		values.deleted_flag = True
		values.save()
		self.url = reverse_lazy("formaconstrutiva_list")
		return super(FormaRemoveView, self).get_redirect_url(*args, **kwargs)
