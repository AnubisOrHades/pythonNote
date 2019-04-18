from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length = 45)
	pwd = models.CharField(max_length = 45)

class Group(models.Model):
	name = models.CharField(max_length = 45)
	
class Host(models.Model):
	name = models.CharField(max_length = 45)
	ip = models.CharField(max_length = 30)
	cname = models.CharField(max_length = 45)
	idc_id = models.IntegerField()
	role = models.CharField(max_length = 10)
	rack = models.CharField(max_length = 30)
	assert_num = models.CharField(max_length = 30)	
	u_phone = models.IntegerField()
	u_id = models.IntegerField()
	update_time = models.IntegerField()
	#update_time = models.DateTimeField(default=datetime.now)
	rep_info = models.CharField(max_length = 45)
	post_time = models.IntegerField()
	status = models.IntegerField(default='0')
	modelNum = models.CharField(max_length = 45,default='0000-0000')
	

	def __str__(self):
		return self.name

class Idc(models.Model):
        city = models.CharField(max_length = 30)
        province = models.CharField(max_length = 30)
        isp = models.CharField(max_length = 30)
        company = models.CharField(max_length = 30)
        #update_time = models.DateTimeField(default=datetime.now)
        update_time = models.IntegerField()

#        def __str__(self):
#                return self.name

class Isp(models.Model):
	name = models.CharField(max_length = 30)
	contact = models.CharField(max_length = 30)
	phone = models.IntegerField()
	info = models.CharField(max_length = 30)
	address = models.CharField(max_length = 30)
class Maintance(models.Model):
        title = models.CharField(max_length = 30)
        msg = models.CharField(max_length = 300)
        ip = models.CharField(max_length = 30)
        idc_id = models.IntegerField()
        update_time = models.IntegerField()
        #update_time = models.DateTimeField(default=datetime.now)

        def __str__(self):
                return self.title
class saltTask(models.Model):
	title = models.CharField(max_length = 45)
	cmd = models.CharField(max_length = 100)
	u_id = models.IntegerField()
	host_id = models.IntegerField()
	update_time = models.IntegerField()
	#update_time = models.DateTimeField(default=datetime.now)

