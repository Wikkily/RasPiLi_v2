from django.shortcuts import render

# Create your views here.

def navigation_view(request):
    return render(request, 'navigation.html',{})

def index_view(request):
    return render(request, 'index.html',{})

def soundboard_view(request):
    return render(request, 'soundboard.html',{})