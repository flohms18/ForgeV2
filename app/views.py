from django.shortcuts import get_object_or_404, render

from .models import Post, Project, Tech


def home(request):
    projects = Project.objects.prefetch_related("stack").order_by("-id")
    posts = Post.objects.prefetch_related("tags")
    tags = Tech.objects.filter(posts__isnull=False).distinct().order_by("name")
    return render(request, "home.html", {
        "projects": projects,
        "posts": posts,
        "tags": tags,
        "categories": Project.Category.choices,
    })


def about(request):
    return render(request, "about.html")


def project_detail(request, slug):
    project = get_object_or_404(Project.objects.prefetch_related("stack"), slug=slug)
    other_projects = Project.objects.exclude(pk=project.pk).order_by("-id")[:3]
    return render(request, "project_detail.html", {
        "project": project,
        "other_projects": other_projects,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post.objects.prefetch_related("tags"), slug=slug)
    other_posts = Post.objects.exclude(pk=post.pk)[:3]
    # Un article peut avoir sa propre page : templates/posts/<slug>.html
    # Sinon, gabarit générique alimenté par le contenu TinyMCE.
    return render(request, [f"posts/{post.slug}.html", "post_detail.html"], {
        "post": post,
        "other_posts": other_posts,
    })
