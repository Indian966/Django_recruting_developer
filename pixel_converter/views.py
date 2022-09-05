from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def index(request) :
    if request.method == 'GET' :
        return render()