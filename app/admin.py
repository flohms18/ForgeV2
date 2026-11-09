from django.contrib import admin

from .models import Post, Project, Tech


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "published_at"]
    list_filter = ["tags"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    filter_horizontal = ["tags"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    list_filter = ["category"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ["title"]}
    filter_horizontal = ["stack"]


@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    search_fields = ["name"]
