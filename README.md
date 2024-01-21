# project name : color blossom

__부제: PERSONAL color 예약 사이트__

---

## 환경세팅

### 아나콘다 세팅
 - conda env list (가상환경 리스트)
 - conda create -n colorblossom python=3.11.4
 - conda activate colorblossom
콘다 설치 
Pillow==9.5.0 - 이미지 처리
Django==4.2.3 - 장고
psycopg2==2.9.6 - 포스트그리 연결
bcrypt - 해쉬 암호화
django-cors-headers -CORS 오류
djangorestframework - 장고 restapi
django-filter - 장고 orm 필터
pandas
numpy
psycopg2-binary -python에서 postgres를 사용하려면 추가 패키지가 필요
django-environ - env 파일 보기위해
beautifulsoup4 -웹 페이지에서 정보를 쉽게 긁어낼 수 있게 해주는 라이브러리
django-rest-knox - rest 인증 모듈 
symspellpy-ko 오타 교정 
jamo - 한글 음절 분해
grpcio
cygrpc - REST 노출 지원을 사용하는 gRPC용 Micro-Framwork.

### 설치해야할것 설치 
 - pip install -r requirements.txt
 - (linux의 경우) 패키지 설치 안 될 시 수동으로 설치
  
### 장고 세팅
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py createsuperuser
 - python manage.py runserver

db 관리자에 등록 admin.py


