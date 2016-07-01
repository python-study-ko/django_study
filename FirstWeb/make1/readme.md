# 프로젝트 진행
질문에 던지고 그에대한 답변을 보내고 확인하는 앱입니다.

### 1. 프로젝트 시작
    django-admin.py startproject make1
### 2. polls앱 추가
    python manage.py startapp polls
### 3. db 마이그레이션
    python manage.py migrate
### 4. 관리자계정 생성
    python manage.py createsuperuser
### 5. settings.py에 polls앱 추가 및 시간대 변경
### 6. model.py 질문,답변 모델 정의(테이블 정의)
### 7. admin.py 에 모델 추가
### 8. DB마이그레이션
    python manage.py makemigrations
    python manage.py migrate
### 9. 127.0.0.1:8000/admin에 접속후 정상적으로 question 및 choice 등록되있는지 확인
    python manage.py runserver >> 127.0.0.1:8000/admin
### 10. admin페이지에서 질문3개와 각 질문에 대해 선택할 답변 3개씩 추가해두기
### 11. URLconf 코딩
### 12. index 템플릿,뷰 구
    127.0.0.1/polls 접속하여 작동 확인
