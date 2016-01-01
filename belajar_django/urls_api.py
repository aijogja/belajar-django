"""belajar_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from article.api.views import CategoryList, CategoryDetail, PostList, PostDetail

urlpatterns = [
    url(r'^categories/$', CategoryList.as_view(), name='categories-list'),
    url(r'^categories/(?P<pk>\d+)/$', CategoryDetail.as_view(), name='categories-detail'),
    url(r'^posts/$', PostList.as_view(), name='posts-list'),
    url(r'^posts/(?P<pk>\d+)/$', PostDetail.as_view(), name='posts-detail'),
]
