from django.shortcuts import render, redirect
from main.models import User, Post, Company, Application

import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

class PostView(View) :

    # 채용 공고 불러오기 && 검색
    def get(self, request):
        try:
            search = request.GET.get('search', None)

            q = Q()

            if search:
                q &= Q(company__name__icontains=search)
                q &= Q(position__icontains=search)
                q &= Q(content__icontains=search)
                q &= Q(tech__icontains=search)

            results = [{
                'id': post.id,
                'company': post.company.name,
                'region': post.company.region,
                'reward': post.reward,
                'position' : post.position,
                'content': post.content,
                'tech': post.tech,
            } for post in Post.objects.filter(q).distinct()]
            return render(request, "index.html", {'post_list' : results})

        except KeyError:
            return JsonResponse({"message": "Key Error"}, status=400)


class PostDetailView(View) :
    # 채용 상세 정보
    def get(self, request, post_id):
        print(request.method)
        if not Post.objects.filter(id=post_id).exists() :
            return JsonResponse({'GET message' : 'No post'}, status=404)

        post = Post.objects.get(id=post_id)
        result = {
            'post_id': post.id,
            'company': post.company.name,
            'position': post.position,
            'reward': post.reward,
            'content': post.content,
            'tech': post.tech
        }
        return render(request, "post_view.html", {'post_info' : result})

    # 채용 공고 수정
    def post(self, request, post_id):
        print("POST")
        try :
            position = request.POST['position']
            reward = request.POST['reward']
            content = request.POST['content']
            tech = request.POST['tech']

            post = Post.objects.get(id=post_id)

            post.position = position
            post.reward = reward
            post.content = content
            post.tech = tech

            post.save()

            return redirect('/')
        except :
            return JsonResponse({'PUT message': 'No post'}, status=401)


# 채용 공고 삭제
class PostDeleteView(View) :

    def get(self, request, post_id):
        print(request.method)
        print('delete')
        if not Post.objects.filter(id=post_id).exists():
            return JsonResponse({'message': '없는 채용공고입니다'}, status=404)
        post = Post.objects.get(id=post_id)
        post.delete()

        return redirect('/')

class NewPostView(View) :
    # 채용 공고 등록
    def post(self, request):
        try:
            print("request : ",request.POST)

            company = request.POST['id']
            position = request.POST['position']
            reward = request.POST['reward']
            content = request.POST['content']
            tech = request.POST['tech']

            Post.objects.create(
                company_id=company,
                position=position,
                reward=reward,
                content=content,
                tech=tech
            )
            return redirect('/')

        except KeyError:
            return JsonResponse({'message': 'Key Error'}, status=400)

    def get(self, request):
        # 뷰 로직 작성
        return render(request, "new-post.html")

class ApplicationView(View):
    # 채용공고에 지원하기
    def get(self, request):
        print("GET")
        return render(request, "application.html")

    def post(self, request):
        print("POST")
        try:
            post = request.POST['post_id']
            user = request.POST['user_id']

            if Application.objects.filter(user_id=user).exists():
                return JsonResponse({'message': '이미 지원한 공고'}, status=404)



            Application.objects.create(
                post_id = post,
                user_id = user,
            )
            return redirect('/')
        except KeyError:
            return JsonResponse({'message': 'Key Error'}, status=400)


# # Create your views here.
# def index(request):
#     post_list = Post.objects.all()
#     return render(request, "index.html", {'post_list' : post_list}) # index.html 렌더링
#
# def new_post(request):
#     # Cop()
#     if request.method == 'POST':
#         new_article = Post.objects.create(
#             cop_id=request.POST['cop_id'],
#             position = request.POST['position'],
#             money = request.POST['money'],
#             content = request.POST['content'],
#             tech = request.POST['tech']
#         )
#         return redirect('index')
#
#     return render(request, "new-post.html") # greet.html 렌더링


