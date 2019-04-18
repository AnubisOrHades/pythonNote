#coding:utf8
'''
@author		:	tonyzhang
@version	:	2016-08-08
'''

import pymysql

class DB():
	def __init__(self,DB_HOST,DB_PORT,DB_USER,DB_PASSWD,DB_NAME):
		self.DB_HOST = DB_HOST
		self.DB_PORT = DB_PORT
		self.DB_USER = DB_USER
		self.DB_PASSWD = DB_PASSWD
		self.DB_NAME = DB_NAME
		
		try:
	
			self.conn = pymysql.connect(host.self.DB_HOST,port=self.DB_PORT,user=self.DB_USER,passwd=self.DB_PASSWD)
			self.conn.autocommit(False)
			self.conn.set_character_set("utf8")
			self.cur = self.conn.cursor()
		except pymysql.Error as e:
			print("MySQL Error %d: %s" % (e.argv[0],e.args[1]))
	
	def __del__(self):
		self.close()


	def selectDb(self,db):
		try:
			self.conn.select_db(db)
		except pymysql.Error as e:
			print("MySQL Select Error %d: %s" % (e.argv[0],e.args[1]))
	
	def query(self,sql):
		try:
			n=self.cur.execute(sql)
			return n
		except pymysql.Error as e:
                        print("MySQL Query Error %d: %s" % (e.argv[0],e.args[1]))
	def fetchRow(self):
		result=self.cur.fetchone()
		return result
	def fetchAll(self):
		result=self.cur.fetchall()
		desc = self.cur.description
		d=[]
		for inv in result:
			_d={}
			for i in range(0,len(inv)):
				_d[desc[i][0]]=str(inv[i])
				d.append(_d)
		return d




