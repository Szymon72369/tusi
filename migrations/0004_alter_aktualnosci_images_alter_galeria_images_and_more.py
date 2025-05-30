# Generated by Django 5.2 on 2025-05-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tusi', '0003_galeria_o_nas_oferta_alter_aktualnosci_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktualnosci',
            name='images',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='aktualnosci/'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='images',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='galeria/'),
        ),
        migrations.AlterField(
            model_name='o_nas',
            name='images',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='o_nas/'),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='images',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='oferta/'),
        ),
    ]
