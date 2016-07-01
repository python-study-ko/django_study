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