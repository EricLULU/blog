"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
import DjangoUeditor #import urls as djud_urls
from django.conf import settings
from django.urls import path

from django.conf.urls import include
import blog.urls as blog_url
from blog.views import home

urlpatterns = [
    path('',home,name="index"),
    path('blog/',include(blog_url)),
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls' )),
    path('users/',include('django.contrib.auth.urls')),
]

"""
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/',include(djud_urls)),
]
"""

if settings.DEBUG:
    from django.conf.urls.static import static
    #urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()