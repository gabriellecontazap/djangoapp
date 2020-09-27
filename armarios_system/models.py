from django.db import models

# Create your models here.
class Obra(models.Model):
	vendedor = models.CharField(max_length=255, null=False, blank=False)
	cliente = models.CharField(max_length=255, null=False, blank=False)
	date = models.DateField(null=True, blank=True)
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.vendedor

class Armario(models.Model):
	obra = models.IntegerField()
	colunas = models.CharField(max_length=255, null=False, blank=False)
	linha = models.CharField(max_length=255, null=False, blank=False)
	tensao = models.IntegerField()
	graudeprotecao = models.CharField(max_length=255, null=False, blank=False)
	instalacao = models.CharField(max_length=100, null=False, blank=False)
	icc = models.FloatField()
	formaconstrutiva = models.CharField(max_length=100, null=False, blank=False)
	chapa = models.CharField(max_length=100, null=False, blank=False)
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.obra

class Coluna(models.Model):
	armario = models.IntegerField()
	componentes = models.CharField(max_length=1000, null=False, blank=False)
	barrageralhorizontal = models.IntegerField()
	barrageralvertical = models.IntegerField()
	barraneutro = models.IntegerField()
	barraterra = models.IntegerField()
	largura = models.IntegerField()
	deleted_flag = models.BooleanField(default=False)

	def __str__(self):
		return self.armario