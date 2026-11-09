from django.shortcuts import get_object_or_404, render

from .models import Post, Project, Tech


def home(request):
    projects = Project.objects.prefetch_related("stack").order_by("-id")
    posts = Post.objects.prefetch_related("tags")[:3]
    return render(request, "home.html", {
        "projects": projects,
        "posts": posts,
        "agent_count": Project.objects.filter(category=Project.Category.AGENT).count(),
        "categories": Project.Category.choices,
    })


def about(request):
    # Les technos réellement utilisées dans les projets publiés
    techs = Tech.objects.filter(projects__isnull=False).distinct().order_by("name")
    return render(request, "about.html", {
        "techs": techs,
        "project_count": Project.objects.count(),
        "post_count": Post.objects.count(),
    })


def post_list(request):
    posts = Post.objects.prefetch_related("tags")
    active_tag = None

    tag_name = request.GET.get("tag")
    if tag_name:
        active_tag = get_object_or_404(Tech, name=tag_name)
        posts = posts.filter(tags=active_tag)

    tags = Tech.objects.filter(posts__isnull=False).distinct().order_by("name")
    return render(request, "post_list.html", {
        "posts": posts,
        "tags": tags,
        "active_tag": active_tag,
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
