from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from alunos.models import Aluno, Materia, Falta, Nota, Semestre, Curso
from alunos.serializers import AlunoSerializer, SemestreSerializer, CursoSerializer, MateriaSerializer, NotaSerializer, FaltaSerializer



# Create your views here.

@api_view(['GET', 'POST'])
def alunos(request):
    alunos = Aluno.objects.all()
    semestres = Semestre.objects.filter(aluno_id=alunos.last().id)
    

    # serializer = AlunoSerializer(alunos, many=True)
    # semestres_serializer = SemestreSerializer(semestres, many=True)


    response = JsonResponse({
        'alunos': list(alunos.values()),
        'semestres': list(semestres.values())

    }, safe=False, status=status.HTTP_200_OK)
    return response

