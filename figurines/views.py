from rest_framework import viewsets, permissions

from .models import Figurine, Step
from .serializers import FigurineSerializer, StepSerializer


class FigurineViewSet(viewsets.ModelViewSet):
    queryset = Figurine.objects.all()
    serializer_class = FigurineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
