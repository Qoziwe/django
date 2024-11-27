from django.shortcuts import render
from django.http import HttpResponse
from .models import WebSite

def index(request):
    website = WebSite.objects.all()
    context = {'website': website, 'title': 'Список новостей'}
    return render(request, 'website/index.html', context)