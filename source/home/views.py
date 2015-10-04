from django.shortcuts import render_to_response, render

def index(request):
    return render(request, 'home/index.html')
    
def bms(request):
    return render(request, 'home/bms.html')

def contact(request):
    return render(request, 'home/contact.html')
