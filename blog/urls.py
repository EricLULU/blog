#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('post/(P<id>\\d+)',views.Detail,name="blog_detail"),
    path('home/',views.home,name="blog_home"),
    path('test/',views.Test,name="blog_test"),
]