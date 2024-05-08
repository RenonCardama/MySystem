from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return render(request, 'hello.html')

def hello_world2(request):
    return render(request, 'helloworld2.html')