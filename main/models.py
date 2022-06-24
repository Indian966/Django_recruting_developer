from django.db import models

# Create your models here.
class Info(models.Model) :
    user_id = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)

    def __str__(self):
        return self.user_id

# Example)
# 데이터 예시이며, 필드명은 임의로 설정가능합니다.
# {
#   "회사_id":회사_id,
#   "채용포지션":"백엔드 주니어 개발자",
#   "채용보상금":1000000,
#   "채용내용":"원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
#   "사용기술":"Python"
# }