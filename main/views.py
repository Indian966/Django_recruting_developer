from django.shortcuts import render
from main.models import User, Post, Company, Application

import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

class PostView(View) :
    # 채용 공고 등록
    def post(self, request):
        try :
            data = json.loads(request.body)

            company = request.company
            position = data['position']
            reward = data['reward']
            content = data['content']
            tech = data['tech']

            Post.objects.create(
                company_id = company.id,
                position = position,
                reward = reward,
                content = content,
                tech = tech
            )
            return JsonResponse({'message' : '등록 완료'}, status=201)

        except KeyError :
            return JsonResponse({'message' : 'Key Error'}, status=400)


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
                'content': post.content,
                'tech': post.tech,
            } for post in Post.objects.filter(q).distinct()]
            return JsonResponse({"results": results}, status=200)

        except KeyError:
            return JsonResponse({"message": "Key Error"}, status=400)


class PostDetailView(View) :
    # 채용 상세 정보
    def get(self, request, post_id):
        if not Post.objects.filter(id=post_id).exists() :
            return JsonResponse({'message' : '채용 공고가 존재하지 않음'}, status=404)

        post = Post.objects.get(id=post_id)

        result = {
            'recruiting_id': post.id,
            'company': post.company.name,
            'position': post.position,
            'reward': post.reward,
            'content': post.content,
            'tech': post.tech
        }
        return JsonResponse({'result' : result}, status=200)

    # 채용 공고 수정
    def put(self, request, post_id):
        try :
            data = json.loads(request.body)

            position = data['position']
            reward = data['reward']
            content = data['content']
            tech = data['tech']

            post = Recruiting.objects.get(id=recruiting_id)

            post.position = position
            post.reward = reward
            post.content = content
            post.tech = tech

            post.save()

            return JsonResponse({'message': '수정되었습니다'}, status=201)
        except Recruiting.DoesNotExist:
            return JsonResponse({'message': '없는 채용공고입니다'}, status=401)

    # 채용 공고 삭제
    def delete(self, request, post_id):
        if not Recruiting.objects.filter(id=post_id).exists():
            return JsonResponse({'message': '없는 채용공고입니다'}, status=404)
        post = Recruiting.objects.get(id=post_id)
        post.delete()

        return JsonResponse({'message': '삭제되었습니다'}, status=200)


class ApplicationView(View):
    # 채용공고에 지원하기
    def post(self, request, recruiting_id, user_id):
        if not Application.objects.filter(user__id=user_id).exists():
            return JsonResponse({'message' : '이미 지원한 공고'}, status=404)
        try:
            data = json.loads(request.body)

            post = data['post_id']
            user = data['user_id']

            Application.objects.create(
                post = post,
                user = user,
            )
            return JsonResponse({'message' : '지원 완료'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'Key Error'}, status=400)


# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, "index.html", {'post_list' : post_list}) # index.html 렌더링

def new_post(request):
    # Cop()
    if request.method == 'POST':
        new_article = Post.objects.create(
            cop_id=request.POST['cop_id'],
            position = request.POST['position'],
            money = request.POST['money'],
            content = request.POST['content'],
            tech = request.POST['tech']
        )
        return redirect('index')

    return render(request, "new-post.html") # greet.html 렌더링

def post_view(request) :
    user_id = request.GET['uid']
    gender = request.GET['gender']
    Info(user_id=user_id, gender = gender).save()
    return render(request, 'post_view.html', {'user_id' : user_id, 'gender' : gender})

def search_result(request) :

    return render(request, 'search_result.html')

def mod_post(requst) :

    return render(requst, 'mod_post.html')