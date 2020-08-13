# from serializer import TensaoSerializer
# from register.models import TensaoAutomatic
# from django.db.models import Max, Q
# from django.db.models.query import QuerySet
# from rest_framework import viewsets

# class TensaoViewSet(viewsets.ModelViewSet):
# 	model = TensaoAutomatic
# 	queryset = model.objects.all()
# 	serializer_class = TensaoSerializer
# 	pagination_class = None
# 	http_method_names = ['get', 'post',  'patch',  'head', 'options'] 
  
# 	def get_queryset(self):
# 		return queryset