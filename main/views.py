from django.shortcuts import render
from main.models import User, Post, Cop

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, "index.html", {'post_list' : post_list}) # index.html 렌더링

def new_post(request):
    cop_id = request.GET['cop_id']
    position = request.GET['position']
    money = request.GET['money']
    content = request.GET['content']
    tech = request.GET['tech']
    Post(cop_id= cop_id,
         post_id =
         position = position)
    return render(request, "new_post.html") # greet.html 렌더링

def post_view(request) :
    user_id = request.GET['uid']
    gender = request.GET['gender']
    Info(user_id=user_id, gender = gender).save()
    return render(request, 'post_view.html', {'user_id' : user_id, 'gender' : gender})

def search_result(request) :

    return render(request, 'search_result.html')

def mod_post(requst) :

    return render(requst, 'mod_post.html')