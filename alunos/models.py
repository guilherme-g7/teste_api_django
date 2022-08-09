from django.db import models


# Create your models here.
class Materia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    codigo = models.IntegerField()
    descr_materia = models.CharField(max_length=500)
    horas = models.IntegerField()
    creditos = models.IntegerField()
    situacao = models.CharField(max_length=255, null=True, blank=True)
    mp = models.CharField(max_length=10, null=True, blank=True)
    mf = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = "materiais"

class Nota(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    descr_avaliacao = models.CharField(max_length=50)
    nota = models.CharField(max_length=10)
    materia = models.ForeignKey(Materia, related_name='notas', on_delete=models.CASCADE)

    class Meta:
        db_table = "notas"

class Falta(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    dia = models.DateField()
    faltas = models.IntegerField()
    materia = models.ForeignKey(Materia, related_name='faltas', on_delete=models.CASCADE)

    class Meta:
        db_table = "faltas"

class Curso(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    descr_curso = models.CharField(max_length=500, default='')
    matriz = models.CharField(max_length=255)
    codigo = models.BigIntegerField()
    campus = models.CharField(max_length=500)
    materias = models.ManyToManyField(Materia, related_name='materias')

    class Meta:
        db_table = "cursos"

class Aluno(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    matricula = models.CharField(max_length=10)
    nome = models.CharField(max_length=255)

    class Meta:
        db_table = "alunos"

class Semestre(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    semestre = models.CharField(max_length=6)
    aluno = models.ForeignKey(Aluno, related_name='aluno', on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso, related_name='cursos')

    class Meta:
        db_table = "semestres"







