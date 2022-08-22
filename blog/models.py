from datetime import datetime
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    slug =  models.SlugField()
    body = models.TextField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.title