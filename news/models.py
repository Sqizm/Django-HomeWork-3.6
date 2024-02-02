from django.db import models


# Класс 'Пост'
class News(models.Model):
    # Поле - название новости/статьи, имеет уникальность.
    name = models.CharField(max_length=128, unique=True)

    # Поле - текст новости/статьи
    description = models.TextField()

    # Поле - автоматическая дата и время создания.
    dateCreate = models.DateTimeField(auto_now_add=True)

    # Поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',  # все новости/статьи в категории будут доступны через поле news
    )

    # Метод магический, выводит заголовок и текст новости/статьи.
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]} Дата публикации: {self.dateCreate}'


# Модель 'Категория'
class Category(models.Model):
    # Поле - название категории, имеет уникальность.
    name = models.CharField(max_length=24, unique=True)

    # Метод магический, выводит название категории.
    def __str__(self):
        return self.name.title()
