from curses import meta
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import CategoriaProduto, Produto,Modelo

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Produto
        fields = '__all__'
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= CategoriaProduto
        fields = '__all__'
class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model= Modelo
        fields = '__all__'
