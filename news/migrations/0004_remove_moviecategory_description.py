# Generated by Django 3.2.9 on 2021-11-13 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_moviedirectoractor_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviecategory',
            name='description',
        ),
    ]
