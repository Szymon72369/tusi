# Generated by Django 5.2 on 2025-05-08 22:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tusi', '0028_sekcja_tekst_pliku'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(blank=True, max_length=1000, null=True)),
                ('tekst', models.TextField(blank=True, max_length=1000, null=True)),
                ('tekst_przycisku', models.CharField(blank=True, max_length=1000, null=True)),
                ('link_przycisku', models.CharField(blank=True, max_length=1000, null=True)),
                ('tekst_pliku', models.CharField(blank=True, max_length=1000, null=True)),
                ('plik', models.FileField(blank=True, null=True, upload_to='pliki/')),
                ('zdjecie', models.ImageField(blank=True, max_length=255, null=True, upload_to='aktualnosci/')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('styl', models.CharField(choices=[('default', 'Domyślny'), ('img-left', 'Obrazek po lewej'), ('img-right', 'Obrazek po prawej'), ('img-top', 'Obrazek na górze'), ('tiles', 'Kafelek')], default='default', max_length=90)),
                ('kolejnosc', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'strona domowa',
                'verbose_name_plural': 'strona domowa',
            },
        ),
        migrations.DeleteModel(
            name='Plik',
        ),
        migrations.DeleteModel(
            name='Sekcja',
        ),
        migrations.AlterModelOptions(
            name='aktualnosci',
            options={'verbose_name': 'aktualności', 'verbose_name_plural': 'aktualności'},
        ),
        migrations.AlterModelOptions(
            name='cennik',
            options={'verbose_name': 'cennik', 'verbose_name_plural': 'cennik'},
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'stopka', 'verbose_name_plural': 'stopka'},
        ),
        migrations.AlterModelOptions(
            name='galeria',
            options={'verbose_name': 'galeria', 'verbose_name_plural': 'galeria'},
        ),
        migrations.AlterModelOptions(
            name='kontakt',
            options={'verbose_name': 'kontakt', 'verbose_name_plural': 'kontakt'},
        ),
        migrations.AlterModelOptions(
            name='o_nas',
            options={'verbose_name': 'o nas', 'verbose_name_plural': 'o nas'},
        ),
        migrations.AlterModelOptions(
            name='oferta',
            options={'verbose_name': 'oferta', 'verbose_name_plural': 'oferta'},
        ),
        migrations.AlterModelOptions(
            name='oferta_pozycja',
            options={'verbose_name': 'oferta: pozycja', 'verbose_name_plural': 'oferta: pozycje'},
        ),
        migrations.RenameField(
            model_name='aktualnosci',
            old_name='zdjecia',
            new_name='zdjecie',
        ),
        migrations.RemoveField(
            model_name='aktualnosci',
            name='pliki',
        ),
        migrations.RemoveField(
            model_name='cennik',
            name='pliki',
        ),
        migrations.RemoveField(
            model_name='cennik',
            name='zdjecia',
        ),
        migrations.RemoveField(
            model_name='galeria',
            name='pliki',
        ),
        migrations.RemoveField(
            model_name='galeria',
            name='zdjecia',
        ),
        migrations.RemoveField(
            model_name='kontakt',
            name='pliki',
        ),
        migrations.RemoveField(
            model_name='kontakt',
            name='zdjecia',
        ),
        migrations.RemoveField(
            model_name='o_nas',
            name='pliki',
        ),
        migrations.RemoveField(
            model_name='o_nas',
            name='zdjecia',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='pliki',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='zdjecia',
        ),
        migrations.RemoveField(
            model_name='oferta_pozycja',
            name='obrazek',
        ),
        migrations.RemoveField(
            model_name='oferta_pozycja',
            name='opis',
        ),
        migrations.RemoveField(
            model_name='oferta_pozycja',
            name='pliki',
        ),
        migrations.AddField(
            model_name='aktualnosci',
            name='kolejnosc',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aktualnosci',
            name='link_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='aktualnosci',
            name='plik',
            field=models.FileField(blank=True, null=True, upload_to='pliki/'),
        ),
        migrations.AddField(
            model_name='aktualnosci',
            name='styl',
            field=models.CharField(choices=[('default', 'Domyślny'), ('img-left', 'Obrazek po lewej'), ('img-right', 'Obrazek po prawej'), ('img-top', 'Obrazek na górze'), ('tiles', 'Kafelek')], default='default', max_length=90),
        ),
        migrations.AddField(
            model_name='aktualnosci',
            name='tekst_pliku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='aktualnosci',
            name='tekst_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='cennik',
            name='kolejnosc',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cennik',
            name='link_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='cennik',
            name='plik',
            field=models.FileField(blank=True, null=True, upload_to='pliki/'),
        ),
        migrations.AddField(
            model_name='cennik',
            name='styl',
            field=models.CharField(choices=[('default', 'Domyślny'), ('img-left', 'Obrazek po lewej'), ('img-right', 'Obrazek po prawej'), ('img-top', 'Obrazek na górze'), ('tiles', 'Kafelek')], default='default', max_length=90),
        ),
        migrations.AddField(
            model_name='cennik',
            name='tekst_pliku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='cennik',
            name='tekst_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='cennik',
            name='zdjecie',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='aktualnosci/'),
        ),
        migrations.AddField(
            model_name='galeria',
            name='kolejnosc',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='galeria',
            name='link_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='galeria',
            name='plik',
            field=models.FileField(blank=True, null=True, upload_to='pliki/'),
        ),
        migrations.AddField(
            model_name='galeria',
            name='styl',
            field=models.CharField(choices=[('default', 'Domyślny'), ('img-left', 'Obrazek po lewej'), ('img-right', 'Obrazek po prawej'), ('img-top', 'Obrazek na górze'), ('tiles', 'Kafelek')], default='default', max_length=90),
        ),
        migrations.AddField(
            model_name='galeria',
            name='tekst_pliku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='galeria',
            name='tekst_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='galeria',
            name='zdjecie',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='aktualnosci/'),
        ),
        migrations.AddField(
            model_name='kontakt',
            name='kolejnosc',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kontakt',
            name='link_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='kontakt',
            name='plik',
            field=models.FileField(blank=True, null=True, upload_to='pliki/'),
        ),
        migrations.AddField(
            model_name='kontakt',
            name='styl',
            field=models.CharField(choices=[('default', 'Domyślny'), ('img-left', 'Obrazek po lewej'), ('img-right', 'Obrazek po prawej'), ('img-top', 'Obrazek na górze'), ('tiles', 'Kafelek')], default='default', max_length=90),
        ),
        migrations.AddField(
            model_name='kontakt',
            name='tekst_pliku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='kontakt',
            name='tekst_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='kontakt',
            name='zdjecie',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='aktualnosci/'),
        ),
        migrations.AddField(
            model_name='o_nas',
            name='kolejnosc',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='o_nas',
            name='link_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='o_nas',
            name='plik',
            field=models.FileField(blank=True, null=True, upload_to='pliki/'),
        ),
        migrations.AddField(
            model_name='o_nas',
            name='styl',
            field=models.CharField(choices=[('default', 'Domyślny'), ('img-left', 'Obrazek po lewej'), ('img-right', 'Obrazek po prawej'), ('img-top', 'Obrazek na górze'), ('tiles', 'Kafelek')], default='default', max_length=90),
        ),
        migrations.AddField(
            model_name='o_nas',
            name='tekst_pliku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='o_nas',
            name='tekst_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='o_nas',
            name='zdjecie',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='aktualnosci/'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='kolejnosc',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='oferta',
            name='link_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='oferta',
            name='plik',
            field=models.FileField(blank=True, null=True, upload_to='pliki/'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='styl',
            field=models.CharField(choices=[('default', 'Domyślny'), ('img-left', 'Obrazek po lewej'), ('img-right', 'Obrazek po prawej'), ('img-top', 'Obrazek na górze'), ('tiles', 'Kafelek')], default='default', max_length=90),
        ),
        migrations.AddField(
            model_name='oferta',
            name='tekst_pliku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='oferta',
            name='tekst_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='oferta',
            name='zdjecie',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='aktualnosci/'),
        ),
        migrations.AddField(
            model_name='oferta_pozycja',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='oferta_pozycja',
            name='kolejnosc',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='oferta_pozycja',
            name='link_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='oferta_pozycja',
            name='plik',
            field=models.FileField(blank=True, null=True, upload_to='pliki/'),
        ),
        migrations.AddField(
            model_name='oferta_pozycja',
            name='styl',
            field=models.CharField(choices=[('default', 'Domyślny'), ('img-left', 'Obrazek po lewej'), ('img-right', 'Obrazek po prawej'), ('img-top', 'Obrazek na górze'), ('tiles', 'Kafelek')], default='default', max_length=90),
        ),
        migrations.AddField(
            model_name='oferta_pozycja',
            name='tekst',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='oferta_pozycja',
            name='tekst_pliku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='oferta_pozycja',
            name='tekst_przycisku',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='oferta_pozycja',
            name='zdjecie',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='aktualnosci/'),
        ),
        migrations.AlterField(
            model_name='aktualnosci',
            name='tekst',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cennik',
            name='tekst',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='tekst',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='kontakt',
            name='tekst',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='o_nas',
            name='tekst',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='tekst',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='oferta_pozycja',
            name='tytul',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
