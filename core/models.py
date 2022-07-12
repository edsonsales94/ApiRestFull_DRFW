from django.db import models
from django.forms import CharField

class CategoriaProduto(models.Model):
    descricaoCategoria = models.CharField(max_length=60)
    def __str__(self):
        return self.descricaoCategoria

class Modelo(models.Model):
    
    modeloDescricao = models.CharField(max_length=30)
    def __str__(self):
        return self.modeloDescricao

class Produto(models.Model):
    produtoCategoria = models.ForeignKey(CategoriaProduto,on_delete=models.CASCADE)
    modeloProduto = models.ForeignKey(Modelo,on_delete=models.CASCADE)
    nomeProduto = models.CharField(max_length=50)
    especificacoesProduto = models.CharField(max_length=120)
    corProduto = models.CharField(max_length=10)
    preco = models.FloatField(default=0.0)

    def __str__(self):
        return self.nomeProduto






