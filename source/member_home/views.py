from django.shortcuts import render


def placeholder(request):
    return render(request, 'member_home/placeholder.html')
