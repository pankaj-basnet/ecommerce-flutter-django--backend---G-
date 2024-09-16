saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend
$ source venv-0915/Scripts/activate
bash: venv-0915/Scripts/activate: No such file or directory

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend
$ cd dj24

saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24 (master)
$ source venv-0915/Scripts/activate
(venv-0915) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24 (master)
$ which python
/d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24/venv-0915/Scripts/python
(venv-0915) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24 (master)
$ which python
/d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24/venv-0915/Scripts/python
(venv-0915) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24 (master)
$ pip install django
Collecting django
  Downloading Django-5.1.1-py3-none-any.whl.metadata (4.2 kB)
Collecting asgiref<4,>=3.8.1 (from django)
  Using cached asgiref-3.8.1-py3-none-any.whl.metadata (9.3 kB)
Collecting sqlparse>=0.3.1 (from django)
  Using cached sqlparse-0.5.1-py3-none-any.whl.metadata (3.9 kB)  
Collecting tzdata (from django)
  Using cached tzdata-2024.1-py2.py3-none-any.whl.metadata (1.4 kB)
Downloading Django-5.1.1-py3-none-any.whl (8.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 MB 4.1 MB/s eta 0:00:00
Using cached asgiref-3.8.1-py3-none-any.whl (23 kB)
Using cached sqlparse-0.5.1-py3-none-any.whl (44 kB)
Using cached tzdata-2024.1-py2.py3-none-any.whl (345 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django  
Successfully installed asgiref-3.8.1 django-5.1.1 sqlparse-0.5.1 tzdata-2024.1

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip  
(venv-0915) 
Collecting djoser
  Downloading djoser-2.2.3-py3-none-any.whl.metadata (5.8 kB)
ERROR: Could not find a version that satisfies the requirement rest_framework (from versions: none)
ERROR: No matching distribution found for rest_framework

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv-0915)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24 (master)
$ pip install djangorestframework
Collecting djangorestframework
  Downloading djangorestframework-3.15.2-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: django>=4.2 in d:\src_dev\z--proj\ecommerce-flutter-django-dbestech--backend\dj24\venv-0915\lib\site-packages (from djangorestframework) (5.1.1)
Requirement already satisfied: asgiref<4,>=3.8.1 in d:\src_dev\z--proj\ecommerce-flutter-django-dbestech--backend\dj24\venv-0915\lib\site-packages (from django>=4.2->djangorestframework) (3.8.1)
Requirement already satisfied: sqlparse>=0.3.1 in d:\src_dev\z--proj\ecommerce-flutter-django-dbestech--backend\dj24\venv-0915\lib\site-packages (from django>=4.2->djangorestframework) (0.5.1)
Requirement already satisfied: tzdata in d:\src_dev\z--proj\ecommerce-flutter-django-dbestech--backend\dj24\venv-0915\lib\site-packages (from django>=4.2->djangorestframework) (2024.1)
Downloading djangorestframework-3.15.2-py3-none-any.whl (1.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 2.1 MB/s eta 0:00:00
Installing collected packages: djangorestframework
Successfully installed djangorestframework-3.15.2

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv-0915) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24 (master)
$ pip install djoser
Collecting djoser
  Using cached djoser-2.2.3-py3-none-any.whl.metadata (5.8 kB)
Requirement already satisfied: django>=3.0.0 in d:\src_dev\z--proj\ecommerce-flutter-django-dbestech--backend\dj24\venv-0915\lib\site-packages (from djoser) (5.1.1)
Collecting django-templated-mail<2.0.0,>=1.1.1 (from djoser)
  Downloading django_templated_mail-1.1.1-py3-none-any.whl.metadata (2.4 kB)
Collecting djangorestframework-simplejwt<6.0,>=5.0 (from djoser)
  Using cached djangorestframework_simplejwt-5.3.1-py3-none-any.whl.metadata (4.3 kB)
Collecting social-auth-app-django<6.0.0,>=5.0.0 (from djoser)
  Downloading social_auth_app_django-5.4.2-py3-none-any.whl.metadata (3.2 kB)
Requirement already satisfied: asgiref<4,>=3.8.1 in d:\src_dev\z--proj\ecommerce-flutter-django-dbestech--backend\dj24\venv-0915\lib\site-packages (from django>=3.0.0->djoser) (3.8.1)
Requirement already satisfied: sqlparse>=0.3.1 in d:\src_dev\z--proj\ecommerce-flutter-django-dbestech--backend\dj24\venv-0915\lib\site-packages (from django>=3.0.0->djoser) (0.5.1)
Requirement already satisfied: tzdata in d:\src_dev\z--proj\ecommerce-flutter-django-dbestech--backend\dj24\venv-0915\lib\site-packages (from django>=3.0.0->djoser) (2024.1)
Requirement already satisfied: djangorestframework>=3.12 in d:\src_dev\z--proj\ecommerce-flutter-django-dbestech--backend\dj24\venv-0915\lib\site-packages (from djangorestframework-simplejwt<6.0,>=5.0->djoser) (3.15.2)
Collecting pyjwt<3,>=1.7.1 (from djangorestframework-simplejwt<6.0,>=5.0->djoser)
  Downloading PyJWT-2.9.0-py3-none-any.whl.metadata (3.0 kB)
Collecting social-auth-core>=4.4.1 (from social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached social_auth_core-4.5.4-py3-none-any.whl.metadata (4.1 kB)
Collecting requests>=2.9.1 (from social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Collecting oauthlib>=1.0.3 (from social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached oauthlib-3.2.2-py3-none-any.whl.metadata (7.5 kB)
Collecting requests-oauthlib>=0.6.1 (from social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
Collecting cryptography>=1.4 (from social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached cryptography-43.0.1-cp39-abi3-win_amd64.whl.metadata (5.4 kB)
Collecting defusedxml>=0.5.0rc1 (from social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached defusedxml-0.8.0rc2-py2.py3-none-any.whl.metadata (33 kB)
Collecting python3-openid>=3.0.10 (from social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached python3_openid-3.2.0-py3-none-any.whl.metadata (1.6 kB)
Collecting cffi>=1.12 (from cryptography>=1.4->social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached cffi-1.17.1-cp312-cp312-win_amd64.whl.metadata (1.6 kB)
Collecting charset-normalizer<4,>=2 (from requests>=2.9.1->social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached charset_normalizer-3.3.2-cp312-cp312-win_amd64.whl.metadata (34 kB)
Collecting idna<4,>=2.5 (from requests>=2.9.1->social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Downloading idna-3.9-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests>=2.9.1->social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Downloading urllib3-2.2.3-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests>=2.9.1->social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached certifi-2024.8.30-py3-none-any.whl.metadata (2.2 kB)
Collecting pycparser (from cffi>=1.12->cryptography>=1.4->social-auth-core>=4.4.1->social-auth-app-django<6.0.0,>=5.0.0->djoser)
  Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Downloading djoser-2.2.3-py3-none-any.whl (44 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.7/44.7 kB 556.1 kB/s eta 0:00:00
Downloading django_templated_mail-1.1.1-py3-none-any.whl (4.7 kB)
Using cached djangorestframework_simplejwt-5.3.1-py3-none-any.whl (101 kB)
Downloading social_auth_app_django-5.4.2-py3-none-any.whl (27 kB)
Downloading PyJWT-2.9.0-py3-none-any.whl (22 kB)
Using cached social_auth_core-4.5.4-py3-none-any.whl (410 kB)
Using cached cryptography-43.0.1-cp39-abi3-win_amd64.whl (3.1 MB)
Using cached defusedxml-0.8.0rc2-py2.py3-none-any.whl (25 kB)
Using cached oauthlib-3.2.2-py3-none-any.whl (151 kB)
Using cached python3_openid-3.2.0-py3-none-any.whl (133 kB)
Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
Using cached certifi-2024.8.30-py3-none-any.whl (167 kB)
Using cached cffi-1.17.1-cp312-cp312-win_amd64.whl (181 kB)
Using cached charset_normalizer-3.3.2-cp312-cp312-win_amd64.whl (100 kB)
Downloading idna-3.9-py3-none-any.whl (71 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.7/71.7 kB 787.6 kB/s eta 0:00:00
Downloading urllib3-2.2.3-py3-none-any.whl (126 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 126.3/126.3 kB 1.2 MB/s eta 0:00:00
Using cached pycparser-2.22-py3-none-any.whl (117 kB)
Installing collected packages: django-templated-mail, urllib3, pyjwt, pycparser, oauthlib, idna, defusedxml, charset-normalizer, certifi, requests, python3-openid, cffi, requests-oauthlib, djangorestframework-simplejwt, cryptography, social-auth-core, social-auth-app-django, djoser
Successfully installed certifi-2024.8.30 cffi-1.17.1 charset-normalizer-3.3.2 cryptography-43.0.1 defusedxml-0.8.0rc2 django-templated-mail-1.1.1 djangorestframework-simplejwt-5.3.1 djoser-2.2.3 idna-3.9 oauthlib-3.2.2 pycparser-2.22 pyjwt-2.9.0 python3-openid-3.2.0 requests-2.32.3 requests-oauthlib-2.0.0 social-auth-app-django-5.4.2 social-auth-core-4.5.4 urllib3-2.2.3

[notice] A new release of pip is available: 24.0 -> 24.2
[notice] To update, run: python.exe -m pip install --upgrade pip  
(venv-0915)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24 (master)
(venv-0915)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24 (master)
$ cd 'd:/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24/fashion_backend'      
(venv-0915)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24/fashion_backend (master)
(venv-0915)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24/fashion_backend (master)       
$ djang-admin startproject backend .
bash: djang-admin: command not found
(venv-0915)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24/fashion_backend (master)       
$ django-admin startproject backend .
(venv-0915)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/src_dev/z--proj/ecommerce-flutter-django-dbestech--backend/dj24/fashion_backend (master)       
$ date 
Sun, Sep 15, 2024  9:34:16 PM