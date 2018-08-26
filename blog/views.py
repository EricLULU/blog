from django.shortcuts import render
from blog.models import Article
from datetime import datetime
from django.http import HttpResponse
from django.http import Http404

def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'blog/home.html', {'post_list': post_list})

def Test(request):
    #return HttpResponse('Just a test')
    return render(request,'blog/test.html',{'current_time': datetime.now()})

def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'blog/post.html',{'post':post})
def index(request):
    return render(request, 'index.html')
"""
def Test(request):
    #post = Article.objects.all()
    #return render(request, '/template/test.html',{'current_time':datetime.now()})
    #return HttpResponse(post[0].content)
    return HttpResponse('Just a test')
# Create your views here.
"""