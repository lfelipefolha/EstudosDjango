from django.urls import path
from  .views import index, cadastro, alteracao, exclusao, listagem

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('alteracao/', alteracao, name='alteracao'),
    path('exclusao/', exclusao, name='exclusao'),
    path('listagem/', listagem, name='listagem'),
]