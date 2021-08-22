from django.shortcuts import render


def index(request):
    title = 'магазин'
    context = {
        'slogan': 'супер предложения',
        'greeting': 'привет, ',
        'title': title,
        'slogan': 'супер предложения',
    }

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'greeting': 'привет, ',
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context)
