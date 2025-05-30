from django.db import models
from ckeditor.fields import RichTextField


class Footer(models.Model):
    phone = models.CharField("Telefon", max_length=1000, blank=True, null=True)
    email = models.EmailField("E-mail", max_length=1000, blank=True, null=True)
    adres = models.CharField("Adres", max_length=1000, blank=True, null=True)

    def __str__(self):
        return "Stopka"

    class Meta:
        verbose_name = "stopka"
        verbose_name_plural = "stopka"


# Lista dostępnych styli
STYLE = [
        ('default',     'Tekst, zwykły'),
        ('default-j',   'Tekst, wyjustowany'),
        ('default-c',   'Tekst, wycentrowany'),
        ('wide-panel',  'Tekst, szeroki panel'),
        ('img-left-s',  'Obrazek z lewej, mały'),
        ('img-left-m',  'Obrazek z lewej, średni'),
        ('img-left-l',  'Obrazek z lewej, duży'),
        ('img-right-s', 'Obrazek z prawej, mały'),
        ('img-right-m', 'Obrazek z prawej, średni'),
        ('img-right-l', 'Obrazek z prawej, duży'),
        ('img-top',     'Obrazek na górze'),
        ('img-bot',     'Obrazek na dole'),
    ]

COLOR = [
    ('color-white',     'Biały'),
    ('color-gray',      'Szary'),
    ('color-aqua',      'Błękitny'),
    ('color-blue',      'Niebieski'),
    ('color-green',     'Zielony'),
    ('color-pink',      'Różowy'),
]


class Page(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    text = RichTextField(max_length=60000, blank=True, null=True)
    button_text = models.CharField(max_length=1000, blank=True, null=True)
    button_link = models.CharField(max_length=1000, blank=True, null=True)
    file_text = models.CharField(max_length=1000, blank=True, null=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/', max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    style = models.CharField(max_length=90, choices=STYLE, default='default')
    color = models.CharField(max_length=90, choices=COLOR, default='color-white')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['order']

    def save(self, *args, **kwargs):
        # If order is 0 or not set, assign the next highest value
        if self.order == 0:
            # Get all objects of the same model
            ModelClass = self.__class__
            max_order = ModelClass.objects.aggregate(models.Max('order'))['order__max'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or "None"


class News(Page):

    class Meta:
        verbose_name = "Aktualność"
        verbose_name_plural = "Aktualności"


class AboutUs(Page):

    class Meta:
        verbose_name = "O nas"
        verbose_name_plural = "O nas"


class Offer(Page):

    class Meta:
        verbose_name = "Oferta"
        verbose_name_plural = "Oferty"


class Gallery(Page):

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galeria"


class Contact(Page):

    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontakt"


class Pricing(Page):

    class Meta:
        verbose_name = "Cennik"
        verbose_name_plural = "Cennik"


class Home(Page):

    class Meta:
        verbose_name = "Główna"
        verbose_name_plural = "Główna"
