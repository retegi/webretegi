from django.contrib import admin
from .models import Post, Label, Project

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields =  (
        'title',
        'datetime',
        'resume',
        'text',
        'image',
        'label',
        'author',
        'readingTime'
    )
admin.site.register(Post, PostAdmin)

class LabelAdmin(admin.ModelAdmin):
    field = (
        'name',
        'backgroundColor'
    )
admin.site.register(Label,LabelAdmin)


class ProjectAdmin(admin.ModelAdmin):
    fields =  (
        'title',
        'datetime',
        'resume',
        'text',
        'image'
    )
admin.site.register(Project, ProjectAdmin)


