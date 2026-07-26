from rest_framework import viewsets

from .models import Figurine, Step
from .serializers import FigurineSerializer, StepSerializer


class FigurineViewSet(viewsets.ModelViewSet):
    queryset = Figurine.objects.all()
    serializer_class = FigurineSerializer


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
