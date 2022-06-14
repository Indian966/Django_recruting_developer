from django.db import models

# Create your models here.
class Info(models.Model) :
    user_id = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)

    def __str__(self):
        return self.user_id

# class InfoB(models.Model) :
#     user = models.ForeignKey(InfoA, on_)