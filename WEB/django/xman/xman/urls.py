"""xman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from portal import views as portal_views

urlpatterns = [
    url(r'^$',portal_views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^login$',portal_views.login),
    url(r'^check_login/$',portal_views.check_login),
    url(r'^check_action/$',portal_views.check_action),
    url(r'^addHost/$',portal_views.addHost),
    url(r'^addIdc/$',portal_views.addIdc),
    url(r'^addMaintance/$',portal_views.addMaintance),
    url(r'^saltCMD/$',portal_views.saltCMD),
    url(r'^list/hosts/',portal_views.get_hosts),
    url(r'^idc/lists/',portal_views.idc_lists),
    url(r'^myip/',portal_views.ip_address),
    url(r'^search/',portal_views.search),
    url(r'^list/(\s+)/(\d+)/$',portal_views.idc_lists),
    #url(r'^add/$',portal_views.add),
    #url(r'^test/$',portal_views.test),
    url(r'^delete',portal_views.delete),
    url(r'^modify',portal_views.modify),
    url(r'^form_upload',portal_views.form_upload),
    url(r'^test1',portal_views.test1),
    url(r'^test2',portal_views.test2),
    url(r'^test3',portal_views.test3),
]
