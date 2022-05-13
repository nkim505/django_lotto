from django.contrib import admin

# 관리자 페이지와 관련있는 파일
# Register your models here.
from lotto.models import GuessNumbers #lotto폴더에서 models.py파일 가져와서 GuessNumbers를 불러온다
# from .models import GuessNumbers #admin이 속한 폴더에서 models.py를 선택해서 GuessNumbers를 불러온다

admin.site.register(GuessNumbers) #보여주고자하는 DB 해당하는 클래스 넣는다.
