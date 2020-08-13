from rest_framework import routers, serializers
from register.models import Tensao
from django.db.models import Prefetch

class Tensao(serializers.ModelSerializer):
	def __init__(self, *args, **kwargs):
		super(TensaoSerializer, self).__init__(*args, **kwargs)
		request = self.context.get("request")
		if request and request.query_params.get('fields'):
			fields = request.query_params.get('fields')
			if fields:
				fields = fields.split(',')
				allowed = set(fields)
				existing = set(self.fields.keys())
	class Meta:
		model = TensaoAutomatic
		fields = '__all__'