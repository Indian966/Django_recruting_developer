from django.shortcuts import render


def result(request):
    list = ['hi', 'hello', '안녕']
    return render(request, "result.html", {"data" : list})
