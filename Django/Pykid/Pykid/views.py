#made for views
from django.http import HttpResponse
from django.shortcuts import render
a={}
def new(request):
    return render(request,'test.html')

def about(request):
    a = {}
    a['h'] =request.POST.post('textfield','default')

    return render(request,'index.html',a)
    return HttpResponse("<h1><center>this page is about page</center></h1>")


def index(request):
    return render(request,'index.html')

def removepunc(request):
    djtext=request.GET.get('text','default')

    return HttpResponse(djtext)
