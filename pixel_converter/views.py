from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
import os
import cv2
from PIL import Image
import hashlib
import datetime as dt
from pixel import make_dot


# Create your views here.

@api_view(['GET', 'POST'])
def index(request) :
    if request.method == 'GET' :
        return render('pixel.html')