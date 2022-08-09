from django.contrib import admin
from alunos.models import Aluno, Nota, Materia, Curso, Falta, Semestre
# Register your models here.


class ModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Aluno, ModelAdmin)
admin.site.register(Nota, ModelAdmin)
admin.site.register(Materia, ModelAdmin)
admin.site.register(Falta, ModelAdmin)
admin.site.register(Semestre, ModelAdmin)
admin.site.register(Curso, ModelAdmin)