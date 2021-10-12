"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, \
                        verify_jwt_token, refresh_jwt_token
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/login', obtain_jwt_token), # id, pw로 jwt 획득
    path('api/login/verify', verify_jwt_token), # 브라우저 재기동 등 storage의 jwt가 유효한지 검사
    path('api/login/refresh', refresh_jwt_token), # jwt 유효기간 갱신, 여기서 토큰 값이 달라짐
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
