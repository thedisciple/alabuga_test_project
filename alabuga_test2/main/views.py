from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def hierarchy(request):
    return render(request, "hierarchy/hierarchy.html")

def auth(request):
    return render(request, "main/auth.html")

def error_404(request):
    return HttpResponse("<h1><i>HTTP ERROR: 404</i></h1>")