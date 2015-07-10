import markdown
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Document(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, null=True, default=None)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def markdown(self):
        return markdown.markdown(self.content)
