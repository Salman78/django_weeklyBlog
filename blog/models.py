from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #User is a separate table in the database which django created for us when we migrated database

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #one to many relationship

    def __str__(self):
        return self.title
