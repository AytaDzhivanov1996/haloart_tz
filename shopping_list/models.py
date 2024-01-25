from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    quantity = models.IntegerField(verbose_name='Кол-во')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'