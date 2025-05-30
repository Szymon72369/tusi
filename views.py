from django.shortcuts import render, get_object_or_404
from .models import News, AboutUs, Offer, Gallery, Contact, Pricing, Home
from offer_subpages.models import OfferItem, Post


def home(request):
    offers = Post.objects.all()[:3]
    gallery = Gallery.objects.all()[:2]
    last_about = AboutUs.objects.order_by('order').last()
    last_news = News.objects.order_by('order').last()
    home_sections = Home.objects.order_by('order')[:2]
    home_1 = home_sections[0] if len(home_sections) > 0 else None
    home_2 = home_sections[1] if len(home_sections) > 1 else None
    context = {
        'offer': offers if offers else [],
        'gallery': gallery if gallery else [],
        'news': last_news,
        'about': last_about,
        'home_1': home_1,
        'home_2': home_2,
    }
    return render(request, 'tusi/home.html', context)


def about_us(request):
    posts = AboutUs.objects.order_by('order')
    return render(request, 'tusi/about_us.html', {
        'title': 'About Us',
        'posts': posts
    })


def news(request):
    posts = News.objects.order_by('-order')
    return render(request, 'tusi/news.html', {
        'title': 'News',
        'posts': posts
    })


def offer(request):
    posts = Offer.objects.order_by('order')
    pricing = Pricing.objects.all()
    items = OfferItem.objects.all()
    subpages_posts = []

    for item in items:
        first_post = item.posts.order_by('order').first()
        if first_post:
            subpages_posts.append(first_post)

    return render(request, 'tusi/offer.html', {
        'title': 'Offer',
        'posts': posts,
        'pricing': pricing,
        'items': subpages_posts,
    })


def offer_subpage(request, slug):
    item = get_object_or_404(OfferItem, slug=slug)
    posts = item.posts.order_by('order')
    return render(request, 'tusi/offer_subpage.html', {
        'item': item,
        'posts': posts,
    })


def gallery(request):
    posts = Gallery.objects.order_by('-order')
    return render(request, 'tusi/gallery.html', {
        'title': 'Gallery',
        'posts': posts
    })


def contact(request):
    posts = Contact.objects.order_by('order')
    return render(request, 'tusi/contact.html', {
        'title': 'Contact',
        'posts': posts
    })


def pricing(request):
    posts = Pricing.objects.order_by('order')
    return render(request, 'tusi/pricing.html', {
        'title': 'Pricing',
        'posts': posts
    })


def custom_404(request, exception):
    return render(request, "404.html", status=404)