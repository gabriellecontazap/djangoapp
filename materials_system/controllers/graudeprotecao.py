from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from materials_system.forms import GraudeProtecaoForm
from materials_system.models import GraudeProtecao
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse

class GraudeProtecaoListView(ListView):
	template_name = 'materials_system/graudeprotecao_list.html'
	context_object_name = 'graus'

	def get_queryset(self):
		queryset = GraudeProtecao.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(GraudeProtecaoListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Grau de Protecao'
		context['create_link'] = reverse("graudeprotecao_create")
		return context

class GraudeProtecaoCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = GraudeProtecaoForm

	def get_context_data(self, **kwargs):
		context = super(GraudeProtecaoCreateView, self).get_context_data(**kwargs)
		context['choice_label'] = 'Nome'
		context['page_title'] = 'Grau de Protecao'
		context['form_title'] = 'Criar Grau de Protecao'
		context['form_button'] = 'Criar'
		context['editable'] = True
		context['back_link'] = reverse("graudeprotecao_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = GraudeProtecao(
		  value= request.POST['value'],
		  deleted_flag=False
		)
		values.save()

		return HttpResponseRedirect(reverse_lazy("graudeprotecao_list"))

class GrauRemoveView(RedirectView):
	pk_url_kwarg = 'grau_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = GraudeProtecao.objects.get(pk=kwargs['grau_pk'])
		values.deleted_flag = True
		values.save()
		self.url = reverse_lazy("graudeprotecao_list")
		return super(GrauRemoveView, self).get_redirect_url(*args, **kwargs)
