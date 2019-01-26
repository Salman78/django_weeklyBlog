from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'salman',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date posted': 'january 25, 2019'
    },
    {
        'author': 'jon',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date posted': 'january 26, 2019'
    }
]

def home(request):

    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
