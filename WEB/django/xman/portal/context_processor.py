#!/usr/bin/env python
#coding:utf-8
def ip_address(request):
    return {'ip_address': request.META['REMOTE_ADDR']}
