from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News


# Класс список всех новостей.
class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = News

    # Поле, которое будет использоваться для сортировки объектов
    # В данном случае, новость сортируется в порядке от более свежой к самой старой.
    ordering = ['-dateCreate']

    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'

    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'


# Класс только одна новость.
class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = News

    # Используем другой шаблон — onlynews.html
    template_name = 'onlynews.html'

    # Название объекта, в котором будет выбранна пользователем новость
    context_object_name = 'onlynews'
