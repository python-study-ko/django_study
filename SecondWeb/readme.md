## 두번째 실습입니다.
두번째 실습은 책,저자,출판사등을 관리해주는 애플리케이션을 만들예정입니다
두번째 실습부터는 원래 있는 실습에 몇가지를 추가로 덧붙였습니다.
먼저 책,저자,출판사에 '요약'필드를 만들것이며 요약필드엔 ckeditor을 이용하여
내용을 변경하거나 사진등을 업로드 할수 있게 할것입니다
또한 파일을 업로드시엔 s3와 연동되게 할 예정입니다.
이를 위해선 django뿐만 아니라 django-ckeditor, django-storages를 이용할 예정이오니
실습을 진행하기전 가상환경에 pip -r requierments.txt로 필요한 모듈을 설치해 주시기 바랍니다.

### 1. 작업준비(1)
    가상환경 생성 -> pip install -r requirements.txt
    프로젝트 시작 django-admin.py startproject make2
### 2. 작업준비(2)
    ckeditor, s3 연동하기 - settings.py,urlspy 건드려주기
    settings.sample파일의 확장자를 변경하시면 됩니다.
    python manage.py collectstatic 명령어로 ckeditor을 위한 정적파일 모으
### 3. app 생성하기
    python manage.py startapp books 명령어로 앱 추가
    settings.py에 앱 추가하기

### 4. 모델 추가
    models.py에 모델 추가
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    +hotfix boto3가 아닌 boto로 설치해주세요
    +hotfix settings.py s3설정 입부변경 코드 확인바람
    +testOK ckeditor및 s3파일 업로드 성공적으로 확인 완료!
