"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import PostList, PostDetail, ApplyPost
from pixel_converter import views as v2
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostList, name='post_list'),
    path('posts/<int:pk>', PostDetail, name='post_detail'),
    path('posts/<int:pk>/apply', ApplyPost, name='apply_post'),
    path('pixelconverter/', v2.index, name='pixel_converter')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)