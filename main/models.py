from django.db import models
import uuid

# Create your models here.

class Cop(models.Model) :
    cop_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cop_name = models.CharField(max_length=100, default="", blank=True)
    region = models.CharField(max_length=100, default = 'korea', blank=True)

class Post(models.Model) :
    cop_id = models.ForeignKey(Cop, on_delete = models.CASCADE)
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.TextField
    money = models.IntegerField(default = 1000000)
    tech = models.TextField
    content = models.TextField

class User(models.Model) :
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE)