from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import deactivate
# Create your models here.

class Post(models.Model):
    content = models.TextField()
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:30]



