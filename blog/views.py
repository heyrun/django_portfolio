from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    blog = Blog.objects.order_by('-created_date')
    return render(request, 'blog/all_blogs.html',{'blogs':blog})

def details(request, id):
    blog =  get_object_or_404(Blog,pk=id)
    return render(request, 'blog/details.html',{'blog':blog})