from .models import Footer
from offer_subpages.models import OfferItem

def offer_item_context(request):
    return {
        'offer_subpage': OfferItem.objects.order_by('order') 
    }


def footer_context(request):
    return {
        'footer': Footer.objects.first()
    }
