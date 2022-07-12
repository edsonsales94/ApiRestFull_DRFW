from django.shortcuts import render
from rest_framework import routers, viewsets

from core.models import CategoriaProduto, Produto,Modelo
from core.serializers import ProdutoSerializer,CategoriaSerializer,ModeloSerializer


# ViewSets define the view behavior.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CategoriaViewset(viewsets.ModelViewSet):
    queryset = CategoriaProduto.objects.all()
    serializer_class = CategoriaSerializer
# Create your views here.
class ModeloViewset(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer