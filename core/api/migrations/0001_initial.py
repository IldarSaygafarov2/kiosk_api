# Generated by Django 5.0 on 2023-12-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('photo', models.ImageField(upload_to='photos/links/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Содержимое',
            },
        ),
        migrations.CreateModel(
            name='SleepingModePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/sleeping_mode/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото спящего режима',
                'verbose_name_plural': 'Фотки спящего режима',
            },
        ),
    ]
