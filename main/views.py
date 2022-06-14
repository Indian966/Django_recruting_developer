from django.shortcuts import render
from main.models import Info

# Create your views here.
def index(request):
    return render(request, "index.html") # index.html 렌더링

def greet(request):
    print(request.GET)

    user_name = request.GET['name']
    return render(request, "greet.html", {'name': user_name}) # greet.html 렌더링

def data_view(request) :
    print(request.GET)

    user_id = request.GET['uid']
    gender = request.GET['gender']
    Info(user_id=user_id, gender = gender).save()
    return render(request, 'data_view.html', {'user_id' : user_id, 'gender' : gender})
