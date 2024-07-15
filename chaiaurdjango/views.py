from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, World!. you are at chai aur Django home page')
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse('Hello, World!. you are at chai aur Django about page')

def contact(request):
    # return HttpResponse('Hello, World!. you are at chai aur Django contact page')
    return render(request, 'website/contact.html')