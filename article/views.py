from django.shortcuts import render, render_to_response
from django.template import RequestContext
from article.models import Category, Post

# Create your views here.


def home(request):
    articles = Post.objects.all()
    data = {'articles': articles}
    return render_to_response('index.html', data, context_instance=RequestContext(request))


def article_detail(request, pk):
    article = Post.objects.get(pk=pk)
    # article.title = ''
    # article.save()
    data = {'article':article}
    return render_to_response('article/index.html', data, context_instance=RequestContext(request))
