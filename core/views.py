from django.shortcuts import render
from django.views.generic import FormView, RedirectView, TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View

# # Create your views here.
# class HomeView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super(HomeView, self).get_context_data(**kwargs)
#         context['page_title'] = 'Oráculo'
#         context['menu_navbar'] = self.menu
#         context['system_menu'] = self.get_ordered_system_menu()
#         # Setup inicial para o login do google      
#         return context