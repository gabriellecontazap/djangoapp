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

class ICC(models.Model):
	value = models.FloatField()
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.value

class FormaConstrutiva(models.Model):
	value = models.CharField(max_length=255, null=False, blank=False)
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.value

class GraudeProtecao(models.Model):
	value = models.CharField(max_length=255, null=False, blank=False)
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.value

class Fornecedores(models.Model):
	name = models.CharField(max_length=255, null=False, blank=False)
	brand = models.CharField(max_length=255, null=False, blank=False)
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Cliente(models.Model):
	name = models.CharField(max_length=255, null=False, blank=False)
	cpf_cnpj = models.CharField(max_length=255, null=False, blank=False)
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Vendedor(models.Model):
	name = models.CharField(max_length=255, null=False, blank=False)
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Componente(models.Model):
	suppliername = models.CharField(max_length=255, null=False, blank=False)
	prodline = models.CharField(max_length=255, null=False, blank=False)
	corrente = models.IntegerField()
	tensao = models.IntegerField()
	altura = models.IntegerField()
	largura = models.IntegerField()
	profundidade = models.IntegerField()
	peso = models.FloatField()
	icc127 = models.FloatField()
	icc220 = models.FloatField()
	icc380 = models.FloatField()
	icc440 = models.FloatField()
	icc480 = models.FloatField()
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.suppliername

