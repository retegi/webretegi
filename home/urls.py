from nturl2path import url2pathname
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('bio', views.bio, name='bio'),
    path('blog', views.blog, name='blog'),
    path('projects', views.projects, name='projects'),
    path(
        'detail_post/<pk>/',
        views.PostDetailView.as_view(),
        name='detail_post'
    ),
    path(
        'detail_projects/<pk>/',
        views.ProjectDetailView.as_view(),
        name='detail_project'
    ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)