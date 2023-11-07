from django.urls import path
from .views import index, about, contact, product, remot, video


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),
    path('remot/', remot, name='remot'),
    path('video/', video, name='video'),
]

