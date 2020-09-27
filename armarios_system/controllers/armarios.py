from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from armarios_system.models import Armario, Coluna
from materials_system.models import Componente
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
import json
from armarios_system.forms import ArmarioForm

class ArmariosListView(ListView):
	template_name = 'armarios_system/armarios_list.html'
	context_object_name = 'armarios'

	def get_queryset(self):
		queryset = Armario.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		path = self.request.get_full_path()
		path = path.split('/')
		path = path[2]
		queryset = queryset.filter(obra=path)
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ArmariosListView, self).get_context_data(**kwargs)
		context['list_title'] = 'Lista de Armarios'
		path = self.request.get_full_path()
		path = path.split('/')
		path = path[2]
		context['obra_pk'] = path
		context['create_link'] = reverse('armarios_create', args=(path))
		return context

class ArmariosFullListView(ListView):
	template_name = 'armarios_system/armariosfull_list.html'
	context_object_name = 'colunas'

	def get_queryset(self):
		queryset = Coluna.objects.all()
		queryset = queryset.filter(deleted_flag=False)
		path = self.request.get_full_path()
		path = path.split('/')
		path = path[3]
		queryset = queryset.filter(armario=path)
		queryset = list(queryset.values())
		k = 0
		for query in queryset:
			query['dadoscomponente'] = []
			query['barrageralhorkzontalid'] = 'GeralHor' + str(k)
			query['barraneutroid'] = 'Neutro' + str(k)
			query['barraterraid'] = 'Terra' + str(k)
			k = k+1
			ids = query['componentes']
			ids = ids.split("-")
			j = 0
			for i in ids:
				componente = Componente.objects.get(pk=i)
				dadoscomponente = {'componenteID': 'Coluna'+str(k)+'Componente'+str(j), 'id': componente.id, 'prodline': componente.prodline, 'corrente': componente.corrente, 'tensao':componente.tensao,'altura':componente.altura,'largura':componente.largura, 'profundidade':componente.profundidade, 'peso':componente.peso}
				query['dadoscomponente'].append(dadoscomponente)
		# queryset['dadoscomponente'] = pd.DataFrame(queryset['dadoscomponente'], columns=['id', 'prodline', 'corrente', 'tensao', 'altura', 'largura', 'profundidade', 'peso'])
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ArmariosFullListView, self).get_context_data(**kwargs)
		path = self.request.get_full_path()
		path = path.split('/')
		path = path[3]
		context['list_title'] = 'Lista de Colunas do Armario #' + str(path)
		context['armario_pk'] = path
		context['create_link'] = reverse('armarios_create', args=(path))
		return context

class ArmarioColunaRemoveView(RedirectView):
	pk_url_kwarg = 'coluna_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = Coluna.objects.get(pk=kwargs['coluna_pk'])
		values.deleted_flag = True
		values.save()
		path = self.request.get_full_path()
		path = path.split('/')
		path = path[3]
		self.url = reverse('armario_columns_list', args=(path))
		return super(ArmarioColunaRemoveView, self).get_redirect_url(*args, **kwargs)


class ArmariosRemoveView(RedirectView):
	pk_url_kwarg = 'armario_pk' # Nome da pk na url
	permanent = False

	def get_redirect_url(self, *args, **kwargs):
		values = Armario.objects.get(pk=kwargs['armario_pk'])
		values.deleted_flag = True
		values.save()
		path = self.request.get_full_path()
		path = path.split('/')
		path = path[2]
		self.url = reverse('armarios_list', args=(path))
		return super(ArmariosRemoveView, self).get_redirect_url(*args, **kwargs)

class ArmariosCreateView(FormView):
	template_name = 'materials_system/form.html'
	form_class = ArmarioForm

	def get_context_data(self, **kwargs):
		context = super(ArmariosCreateView, self).get_context_data(**kwargs)
		context['page_title'] = 'Armario'
		context['form_title'] = 'Criar Armario'
		context['form_button'] = 'Criar'
		context['editable'] = True
		path = self.request.get_full_path()
		path = path.split('/')
		path = path[2]
		context['back_link'] = reverse('armarios_list', args=(path))
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		path = self.request.get_full_path()
		path = path.split('/')
		path = path[2]
		values = Armario(
		  linha= request.POST['linha'],
		  obra= path,
		  tensao= request.POST['tensao'],
		  graudeprotecao= request.POST['graudeprotecao'],
		  instalacao= request.POST['instalacao'],
		  icc= request.POST['icc'],
		  formaconstrutiva= request.POST['formaconstrutiva'],
		  chapa= request.POST['chapa'],
		  deleted_flag=False
		)
		values.save()
		return HttpResponseRedirect(reverse_lazy('armarios_list', args=(path)))

class ColunaCreateIView(TemplateView):
	template_name = 'materials_system/form.html'
	pk_url_kwarg = 'componente_pk' # Nome da pk na url

	def get_initial(self):
		values = Componente.objects.get(pk=self.kwargs['componente_pk'])
		initial = {}
		initial.update({'suppliername': values.suppliername,
			'prodline': values.prodline,
			'corrente': values.corrente,
			'tensao': values.tensao,
			'altura': values.altura,
			'largura': values.largura,
			'profundidade': values.profundidade,
			'peso': values.peso,
			'icc127': values.icc127,
			'icc220': values.icc220,
			'icc380': values.icc380,
			'icc440': values.icc440,
			'icc480': values.icc480})
		return initial

	def get_context_data(self, **kwargs):
		context = super(ComponenteUpdateView, self).get_context_data(**kwargs)
		pk = self.kwargs['componente_pk']
		context['page_title'] = 'Editar Componente'
		context['form_title'] = 'Editar Componente'
		context['form_button'] = 'Salvar'
		context['editable'] = True
		context['form'] = ComponenteForm(self.get_initial())
		context['initial'] = self.get_initial()
		context['action_link'] = reverse("componente_edit", kwargs={'componente_pk': self.kwargs['componente_pk']})
		context['back_link'] = reverse("componente_list")
		context['back_button'] = "Voltar"
		return context

	def post(self, request, *args, **kwargs):
		values = Componente.objects.get(pk=self.kwargs['componente_pk'])
		values.suppliername= request.POST['suppliername']
		values.prodline= request.POST['prodline']
		values.corrente= request.POST['corrente']
		values.tensao= request.POST['tensao']
		values.altura= request.POST['altura']
		values.largura= request.POST['largura']
		values.profundidade= request.POST['profundidade']
		values.peso= request.POST['peso']
		values.icc127= request.POST['icc127']
		values.icc220= request.POST['icc220']
		values.icc380= request.POST['icc380']
		values.icc440= request.POST['icc440']
		values.icc480= request.POST['icc480']
		values.save()
		return HttpResponseRedirect(reverse_lazy("componente_list"))
