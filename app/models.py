from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify

# Create your models here.


class Tech(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300,null=False)
    slug = models.SlugField(unique=True, blank=True)
    content = HTMLField()
    tags = models.ManyToManyField(Tech, related_name="posts", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Project(models.Model):
    class Category(models.TextChoices):
        AGENT = "agent", "Agent IA"
        LOW_CODE = "low_code", "Low-code"
        RAG = "rag" , "RAG"
        DATA = "data", "Data"

    title = models.CharField(max_length=300,null=False)
    slug = models.SlugField(unique=True, blank=True)
    problem = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=Category.choices)
    built = models.TextField() 
    result = models.CharField(max_length=200, blank=True)            
    github_url = models.URLField(blank=True)
    stack = models.ManyToManyField(Tech, related_name="projects", blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    

    



    

    


        

    