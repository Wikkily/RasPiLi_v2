from django.shortcuts import render

# Create your views here.

def navigation_view(request):
    return render(request, 'navigation.html')