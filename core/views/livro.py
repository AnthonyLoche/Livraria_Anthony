from rest_framework.viewsets import ModelViewSet
from core.models.livro import Livro
from core.serializers.livro import LivroSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
