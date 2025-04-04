from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def blogs(request):
    return render(request, 'pages/blogs.html')

def contact(request):
    return render(request, 'pages/contact.html')

def contact1(request):
    return render(request, 'pages/contact1.html')


