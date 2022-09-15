from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request,'index.html',context={'title':'Library Management System'})


def signup(request):
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            context = {
                'result' : 'Account Added successfully',
                'title':'Sign Up',
            }
            return render(request,'dashboard/result.html',context=context)

        else:
            context = {
                'result' : 'ERROR - Does not meet the requirements!',
                'title':'Sign Up',
            }
            return render(request,'dashboard/result.html',context=context)

    context = {
        'form' : form,
        'title':'Sign Up',
        }

    return render(request,'registration/signup.html',context=context)