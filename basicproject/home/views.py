from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        "variable": "Hello World"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")