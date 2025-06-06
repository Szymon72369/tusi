# Generated by Django 5.2 on 2025-05-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tusi', '0046_alter_aktualnosci_kolor_alter_cennik_kolor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktualnosci',
            name='kolor',
            field=models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebiski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90),
        ),
        migrations.AlterField(
            model_name='cennik',
            name='kolor',
            field=models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebiski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='kolor',
            field=models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebiski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90),
        ),
        migrations.AlterField(
            model_name='home',
            name='kolor',
            field=models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebiski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90),
        ),
        migrations.AlterField(
            model_name='kontakt',
            name='kolor',
            field=models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebiski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90),
        ),
        migrations.AlterField(
            model_name='o_nas',
            name='kolor',
            field=models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebiski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='kolor',
            field=models.CharField(choices=[('kol-bialy', 'Biały'), ('kol-szary', 'Szary'), ('kol-niebieski', 'Niebiski'), ('kol-zielony', 'Zielony'), ('kol-rozowy', 'Różowy')], default='kol-bialy', max_length=90),
        ),
    ]
