from django.contrib import admin
from .models import User, Company, Post
# Register your models here.

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Post)