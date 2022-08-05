from rest_framework import serializers
from main.models import User, Post, Company, Application
from django.db.models import Q

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# 채용공고 전체 목록 조회
class PostSerializer(serializers.ModelSerializer):
    채용공고_id = serializers.IntegerField(source='id')
    회사명 = serializers.CharField(source='company.name')
    지역 = serializers.CharField(source='company.region')
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    사용기술 = serializers.CharField(source='tech')

    class Meta:
        model = Post
        fields = ('채용공고_id', '회사명', '지역', '채용포지션', '채용보상금', '사용기술')


# 채용공고 등록
class PostCreateSerializer(serializers.ModelSerializer):
    회사_id = serializers.CharField(source='company_id')
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    채용내용 = serializers.CharField(source='content')
    사용기술 = serializers.CharField(source='tech')

    class Meta:
        model = Post
        fields = ('회사_id', '채용포지션', '채용보상금', '채용내용', '사용기술')


# 채용공고 수정
class PostUpdateSerializer(serializers.ModelSerializer):
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    채용내용 = serializers.CharField(source='content')
    사용기술 = serializers.CharField(source='tech')

    class Meta:
        model = Post
        fields = ('채용포지션', '채용보상금', '채용내용', '사용기술')


# 채용공고 상세정보
class PostDetailSerializer(serializers.ModelSerializer):
    채용공고_id = serializers.IntegerField(source='id')
    회사명 = serializers.CharField(source='company.name')
    지역 = serializers.CharField(source='company.region')
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    사용기술 = serializers.CharField(source='tech')
    채용내용 = serializers.CharField(source='content')
    회사가올린다른채용공고 = serializers.SerializerMethodField(method_name='get_other_post')

    def get_other_post(self, obj):
        posts = Post.objects.filter(~Q(id=obj.id), company=obj.company)
        posts_id = [post.id for post in posts]
        return posts_id

    class Meta:
        model = Post
        fields = ('채용공고_id', '회사명', '지역', '채용포지션', '채용보상금', '사용기술', '채용내용', '회사가올린다른채용공고')


# 채용공고 지원
class ApplicationSerializer(serializers.ModelSerializer):
    사용자_id = serializers.CharField(source='user_id_id')
    채용공고_id = serializers.IntegerField(source='post_id_id')

    class Meta:
        model = Application
        fields = ('사용자_id', '채용공고_id')