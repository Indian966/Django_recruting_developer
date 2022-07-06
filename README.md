### Hello Django
<pre>
Django 웹 서버 구축 toy project 입니다.
개발자 채용 사이트를 만들어 보았습니다.
</pre>


기술 스택 : <br>
웹 - Django <br>
서버 - AWS EC2 <br>
Front - html <br>
DB - SQLite <br>
etc - Docker & GithubAction <br>


## 메인 페이지

![mainpage_after_admin_newpost](https://user-images.githubusercontent.com/22446076/177272167-1d6e0d21-5617-46c4-be8e-0e7ddc00ad7d.png)

채용 공고 리스트와 
새로운 공고를 작성, 지원하기 페이지로 넘어갈 수 있습니다.

----------

## NewPostView

![newpost](https://user-images.githubusercontent.com/22446076/177274037-8a6b4714-8868-4179-baa3-e8e70cf787b7.png)

'새로운 공고' 버튼을 통해 이동하였습니다.
새로운 공고를 작성 할 수 있습니다.

----------

## PostDetailView

![post_detail](https://user-images.githubusercontent.com/22446076/177274137-468ded1a-43db-4f7e-b3f9-136d59290482.png)

공고 리스트를 클릭하여 이동하였습니다.
공고의 자세한 내용을 볼 수 있습니다.
수정, 삭제 할 수 있습니다.

----------

## ApplicationView

![application0](https://user-images.githubusercontent.com/22446076/177275423-8af35aa7-bea0-4368-8833-3d5f6409aed0.png)

![application](https://user-images.githubusercontent.com/22446076/177274415-cb2bbfa7-a120-45f4-83af-f72a477b9112.png)

'지원하러가기' 버튼을 통해 이동하였습니다.
공고의 id와 사용자의 id를 이용하여 지원 할 수 있습니다.

----------

## Admin

![post_obj](https://user-images.githubusercontent.com/22446076/177275042-e26a9eb4-af56-4235-bede-ecb18816052d.png)

admin을 통해 사용자, 회사, 공고에 대한 생성, 수정, 삭제를 수행 할 수 있습니다.

![mainpage_after_admin_newpost](https://user-images.githubusercontent.com/22446076/177275188-a32826b5-ef61-4ad1-8bf0-d935ee73f249.png)

----------

## url patterns

![url_patterns](https://user-images.githubusercontent.com/22446076/177480834-d014ba4b-67a4-4066-a580-babfad67750e.png)

----------
## Model

![model1](https://user-images.githubusercontent.com/22446076/177275494-5d43327b-dee4-44d7-94c6-73c84bf6a8c3.png)

![moodel2](https://user-images.githubusercontent.com/22446076/177275515-12347431-d860-4830-9fd3-5a1bfc382616.png)

DB에 저장된 Model입니다.

----------

## AWS EC2 개발환경


![jupyter_server](https://user-images.githubusercontent.com/22446076/177480882-4edfd334-badf-4920-ad60-ef1e18b02362.png)

Jupyter 노트북을 데몬으로 돌려서 서버를 구축하였습니다.

----------

![github_action](https://user-images.githubusercontent.com/22446076/177481221-cb5058d0-8976-43df-9fdb-ea53a215fa4c.png)

Github Action을 이용한 Docker 자동 빌드입니다.
