from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .form import Blog_creation,Comment

from .models import Comments, Idea
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


def home(request):
    context = {
        'posts': Idea.objects.all()
    }
    return render(request, 'idea/home.html', context)

def search(request):
    search_text=request.POST['search_text']
    search_text=search_text.lower()
    array=Idea.objects.all()
    result_array=[]
    for i in range(len(array)):
        title= array[i].title
        title=title.lower()
        author=array[i].author
        
        # author=author.lower()
        

        if search_text in title:
            result_array.append(array[i])
    context = {
        'posts':result_array

    }
    
    #     context={Idea.objects}

    return render(request,'idea/home.html',context)

def filter(request):
    array=Idea.objects.all()
    filter=request.POST['Filter']
    array=list(array)
    if filter=='latest':
        array.sort(key=lambda x: x.date_posted, reverse=True)
    elif filter=='oldest':
        array.sort(key=lambda x: x.date_posted, reverse=False)
    elif filter=='most commented':
        pass
    context={
        'posts':array
    }
    print(array)

    return render(request,'idea/home.html',context)
@login_required 
def add(request):
    id=request.user.id
    if request.method=='POST':
        form=Blog_creation(request.POST)
        if form.is_valid():
            form.instance.author=request.user
            form.save()
            return redirect('home')
    else:
        form=Blog_creation()
    return render(request, 'idea/add_idea.html', {'form':form})

def detail(request,idea_id):
    idea=get_object_or_404(Idea, pk=idea_id)
    
    if request.method=='POST':
        if not request.user.is_authenticated:
           return redirect('login')
        form=Comment(request.POST)
        if form.is_valid():
            form.instance.author=request.user
            form.instance.idea=idea
            form.save()
            return HttpResponseRedirect(reverse('idea-view',args=(idea.id, )))
    else:
        form=Comment()
    
    return render(request, 'idea/view_idea.html', {'idea':idea,'form':form, 'view_idea': True})


