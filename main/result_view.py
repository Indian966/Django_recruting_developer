from django.shortcuts import render
from main.models import Info

def result(request):
    list = Info.objects.filter()
    data = []
    for i in list :
        data.append(i.user_id + " is " + i.gender)
    return render(request, "result.html", {"data" : data})
