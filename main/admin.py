from django.contrib import admin
from .models import User, Cop
# Register your models here.

admin.site.register(Cop)
admin.site.register(User)
# admin.site.register(Post)