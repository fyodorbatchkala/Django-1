from django.shortcuts import render
from mainapp.views import get_basket

def index(request):
    title = 'магазин'
    context = {
        'slogan': 'супер предложения',
        'greeting': 'привет, ',
        'title': title,
        'basket': get_basket(request.user),
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'greeting': 'привет, ',
        'title': title,
        'basket': get_basket(request.user),
    }
    return render(request, 'geekshop/contact.html', context)
