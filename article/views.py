from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from article.models import Category, Post
from .forms import PostForm, PostForm2

# Create your views here.


def home(request):
    articles = Post.objects.all()
    data = {'articles': articles}
    return render_to_response('index.html', data, context_instance=RequestContext(request))


def article_detail(request, pk):
    article = Post.objects.get(pk=pk)
    data = {'article':article}
    return render_to_response('article/index.html', data, context_instance=RequestContext(request))

@login_required
def article_add(request):
    form = PostForm2(request.POST or None)

    if form.is_valid():
        # form.save()

        # Create
        post = Post()
        post.title = form.cleaned_data['title']
        post.content = form.cleaned_data['content']
        post.creator = request.user
        post.save()

        # Read
        post = Post.objects.get(pk=1)
        post.title = ''
        post.save()


        return HttpResponseRedirect('/')


    data = {'form':form}
    return render_to_response('article/add_form.html', data, context_instance=RequestContext(request))	