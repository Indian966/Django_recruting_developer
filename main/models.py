from django.db import models
import uuid

# Create your models here.

class Cop(models.Model) :
    cop_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cop_name = models.CharField(max_length=100, default="", blank=True)
    region = models.CharField(max_length=100, default = 'korea', blank=True)

    def __str__(self):
        return self.cop_name

class Post(models.Model) :
    cop_id = models.ForeignKey(Cop, on_delete = models.CASCADE)
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField(max_length=100, default="", blank=True)
    money = models.IntegerField(default = 1000000)
    tech = models.CharField(max_length=100, default="", blank=True)
    content = models.TextField(null = True, default = '')

    def __str__(self):
        return self.post_id

class User(models.Model) :
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.CharField(max_length=100, default="", blank=True)
    def __str__(self):
        return self.user_id