from django.shortcuts import render

from django.conf import settings

import rest_framework
from rest_framework import  viewsets


from .models import Author
from .serializers import AuthorSerializer


# Определение ViewSet для работы с авторами
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')  # Запрос всех авторов, отсортированных по id
    serializer_class = AuthorSerializer  # Указываем сериализатор для преобразования объектов модели в JSON