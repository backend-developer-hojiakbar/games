from django.shortcuts import render
from .models import Product, Comment, Video, Remot
# Create your views here.
def index(request):
    products = Product.objects.all()
    comments = Comment.objects.all()
    context = {
        'products': products,
        'comments': comments
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})

def product(request):
    video = Video.objects.all()
    remot = Remot.objects.all()
    context = {
        'video': video,
        'remot': remot
    }
    return render(request, 'product.html', context=context)

def remot(request):
    remot = Remot.objects.all()
    context = {
        'remot': remot
    }
    return render(request, 'remot.html', context=context)

def video(request):
    video = Video.objects.all()
    context = {
        'video': video
    }
    return render(request, 'video.html', context=context)














