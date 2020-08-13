from django.db import models

# Create your models here.

class Tensao(models.Model):
	value = models.IntegerField()
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.value

class Corrente(models.Model):
	value = models.IntegerField()
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.value

class Fabricantes(models.Model):
	name = models.CharField(max_length=255, null=False, blank=False)
	brand = models.CharField(max_length=255, null=False, blank=False)
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class LinhadeProducao(models.Model):
	brand = models.CharField(max_length=255, null=False, blank=False)
	prodline = models.CharField(max_length=255, null=False, blank=False)
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.brand

class Componente(models.Model):
	suppliername = models.CharField(max_length=255, null=False, blank=False)
	prodline = models.CharField(max_length=255, null=False, blank=False)
	corrente = models.IntegerField()
	icc127 = models.IntegerField()
	icc220 = models.IntegerField()
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.suppliername

