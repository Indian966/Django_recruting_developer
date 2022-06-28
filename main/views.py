from django.shortcuts import render
from main.models import Info

# Create your views here.
def index(request):
    return render(request, "index.html") # index.html 렌더링

def new_post(request):

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