### Hello Django
<pre>
Django 웹 서버 구축 toy project 입니다.
개발자 채용 사이트를 만들어 보았습니다.

</pre>


기술 스택 : <br>
웹 - Django, DRF <br>
서버 - AWS EC2 <br>
Front - html <br>
DB - SQLite <br>
etc - Docker & GithubAction <br>

```
현재 Flask에서 작성된 'pixel-converter' 마이그레이션 하는 작업 진행중
```



## API 명세서

<!-- |Company|||
|---|---|---|
||GET|회사 목록|
||POST|회사 등록|
||GET|회사 상세정보|
||PATCH|회사 상세정보 수정|
||DEL|회사 삭제|

|User|||
|---|---|---|
||GET|사용자 목록|
||POST|사용자 등록|
||GET|사용자 상세정보|
||PATCH|사용자 상세정보 수정|
||DEL|사용자 삭제| -->

|Posting|||
|---|---|---|
||GET|채용공고 목록|
||POST|채용공고 등록|
||GET|채용공고 상세정보|
||PATCH|채용공고 상세정보 수정|
||DEL|채용공고 삭제|

<!-- |Application|||
|---|---|---|
||GET|지원내역 목록|
||POST|지원 등록|
||GET|지원내역 상세정보|
||PATCH|지원내역 수정|
||DEL|지원내역 삭제| -->

-----------

## 메인 페이지

![rest_01](https://user-images.githubusercontent.com/22446076/183009083-ecbca4b0-8e06-41a6-8c47-30f0e872e3dc.png)


채용 공고 리스트와 
새로운 공고를 작성, 지원하기 페이지로 넘어갈 수 있습니다.

----------

## PostDetail

![rest_02](https://user-images.githubusercontent.com/22446076/183009152-269da31c-87a0-4f2e-980d-2d76a409cb9b.png)

공고 리스트를 클릭하여 이동하였습니다.
공고의 자세한 내용을 볼 수 있습니다.
수정, 삭제 할 수 있습니다.

----------

## Application

![rest_04](https://user-images.githubusercontent.com/22446076/183015579-b2950bef-2082-4021-a873-733a7346a6b5.png)


'지원하러가기' 버튼을 통해 이동하였습니다.
공고의 id와 사용자의 id를 이용하여 지원 할 수 있습니다.

----------

## Admin

![post_obj](https://user-images.githubusercontent.com/22446076/177275042-e26a9eb4-af56-4235-bede-ecb18816052d.png)

admin을 통해 사용자, 회사, 공고에 대한 생성, 수정, 삭제를 수행 할 수 있습니다.


----------

## url patterns

![rest_03](https://user-images.githubusercontent.com/22446076/183015645-55d86d3b-069a-420a-bfe9-204b024fc135.png)

url 패턴입니다.

----------
## Model

![rest_05](https://user-images.githubusercontent.com/22446076/183015930-35eb5994-8638-44a7-8243-a8bfc6b061ae.png)


DB에 저장된 Model입니다.

----------

## AWS EC2 개발환경


![jupyter_server](https://user-images.githubusercontent.com/22446076/177480882-4edfd334-badf-4920-ad60-ef1e18b02362.png)

Jupyter 노트북을 데몬으로 돌려서 서버를 구축하였습니다.

----------

![github_action](https://user-images.githubusercontent.com/22446076/177481221-cb5058d0-8976-43df-9fdb-ea53a215fa4c.png)

Github Action을 이용한 Docker 자동 빌드입니다.
