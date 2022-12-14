from rest_framework import serializers
from alunos import models

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aluno
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Curso
        fields = '__all__'


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Materia
        fields = '__all__'


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nota
        fields = '__all__'

class FaltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Falta
        fields = '__all__'

class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Semestre
        fields = '__all__'