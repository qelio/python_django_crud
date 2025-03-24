from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

# Импортируем вьюсет для работы с авторами
from mainapp.views import AuthorViewSet

# Определение маршрутов
urlpatterns = [
    # Маршрут для панели администратора
    path('admin/', admin.site.urls),

    # Маршрут для работы со списком авторов (GET — список, POST — создание)
    path('api/author', AuthorViewSet.as_view({'get': 'list', 'post': 'create'})),

    # Маршрут для работы с конкретным автором (GET — получение, DELETE — удаление, PATCH — частичное обновление)
    path('api/author/<pk>', AuthorViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'partial_update'})),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)