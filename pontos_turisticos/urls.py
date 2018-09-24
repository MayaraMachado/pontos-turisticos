"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from enderecos.api.viewsets import EnderecosViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, base_name="PontoTuristico" )
router.register(r'atracoes', AtracoesViewSet, base_name="Atracao")
router.register(r'enderecos', EnderecosViewSet, base_name="Endereco")
router.register(r'comentarios', ComentarioViewSet, base_name="Comentario")
router.register(r'avaliacoes', AvaliacaoViewSet, base_name="Avaliacao")

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
    ) + static(
        settings.STATIC_URL, document_root = settings.STATIC_ROOT
    )