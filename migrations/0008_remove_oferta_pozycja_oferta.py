# Generated by Django 5.2 on 2025-05-06 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tusi', '0007_oferta_pozycja_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta_pozycja',
            name='oferta',
        ),
    ]
