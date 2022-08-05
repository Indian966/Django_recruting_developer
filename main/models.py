from django.db import models

# Create your models here.

class Company(models.Model) :
    id = models.CharField(primary_key=True, max_length=20, default="", blank=True)
    name = models.CharField(max_length=20, default="", blank=True)
    region = models.CharField(max_length=20, default = 'korea', blank=True)

    class Meta :
        db_table = 'companies'

class Post(models.Model) :
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default="")
    position = models.CharField(max_length=20, default="", blank=True)
    reward = models.IntegerField()
    tech = models.CharField(max_length=100, default="", blank=True)
    content = models.TextField()

    class Meta :
        db_table = 'posts'

class User(models.Model) :
    user_id = models.CharField(primary_key = True,max_length=20, default="", blank=True)
    name = models.CharField(max_length=20, default="", blank=True)
    # 일단 나중에 구현

    class Meta :
        db_table = 'users'

class Application(models.Model) :
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "applications"