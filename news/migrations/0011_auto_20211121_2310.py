# Generated by Django 3.2.9 on 2021-11-21 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_remove_movie_release_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iframevideo',
            options={'verbose_name': 'Ссылка на трейлер'},
        ),
        migrations.RenameField(
            model_name='iframevideo',
            old_name='iframe',
            new_name='link',
        ),
    ]
