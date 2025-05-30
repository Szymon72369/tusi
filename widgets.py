from django import forms
from django.urls import reverse
from offer_subpages.models import OfferItem

class LinkSelectWidget(forms.TextInput):
    template_name = 'widgets/link_select_widget.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['datalist_id'] = f'{name}_datalist'
        context['options'] = [
            '/home/',
            '/news/',
            '/about_us/',
            '/offer/',
            '/gallery/',
            '/contact/',
            '/pricing/',
        ] + [f'/offer/{obj.slug}/' for obj in OfferItem.objects.all()]
        return context
