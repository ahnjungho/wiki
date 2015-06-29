from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

