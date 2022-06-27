from django.db import models
import uuid

# Create your models here.
class Info(models.Model) :
    user_id = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)

    def __str__(self):
        return self.user_id

class Cop(models.Model) :
    cop_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cop_name = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)

class Post(models.Model) :
    cop_id = models.ForeinKey(Cop, on_delete = models.CASCADE)
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    position = models.CharField(max_length=100)
    money = models.IntegerField(default = 1000000)
    tech = models.CharField(max_length=100)
    content = models.TextField

class User(models.Model) :
    user_id = models.CharField(max_length = 100)
    post_id = models.ForeinKey