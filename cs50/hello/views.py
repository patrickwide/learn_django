from django.http import HttpResponse


from django.shortcuts import render

# Create your views here.

# here is where our app index pahe will be running from
# but in order for it to run we need a urls page to handle the urls

def index(request):
    return render(request, "hello/index.html")


def brian(request):
    return HttpResponse("Hello, brian!")


def patrick(request):
    return HttpResponse("Hello, patrick!")


def greet(request,name):
    return render(request,'Hello/greet.html',{
        "name":name.capitalize()
    })