# Generated by Django 3.2.9 on 2021-11-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_rename_premiere_date_movie_premieredate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecomment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
    ]
