# Generated by Django 5.2 on 2025-05-08 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tusi', '0022_sekcja'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sekcja',
            options={'ordering': ['kolejnosc'], 'verbose_name': 'sekcja', 'verbose_name_plural': 'sekcje'},
        ),
    ]
