from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('news/', views.news, name='news'),
    path('offer/', views.offer, name='offer'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('offer/<slug:slug>/', views.offer_subpage, name='offer_subpage'),
    path('pricing/', views.pricing, name='pricing'),
]
