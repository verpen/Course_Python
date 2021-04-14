from django.db import models


class Part(models.Model):
    title = models.CharField('Название', max_length=60)
    abstract = models.CharField('Аннотация', max_length=200)
    full_text = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Rating(models.Model):
    kino = models.CharField('Название', max_length=40)
    ozenka = models.CharField('Оценка', max_length=4)
    age = models.CharField('Возрастная категория', max_length=3)

    def __str__(self):
        return self.kino

    class Meta:
        verbose_name = 'Рэйтинг'
        verbose_name_plural = 'Рэйтинги'
