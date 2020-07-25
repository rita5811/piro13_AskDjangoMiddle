from django.urls import path, include
from article.views import index, create #views에서 만든 애들

urlpatterns = [
    path('', index),
    path('create/', create),
]