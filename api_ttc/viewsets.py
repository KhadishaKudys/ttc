from rest_framework import viewsets
from . import models
from . import serializers

class CatergoriesViewset(viewsets.ModelViewSet):
    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer