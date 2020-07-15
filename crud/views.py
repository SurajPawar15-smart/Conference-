from django.shortcuts import render
from django.http import HttpResponse
def about(request):
   return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request, 'index.html')
def schedule(request):
    return render(request, 'schedule.html')
def elements(request):
    return render(request, 'elements.html')


