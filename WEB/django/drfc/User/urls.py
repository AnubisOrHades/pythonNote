from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViews)
# router.register(r'verifycode', views.VerifyCodeViews)

urlpatterns = [
    url(r'^', include(router.urls)),
]
