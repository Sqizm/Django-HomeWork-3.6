from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail

urlpatterns = [
    # Вызываем метод as_view.
    path('', NewsList.as_view()),
    # Вызываем метод as_view для страниц по id.
    path('<int:pk>', NewsDetail.as_view()),
]
