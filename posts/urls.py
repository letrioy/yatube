# Импортируйте в код всё необходимое
from . import views
from django.urls import path

urlpatterns = [
    path('api/v1/posts/', views.api_posts),
]