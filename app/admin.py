from django.contrib import admin
from .models import Post, Project, Tech

# Register your models here.

admin.site.register(Post)
admin.site.register(Project)
admin.site.register(Tech)