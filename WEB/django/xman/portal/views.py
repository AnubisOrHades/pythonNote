from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from portal.models import Host
from portal.models import Idc
from portal.models import Isp
from portal.models import User
from portal.models import Maintance
from django.http import JsonResponse
import time

def timestamo_datetime(value):
	format = '%Y-%m-%d %H:%M'
	#value为传入的时间戳
	value = time.localtime(value)
	dt = time.strftime(format,value)
	return dt

# Create your views here.
indexURL='http://192.168.100.101:8080/'
def login(request):
	return render(request,'portal/login.html')
def check_login(request):
	username = request.GET.get('username')
	#username = request.GET.get('u')
	passwd = request.GET.get('password')
	#查询数据库
	pwd = User.objects.get(name__exact=username)
	if pwd.pwd == passwd:
		return HttpResponseRedirect('/')
		#return render(request,'portal/index.html')
	else:
		#return HttpResponse('用户名或密码错误')
		#return HttpResponse('<p style="color:red;">用户名或密码错误</p>')
		return render(request,'portal/login.html')
def addHost(request):
	return render(request,'portal/addHost.html')
def addIdc(request):
	return render(request,'portal/addIdc.html')
def addMaintance(request):
	return render(request,'portal/addMaintance.html')
def saltCMD(request):
	return render(request,'portal/saltCMD.html')
def get_hosts(request):
	#id=request.GET['id']
	hosts=Host.objects.all()[:10]	
	return render(request,'portal/hosts.html',{'hosts':hosts})
def idc_lists(request):
	idcs_list=Idc.objects.all()[:10]
	return HttpResponse('<p style="color:red;">测试IDC机房列表</p>')
	#return render(request,'portal/idcs.html')
#首页
def index(request):
	response = ""
	hosts_list=Host.objects.all()[:10]
	idcs_list=Idc.objects.all()[:10]
	isps_list=Isp.objects.all()[:10]
	maintances_list=Maintance.objects.all()[:10]
	unhosts_list=Host.objects.filter(status='0')[:10]
	return render(request,'index.html',{'hosts':hosts_list,'idcs':idcs_list,'isps':isps_list,'maintances':maintances_list,'unhosts_list':unhosts_list})
#获取IP地址
def ip_address(request):
	return {'ip_address': request.META['REMOTE_ADDR']}
#搜索框搜索
def search(request):
	host = request.GET.get('host')
	idc = request.GET.get('idc')
	hosts_array=Host.objects.filter(name__icontains='%s' % host)[:10]
	idcs_array=Host.objects.filter(name__icontains='%s' % idc)[:10]
	hosts_info=""
	for i in hosts_array:
		hosts_info += "<tr><td>"+str(i.id)+"</td><td>"+i.name+"</td><td>"+i.ip+"</td><td>"+str(i.role)+"</td><td>"+str(i.rack)+"</td><td></td></tr>"
	return HttpResponse("<tr>"+hosts_info+"</tr>")
