from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    all_post=Post.objects.filter(status=1).order_by('-created_on')
    return render(request,'project/home.html',{'all_posts':all_post})
def post_details(request,slug):
    get_post=Post.objects.get(slug=slug)
    return render(request,'project/post_details.html',{'get_post':get_post})
    
    

