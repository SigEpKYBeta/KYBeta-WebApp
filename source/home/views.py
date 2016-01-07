from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def bms(request):
    return render(request, 'home/bms.html')


def contact(request):
    return render(request, 'home/contact.html')


def coming_soon(request):
    return render(request, 'home/coming_soon.html')