#检查提交是否正确,包括设备机房维护等所有的
def check_action(request):
	#不接收GET请求
	if request.method == 'GET':
		return HttpResponse(status=403)
	#根据iname判断表单是什么表单	
	if request.POST["iname"] == "add-idc":
		city=request.POST["idc-city"].encode('utf8')
		province=request.POST["idc-province"].encode('utf8')
		isp=request.POST["idc-isp"].encode('utf8')
		company=request.POST["idc-company"].encode('utf8')
		iname=request.POST["iname"].encode('utf8')
		
		#数据库保存数据
		i1 = Idc(city=city,isp=isp,province=province,company=company)
		i1.save()
		return render(request,'portal/formRes.html')
	elif request.POST["iname"] == "add-isp":
		name=request.POST["isp-name"].encode('utf8')
		contact=request.POST["isp-contact"].encode('utf8')
		phone=request.POST["isp-phone"].encode('utf8')
		info=request.POST["isp-info"].encode('utf8')
		address=request.POST["isp-address"].encode('utf8')
		#数据库保存数据
		s1 = Isp(name=name,contact=contact,phone=phone,info=info,address=address)
		s1.save()
		return render(request,'portal/formRes.html')
	elif request.POST["iname"] == "add-host":
		name=request.POST["host-name"].encode('utf8')
		ip=request.POST["host-ip"].encode('utf8')
		contact=request.POST["host-contact"].encode('utf8')
		modelNum=request.POST["host-modNum"].encode('utf8')
		role=request.POST["host-role"].encode('utf8')
		h1 = Host(name=name,ip=ip,role=role,modelNum=modelNum)
		h1.save()
		return render(request,'portal/formRes.html')	
	elif request.POST["iname"] == "add-maintance":
		iname=request.POST["iname"].encode('utf8')
		ip=request.POST["ip"]
		info=request.POST["info"].encode('utf8')
		return HttpResponse(iname)
	elif request.POST["iname"] == "init-host":
                newName=request.POST["name"].encode('utf8')
                info=request.POST["info"].encode('utf8')
                return HttpResponse(newName)
	elif request.POST["iname"] == "modify-isp":
		iid=request.POST["isp-id"]
		name=request.POST["isp-name"].encode('utf8')
		contact=request.POST["isp-contact"].encode('utf8')
		phone=request.POST["isp-phone"].encode('utf8')
		info=request.POST["isp-info"].encode('utf8')
		address=request.POST["isp-address"].encode('utf8')
		#数据库保存数据
		s1 = Isp.objects.filter(id=iid).update(name=name,contact=contact,phone=phone,info=info,address=address)
		return render(request,'portal/formRes.html')

def delete(request):
	#不允许直接访问该地址
	if 'HTTP_REFERER' in request.META.keys():
		referrer=request.META['HTTP_REFERER']
		if referrer != indexURL:
			return HttpResponse(status=403)
		else:	
			if request.GET.get('t') == 'host':
				hid = request.GET.get('id')
				name = request.GET.get('name')
				ip = request.GET.get('ip')
				Host.objects.filter(id=hid).delete()
				return render(request,'portal/formRes.html')			
			elif request.GET.get('t') == 'idc':
				iid = request.GET.get('id')
				name = request.GET.get('name')
				isp = request.GET.get('isp')
				Idc.objects.filter(id=iid).delete()
				return render(request,'portal/formRes.html') 
			elif request.GET.get('t') == 'isp':
				iid = request.GET.get('id')
				Isp.objects.filter(id=iid).delete()
				return render(request,'portal/formRes.html')
			
	else:
		return HttpResponse(status=403)
def modify(request):
	#不允许直接访问该地址
	if 'HTTP_REFERER' in request.META.keys():
		referrer=request.META['HTTP_REFERER']
		if referrer != indexURL:
			return HttpResponse(status=403)
		else:
			if request.GET.get('t') == 'host':
				t = request.GET.get('t')
				name = request.GET.get('name')
				ip = request.GET.get('ip')
				dict_host_info = request.GET
				return render(request,'portal/modify_host.html',{'dict_host_info':dict_host_info})
			elif request.GET.get('t') == 'idc':
				t = request.GET.get('t')
				name = request.GET.get('name')
				isp = request.GET.get('isp')
				dict_idc_info = request.GET
				return render(request,'portal/modify_idc.html',{'dict_idc_info':dict_idc_info})
			elif request.GET.get('t') == 'isp':
				dict_isp_info = request.GET
				return render(request,'portal/modify_isp.html',{'dict_isp_info':dict_isp_info})
			elif request.GET.get('t') == 'initHost':
				dict_init_info = request.GET
				return render(request,'portal/initHost.html',{'dict_init_info':dict_init_info})
	else:
                return HttpResponse(status=403)
def initHost(request):
	#不允许直接访问该地址
	if 'HTTP_REFERER' in request.META.keys():
		referrer=request.META['HTTP_REFERER']
		if referrer != indexURL:
			return HttpResponse(status=403)
		else:
			return render(request,'portal/initHost.html')
	else:
		return HttpResponse(status=403)
#表单提交
def form_upload(request):
	if request.method == 'POST':
		return HttpResponse('数据提交成功!')
	else:
		return HttpResponse("test")
def test1(request):
	return render(request,'portal/formRes.html')
def test2(request):
	return render(request,'portal/test2.html')

def test3(request):
	return render(request,'portal/test3.html')


