from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
posts=[
    {
        'author':'Aduewasola',
        'title':'Data analytics',
        'content':'First blog post',
        'date_posted':'December 23,2022'
    },
    {
        'author':'Lewis',
        'title':'pthon in data analytics',
        'content':'blog post2',
        'date_posted':'January 23,2023'
    }
]


def home(request):
    context={ 'posts':Post.objects.all()}
    return render(request, 'blog/home.html',context)

def about(request):
   # return HttpResponse('<h1>About page worked just fine too, yaaay!</h1>')
   return render(request,'blog/about.html',{'title':'about'})

def introduce(request):
    return HttpResponse('<h3>My name is Oluwasola Aduewa</h3>')