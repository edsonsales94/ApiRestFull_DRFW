from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter
from core.models import  CategoriaProduto, Modelo, Produto

# class CatPorProd(SimpleListFilter):
#     title = 'Por Categoria'
#     parameter_name = 'Por Categoria'
#     def lookups(self, request, model_admin):
#         return (('regata', 'regata'),
#         ('Social', 'Social'),)

#     def queryset(self, request, queryset):
#         print(self.value())
#         if (self.value()=='regata'):
#             return queryset.filter()

# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display= ('id','nomeProduto','produtoCategoria','modeloProduto','especificacoesProduto','corProduto','preco')
    list_filter=('nomeProduto','produtoCategoria')

@admin.register(CategoriaProduto)
class CategoriaProdutoAdmin(admin.ModelAdmin):
    list_display=('id','descricaoCategoria')
    list_filter=('descricaoCategoria',)

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display=('id','modeloDescricao')
    list_filter=('modeloDescricao',)
