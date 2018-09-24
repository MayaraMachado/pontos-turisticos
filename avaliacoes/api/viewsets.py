from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        return Avaliacao.objects.all()