# Generated by Django 4.1.6 on 2023-02-11 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autolasercut', '0002_remove_toolpaths_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolpaths',
            name='moddate',
        ),
    ]
