from django.shortcuts import render,redirect

from item.models import *

from .forms import SignUpForm
# Create your views here.
def Index(request):
    context= {
        'items':Item.objects.filter(is_sold=False)[0:6],
        'Cats':Category.objects.all()
    }
    return render(request,"Main/index.html",context)

def Contect(request):
    return render(request,'Main/contect.html')

def SignUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request,'Main/signup.html',{'form':form})
    else:
        form = SignUpForm()
        return render(request,'Main/signup.html',{'form':form})
