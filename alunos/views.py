from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from alunos.models import Aluno
from alunos.serializers import AlunoSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def alunos(request):
    a = Aluno.objects.all()
    serializer = AlunoSerializer(a, many=True)
    if request.method == 'POST':
        return Response(serializer.data)
    return Response(serializer.data)

