#!/usr/bin/env python
#coding:utf-8
import commands
import sys
import urllib
import urllib2

'''
	1. 收集本地服务器硬件信息
	2. 收集本地服务器网络信息
	3. POST 上传所有信息至远程服务器
	4. 接收配置服务器返回信息并配置本机

	@tonyzhang 2016-08-22
'''
#接口URL
apiUrl='http://124.251.10.102:28080/zcheck'
def getLocalData():
	postDict={}
	#获取服务器型号
	status,hardware_model=commands.getstatusoutput('''/usr/sbin/dmidecode | grep "Product Name"|head -1|awk -F':' '{print $2}'|tr -d " "''')
	postDict['hardware_model']=hardware_model
	#获取CPU型号
	status,cpu_model=commands.getstatusoutput('cat /proc/cpuinfo |grep \'model name\'|head -1|awk -F\': \' \'{print $2}\'')
	postDict['cpu_model']=cpu_model
	#获取内存大小
	status,memory_total=commands.getstatusoutput('cat /proc/meminfo |grep MemTotal|awk \'{print $2/1024" MB"}\'|awk -F\'.\' \'{print $1" MB"}\'')
	postDict['memory_total']=memory_total
	#获取操作系统信息
	status,kernel=commands.getstatusoutput('uname -r')
	postDict['kernel']=kernel
	return postDict
	
def putData():
	postData=urllib.urlencode(getLocalData())
	
	#提交数据
	req=urllib2.urlopen(apiUrl,postData)
	#获取返回信息
	content=req.read()
	print content,
#	curl -d "name=test1&ip=110.1120.110.110&m=select" http://192.168.100.101:28080/xman/api
putData()
