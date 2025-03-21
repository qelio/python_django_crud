from rest_framework import serializers

from .models import Author


# Определение сериализатора
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author  # Указываем, что сериализатор работает с моделью Author
        fields = '__all__'  # Включаем все поля модели в сериализацию (и десериализацию)
