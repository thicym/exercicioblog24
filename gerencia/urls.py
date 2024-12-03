from django.urls import path
from .views import inicio_gerencia, listagem_noticia,cadastrar_noticia,editar_noticia, listar_categg, criar_categg, editar_categg, deletar_categg

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    path('categorias/', listar_categg, name='listar_categg'),
    path('categorias/criar/', criar_categg, name='criar_categg'),
    path('categorias/editar/<int:id>/', editar_categg, name='editar_categg'),
    path('categorias/deletar/<int:id>/', deletar_categg, name='deletar_categg'),
]