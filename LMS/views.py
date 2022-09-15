from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("INDEX PAGE")
    #return render(request,'index.html',context={'title':'Library Management System'})