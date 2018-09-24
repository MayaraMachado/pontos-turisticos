from comentarios.models import Comentario
from rest_framework.viewsets import ModelViewSet
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    
    serializer_class = ComentarioSerializer
    
    def get_queryset(self):
        return Comentario.objects.all()
