from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from alunos.models import Aluno
from alunos.serializers import AlunoSerializer
# Create your views here.

@api_view(['GET'])
def getAlunos(request):
    items = Aluno.objects.all()
    serializer = AlunoSerializer(items, many=True)
    return Response(serializer.data)