"""drfc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token  # 导入jwt登录
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from User.views import UserViews, BookViews

router = routers.DefaultRouter()
router.register(r'users', UserViews)
router.register(r'books', BookViews)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),  # jwt登录路由
    # url("^api/", include(router.urls)),
    url("^api/", include("User.urls")),
    url(r'api/text/', include_docs_urls(title="初号")),  # 接口文档
    path('san/', include('social_django.urls', namespace='oauth2_provider')),
]
