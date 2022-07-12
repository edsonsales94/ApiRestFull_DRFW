
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from _curses import *

from core.views import ProdutoViewSet,CategoriaViewset,ModeloViewset

router = routers.DefaultRouter()
router.register(r'produto', ProdutoViewSet)
router.register(r'categoria', CategoriaViewset)
router.register(r'modelo', ModeloViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
