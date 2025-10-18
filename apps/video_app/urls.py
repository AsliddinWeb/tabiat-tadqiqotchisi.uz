from django.urls import path

from .views import home_page, videos_page, about_page, contact

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
    path('contact/', contact, name='contact_page'),
    path('videos/', videos_page, name='videos_page'),
]
