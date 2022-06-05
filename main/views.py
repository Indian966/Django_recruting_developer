from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html") # index.html 렌더링

def greet(request):
    user_name = request.GET['name']
    return render(request, "greet.html", {'name': user_name}) # greet.html 렌더링

