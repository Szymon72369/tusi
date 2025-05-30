from django.contrib import admin
from django import forms
from .models import News, AboutUs, Offer, Gallery, Contact, Pricing, Footer, Home

from offer_subpages.models import OfferItem
from .widgets import LinkSelectWidget


# BASE ADMIN -------------------------------------
class BasePageAdmin(admin.ModelAdmin):
    # widget with list of slugs for the given field
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == "button_link":
            field.widget = LinkSelectWidget()
        if db_field.name == "slug":
            field.label = "URL"
        return field

    # anti-clear for button_link field
    def save_model(self, request, obj, form, change):
        if change:
            original = obj.__class__.objects.get(pk=obj.pk)
            if 'button_link' in form.cleaned_data:
                if not form.cleaned_data.get('button_link'):
                    obj.button_link = getattr(original, 'button_link', None)
        super().save_model(request, obj, form, change)


# OFFER ITEM ADMIN ----------------------------
class OfferItemForm(forms.ModelForm):
    class Meta:
        model = OfferItem
        fields = '__all__'

class OfferItemAdmin(BasePageAdmin):
    form = OfferItemForm
    list_display = ('name', 'slug', 'style', 'order')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['style', 'color', 'order']
    ordering = ('order',)


# OTHER PAGES ADMIN -----------------------------
class HomeAdmin(BasePageAdmin):
    list_display = ['name', 'style', 'color', 'order']
    list_editable = ['style', 'color', 'order']
    ordering = ['order']

class NewsAdmin(BasePageAdmin):
    list_display = ['name', 'style', 'color', 'order']
    list_editable = ['style', 'color', 'order']
    ordering = ['order']

class AboutUsAdmin(BasePageAdmin):
    list_display = ['name', 'style', 'color', 'order']
    list_editable = ['style', 'color', 'order']
    ordering = ['order']

class OfferAdmin(BasePageAdmin):
    list_display = ['name', 'style', 'color', 'order']
    list_editable = ['style', 'color', 'order']
    ordering = ['order']

class GalleryAdmin(BasePageAdmin):
    list_display = ['name', 'color', 'order']
    list_editable = ['color', 'order']
    ordering = ['order']

    def get_fields(self, request, obj=None):
        return ['name', 'title', 'text', 'image', 'date', 'color', 'order']


class ContactAdmin(BasePageAdmin):
    list_display = ['name', 'style', 'color', 'order']
    list_editable = ['style', 'color', 'order']
    ordering = ['order']

class PricingAdmin(BasePageAdmin):
    list_display = ['name', 'style', 'color', 'order']
    list_editable = ['style', 'color', 'order']
    ordering = ['order']


# REGISTER MODELS ------------------------------
admin.site.register(Home, HomeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Pricing, PricingAdmin)
admin.site.register(Footer)
