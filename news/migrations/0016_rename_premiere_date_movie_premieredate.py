# Generated by Django 3.2.9 on 2021-11-30 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_alter_iframevideo_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='premiere_date',
            new_name='premieredate',
        ),
    ]
