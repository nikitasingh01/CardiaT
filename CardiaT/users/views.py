from django.shortcuts import render
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import  User
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from idea.models import Idea

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your Account is created for {username}!,you can now login')
            return redirect('login')

    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    id=request.user.id
    array=Idea.objects.all()
    result_array=[]
    for i in range(len(array)):
        if request.user== array[i].author:
            result_array.append(array[i])
    context = {
        'posts':result_array

    }
    return render(request,'users/profile.html',context)
# Create your views here.
