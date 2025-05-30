# Generated by Django 5.2 on 2025-05-06 14:10

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tusi', '0005_kontakt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta_Pozycja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=255)),
                ('opis', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('obrazek', models.ImageField(blank=True, null=True, upload_to='oferta/podstrony/')),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='podstrona', to='tusi.oferta')),
            ],
            options={
                'verbose_name': 'Oferta - podstrona',
                'verbose_name_plural': 'Oferta - podstrony',
            },
        ),
    ]
