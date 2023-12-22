from django.db import models

# Create your models here.


class SleepingModePhoto(models.Model):
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/sleeping_mode/')

    def __str__(self):
        return f'Фото №{self.pk}'

    class Meta:
        verbose_name = 'Фото спящего режима'
        verbose_name_plural = 'Фотки спящего режима'


class LinkItem(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    link = models.URLField(verbose_name='Ссылка')
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/links/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Содержимое'
        verbose_name_plural = 'Содержимое'

