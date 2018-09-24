from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication

class PontoTuristicoViewSet(ModelViewSet):

    
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao')
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication, )
    # lookup_field = 'id' #Importante o campo ser único

    def get_queryset(self):
        id = self.request.query_params.get('id', None)

        if id:
            queryset = PontoTuristico.objects.filter(id=id)
        else:
            queryset = PontoTuristico.objects.all()

        return queryset
    
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # @action([method='post'], detail=True)
    # def acao_propria(sel, request, pk=None):
    #     pass

    # @action(method=['get'], detail=False)
    # def test(self, request):
    #     pass