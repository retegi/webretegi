
from urllib import request
from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post, Label, Project
from django.views.generic.detail import DetailView

def home(request):
    #return HttpResponse('Prueba')
    template = loader.get_template('index.html')
    posts = Post.objects.all()
    label = Label.objects.all()
    projects = Project.objects.all()
    context = { 'posts' : posts, 'labels': label, 'projects' : projects }
    #return render(request,'index.html', context)
    return HttpResponse(template.render(context, request))

def bio(request):
    template = loader.get_template('bio.html')
    context = {}
    return HttpResponse(template.render(context, request))

def blog(request):
    template = loader.get_template('blog.html')
    posts = Post.objects.all()
    label = Label.objects.all()
    context = { 'posts' : posts, 'labels': label, }
    return HttpResponse(template.render(context, request))


def projects(request):
    template = loader.get_template('projects.html')
    projects = Project.objects.all()
    context = { 'projects' : projects }
    return HttpResponse(template.render(context, request))

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    def get_context_data(self, **kwargs):
        name = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['PostsTodos'] = Post.objects.all()
        context['Post'] = Post.objects.filter(id = name)
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        name = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['PostsTodos'] = Post.objects.all()
        context['Project'] = Post.objects.filter(id = name)
        return context