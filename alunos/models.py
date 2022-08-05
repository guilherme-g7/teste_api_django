from django.db import models

# Create your models here.
class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=10)
    nome = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    