from main.models import User, Post, Company, Application

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer, \
    PostDetailSerializer, ApplicationSerializer

from django.db.models import Q

# Create your views here.
@api_view(['GET', 'POST'])
def PostList(request):
    if request.method == 'GET':
        posting = Post.objects.all()
        q = request.GET.get('q', '')
        if q:
            posting = posting.filter(
                Q(company__name__icontains=q) | Q(company__region__icontains=q) |
                Q(content__icontains=q) | Q(position__icontains=q) | Q(reward__icontains=q) | Q(tech__icontains=q))
        serializer = PostSerializer(posting, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)


@api_view(['GET', 'PUT', 'DELETE'])
def PostDetail(request, pk):
    try:
        posting = Post.objects.get(id=pk)
    except posting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostDetailSerializer(posting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostUpdateSerializer(posting, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        posting = Post.objects.get(id=pk)
        posting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def ApplyPost(request, pk):
    try:
        apply = Application.objects.all()
    except apply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        apply = apply.filter(jobposting_id_id=pk)
        serializer = ApplicationSerializer(apply, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)
