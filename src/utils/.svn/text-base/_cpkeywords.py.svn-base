#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time,re,sys
import requests
import random
import json
import math
from collections import OrderedDict
# import pyodbc
import pymssql
# import robot
# from robot.errors import DataError
import hashlib

import decimal
import simplejson
import datetime

def json_encode_decimal(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    if isinstance(obj, datetime.datetime):
        return str(obj).split('.')[0]    #转化为时间字符串    '2016-12-02 15:33:41'
    raise TypeError(repr(obj) + " is not JSON serializable")





class _CPKeywords():
    def __init__(self):
        #self.postlist=[]
        self.Debug = "init success"
        #print("CPKeywords_Init")


    def ExGetTimeStr11(self,a,b,c):
        """
        @name    :  ExGetTimeStr
        @brief   :  Get the time string
        @parem   :  NA
        @return  :  time string
        @pkgpath :  Basekeywords.keywords
        @remark  :  
        @author  :  Jarvis
        @history :  Create 2015/6/17
        """
        TimeStr = a+b+c
        return TimeStr


    def ExGetTimeStr22(self,a,b,c):
        """
        @name    :  ExGetTimeStr
        @brief   :  Get the time string
        @parem   :  NA
        @return  :  time string
        @pkgpath :  Basekeywords.keywords
        @remark  :  
        @author  :  Jarvis
        @history :  Create 2015/6/17
        """
        TimeStr = a+b
        return TimeStr



    def ExGetTimeStr44(self,a,b,c):
        """
        @name    :  ExGetTimeStr
        @brief   :  Get the time string
        @parem   :  NA
        @return  :  time string
        @pkgpath :  Basekeywords.keywords
        @remark  :  
        @author  :  Jarvis
        @history :  Create 2015/6/17
        """
        TimeStr = a+b
        return TimeStr


    def CP_Post(self,times,mode,codes,nums,money,issue_start,total_nums,total_money,exceptresult,type,methodid,point,post_url,lotteryid,lotterytype,cookie,desc=None,position=None):
		'''
		@name    :  PostArrayFive
		@brief   :  Get the response of the poster
		@parem   :  <post_url> :the url of the poster
					<sel_times> :the times of sel #下注倍数  n倍
					<mode> :the mode of sel #元、角、分；（1，2，3）
					<sel_type> :the type of sel
					<methodid> :the id of the method
					<codes> : the code of sel #下注号码
					<nums> :the num
					<money>: the money 
					<point>: the point of the user
					<issue_start> :the start of the issue
					<total_nums> :the num of total
					<total_moneynums> :the money of total
					<lotteryid> : the id of lottery #彩种种类 20:排列五
					<lotterytype> :the type  # 下注-2
					<formhash> :hash of the form 
					<cookie> : the id of cookie		
					<exceptresult> :the result of except
		@return  :  
		@pkgpath :  
		@remark  :  
		@author  :  Jason
		@history :  Create 2016/04/06
		'''
		result=-1
		#global project2
		project1 = {}
		project1['type'] = type
		project1['methodid'] = methodid
		project1['codes'] = codes
		project1['nums'] = nums
		project1['times'] = times
		project1['money'] = money
		project1['mode'] = mode
		project1['point'] = point
		project1['curtimes'] = '1459914036996'

		if desc !=None:
			project1['desc'] = desc
		if position !=None:
			project1['position'] = position


		project2 = json.dumps(project1, ensure_ascii=False)

		project2 = project2.replace('"', '\'')
		#print project2
		#
		try:
			#lotteryid = int(lotteryid)
			issue_start = int(issue_start)
		except ValueError:
			issue_start = issue_start
		else:
			if issue_start==9018754615:
				try:
					lotteryid = int(lotteryid)
				except ValueError:
					issue_start=issue_start
				else:
					if   0<lotteryid <99:
						issue_start = self.NewestPeriodCloseTime(lotteryid)
					else:
						issue_start = issue_start
			else:
				issue_start = issue_start

		payload = {
			"lt_project[]":project2,
			"lt_issue_start": issue_start,
			"lt_total_nums": total_nums,
			"lt_total_money": total_money,
			"lotteryid": lotteryid,
			"type": lotterytype,
		  }

		#print  payload

		headers = {
			"cookie": 'CLIENTID='+cookie,
			}


		response = requests.request('POST', post_url, data=payload, headers=headers)

		b=response.text     #{'ret': '\u53c2\u6570\u975e\u6cd52'}
		#print b.decode('raw_unicode_escape')
		#t = json.loads(b)
		#t=t.decode('raw_unicode_escape')
		#print t
		#print t.keys()

		# {"err":"\u53c2\u6570\u975e\u6cd56"}字符串转化为中文
		#c=b.split('"')[3]   #字符串切割
		c=b
		
		if c!='1':
			c=c.decode('raw_unicode_escape')   #转化为中文
			#e={"ret":c}

		if '"ret":"1"' in exceptresult:
			if exceptresult in b:
				result=0
				print "Pass; the respone is:%s,提示:%s" %(b,c)
			else:
				result=-1
				print "Fail; the respone is:%s,提示:%s" %(b,c)	
		else:
			#f=exceptresult.split('"')[3]
			if ":" in exceptresult:
				f=exceptresult.split(':')[1]
				if '"' in f:
					f=f.split('"')[1]
			elif '"' in exceptresult:
				f=exceptresult.split('"')[1]
			else:
				f=exceptresult

			if f==c or f in c or "err" in c or c=='':
				result=0
				print "Pass; the respone is:%s,提示:%s" %(b,c)
			else:
				result=-1
				print "Fail; the respone is:%s,提示:%s" %(b,c)
		return result

    def CP_Post_Lhc(self,methodid,type1,money,codes,cookie1,exceptresult,post_url1,tab=None):
		post_url = post_url1
		result = -1

		payload2={
			"data[0][methodid]": methodid,
			"data[0][type]": type1,
			"data[0][money]": money,
			"data[0][codes]": codes,
		}

		if tab != None:
			payload2["data[0][tab]"] = tab
		#payload = json.dumps(payload, sort_keys=True, separators=(',', ':'))

		#print payload2
		headers = {
			"cookie": 'CLIENTID='+ cookie1
		}

		#print str(payload2).decode('raw_unicode_escape')

		response = requests.request('POST', post_url, data=payload2, headers=headers)

		#b = response.json() # {'ret': '\u53c2\u6570\u975e\u6cd52'}
		#c=response.text
		c = response.text.decode('raw_unicode_escape')

		if '"status":1000' in exceptresult:
			if  '"status":1000' in c:
				result = 0
				print "Pass; the respone is:%s" % (c)
			else:
				result = -1
				print "Fail; the respone is:%s" % (c)
		elif "err" in exceptresult:
			if  '"status":1000' not in c:
				result = 0
				print "Pass; the respone is:%s" % (c)
			else:
				result = -1
				print "Fail; the respone is:%s" % (c)
		else:
			result = -1
			print "Fail; the respone is:%s" % (c)
		return result

    def Get_Var(self,aaa=None,bbb=None,ccc=None,ddd=None,eee=None,fff=None,ggg=None,hhh=None,iii=None,jjj=None,kkk=None,lll=None,mmm=None,nnn=None):
		'''
		@name    :  PostArrayFive
		@brief   :  Get the response of the poster
		@parem   :  <post_url> :the url of the poster
					<sel_times> :the times of sel #下注倍数  n倍
					<sel_modes> :the mode of sel #元、角、分；（1，2，3）
					<sel_type> :the type of sel
					<methodid> :the id of the method
					<codes> : the code of sel #下注号码
					<nums> :the num
					<money>: the money 
					<point>: the point of the user
					<issue_start> :the start of the issue
					<total_nums> :the num of total
					<total_moneynums> :the money of total
					<lotteryid> : the id of lottery #彩种种类 20:排列五
					<lotterytype> :the type  # 下注-2
					<formhash> :hash of the form 
					<cookie> : the id of cookie		
					<exceptresult> :the result of except
		@return  :  
		@pkgpath :  
		@remark  :  
		@author  :  Jason
		@history :  Create 2016/04/06
		'''		
		list_var={'post_url':'Gpost_url','times':'Gtimes','mode':'Gmode','type':'Gtype','methodid':'Gmethodid','codes':'Gcodes',
		'nums':'Gnums','money':'Gmoney','point':'Gpoint','issue_start':'Gissue_start','total_nums':'Gtotal_nums','total_money':'Gtotal_money',
		'lotteryid':'Glotteryid','lotterytype':'Glotterytype','formhash':'Gformhash','cookie':'Gcookie','exceptresult':'Gexceptresult',
		'feipan':'Gtype','codenum':'1','playtype':'10','codenum1':1,'codenum2':1,'codenum3':1,'codenum4':1,'codenum5':1,'listnum':1,'position':'1','desc':1,"tab":None
		}
		list_input=[aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii,jjj,kkk,lll,mmm,nnn]
		for i in list_input :
			list_var[i] = i
		post_var = list_var
		#print post_var
		return post_var


    def Get_Codes_Bjkl8 (self,list_codes,codenum,feipan=None):
		k = int(codenum)
		c1 = random.sample(xrange(80),k)
		#print c1
		#c2 = type(list_codes)(map(lambda i:list_codes[i], c1))
		c2=[list_codes[i] for i in c1]
		codes = '&'.join(c2)

		if feipan=='是':
			codes=codes+'|'+'是'
		return codes

    def Get_Num_Plzh(self,num_m,num_n):
		try:
			num_m = int(num_m)
			num_n = int(num_n)
		except ValueError: 
			codes_num = 1
		else:
			num_n = num_n % 10
			if num_n ==0:
				num_n = 10
			if num_m >= num_n:
				codes_num= math.factorial(num_m)/(math.factorial(num_n)*math.factorial(num_m-num_n))
			else:
				print "the num_m:%s is not large than the num_n:%s" %(num_m,num_n)
				codes_num=1
		return codes_num

    def Get_Money(self,times,mode,num):
		try:
			times1 = int(times)
			mode1 = int(mode)
			num = int(num)
		except ValueError: 
			codes_money = 2
		else:
			if times1 >= 1 and num >= 1 and (mode1 in [1,2,3]):
				codes_money=2*math.pow(10,1-mode1)*times1*num
				#codes_money = round(codes_money,5)
			else:
				codes_money = 2
		return codes_money		

    def Get_Money_Feipan(self,times1,mode1,num,feipan=None):
		try:
			times1 = int(times1)
			mode1 = int(mode1)
			num = int(num)
		except ValueError: 
			codes_money = 2
		else:
			if times1 >= 1 and num >= 1 and (mode1 in [1,2,3]):
				codes_money=2*math.pow(10,1-mode1)*times1*num
				#codes_money = round(codes_money,5)
				if feipan=='是':
					codes_money = 2 * codes_money
			else:
				codes_money = 2
		return codes_money



    def Get_Codes_Num_Cqssc (self,methodid,codenum1=1,codenum2=1,codenum3=1,codenum4=1,codenum5=1,listnum=1):
		#global type
		#type='digital'
		try:
			methodid = int(methodid)
			codenum1 = int(codenum1)
			codenum2 = int(codenum2)
			codenum3 = int(codenum3)
			codenum4 = int(codenum4)
			codenum5 = int(codenum5)
		except ValueError:
			codes = '1|2|3|4|5'
			codes_num = 1
		else:
			codenumlist=[codenum1,codenum2,codenum3,codenum4,codenum5]
			codes_num = 1
			methodid=int(methodid)
			list_shunzi = [u'豹子', u'顺子', u'对子']
			list_daxiaodanshuan = [u'大', u'小', u'单', u'双']
			if methodid==107:   #五星直选  复式：1&3&5&7&9|0&2&4&6&8|1&3&5&7&9|0&2&4&6&8|1&3&5&7&9   注数 = 万个数*千个数*百个数*十个数*个个数
				playtype=5
				codeslist=[self.Get_Codes_Fushi(codenumlist[i]) for i in range(playtype)]
				codes = '|'.join(codeslist)
				for i in range(playtype):
					codes_num *=int(codenumlist[i])
			elif methodid==108:   #五星直选  单式：12345&21211  注数 = 以&分割的字符串数量  =listnum
				playtype=5
			#	type='input'
			#	print type
				codeslist = [self.Get_Codes_Danshi(playtype) for i in range(int(listnum))]
				codes = '&'.join(codeslist)
				codes_num = listnum
			elif methodid==105:   #四星直选   复式：0&3&4|0&3&4&6|0&3|0&1&2   注数 = 千个数*百个数*十个数*个个数
				playtype=4
				codeslist=[self.Get_Codes_Fushi(codenumlist[i]) for i in range(playtype)]
				codes = '|'.join(codeslist)
				#print codenumlist
				for i in range(playtype):
					codes_num *=int(codenumlist[i])
			elif methodid==106:   #四星直选 单式：1111&1234&2222&3333&4321&4444   注数 = 以&分割的字符串数量 =listnum
				playtype=4
				codeslist = [self.Get_Codes_Danshi(playtype) for i in range(int(listnum))]
				codes = '&'.join(codeslist)
				codes_num = listnum
			elif methodid == 88 or methodid == 54:  # 后三直选  复式：0 & 1 | 0 & 1 | 0 & 1   注数 = 百个数*十个数*个个数
				playtype = 3
				codeslist = [self.Get_Codes_Fushi(codenumlist[i]) for i in range(playtype)]
				codes = '|'.join(codeslist)
				for i in range(playtype):
					codes_num *= codenumlist[i]
			elif methodid == 89 or methodid == 55:  # 后三直选 单式：111&123&222&321&333    注数 = 以&分割的字符串数量 =listnum
				playtype = 3
				codeslist = [self.Get_Codes_Danshi(playtype) for i in range(int(listnum))]
				codes = '&'.join(codeslist)
				codes_num = listnum
			elif methodid == 92 or methodid == 58:  # 后三直选  后三组合：0&1&2|1&2|2&3（多中奖、多赔率）  注数 = （百个数*十个数*个个数）* 3
				playtype = 3
				codeslist = [self.Get_Codes_Fushi(codenumlist[i]) for i in range(playtype)]
				codes = '|'.join(codeslist)
				for i in range(playtype):
					codes_num *= codenumlist[i]
				codes_num *= 3
			elif methodid == 90  or methodid == 56:  # 后三直选 直选和值：1&3&5&7&9
				playtype = 3
				zhixuan = 'Y'
				codes, codes_num = self.Get_Codes_Num_Hezhi(playtype, zhixuan, listnum)
			elif methodid == 91  or methodid == 57:  # 后三直选  直选跨度：2&3&4&7
				playtype = 3
				codes, codes_num = self.Get_Codes_Num_Kuadu(playtype, listnum)
			elif methodid == 93  or methodid == 59:  # 后三组选  组三复式：1&2&3  注数 = C(n,m) * 2，n=2，m=投注号码数量。
				codes = self.Get_Codes_Fushi(codenumlist[0])
				if codenumlist[0]>=2:
					codes_num = self.Get_Num_Plzh(codenumlist[0],2)*2
				else:
					codes_num = 1
			elif methodid == 1148 or methodid == 1146 :  # 后三组选 组三单式：112&113&788&799  每注3个号码，其中2个号码必须一样；每注以&分割；如112=百十个有2个1和1个2即中奖；注数 = 以&分割的字符串数量
				codeslist = [self.Get_Codes_Danshi_Zousan() for i in range(int(listnum))]
				codes = '&'.join(codeslist)
				codes_num = listnum
			elif methodid == 94 or methodid == 60:  # 后三组选  组六复式：0&1&2&3&4&5&6&7&8&9 （120注）  注数 = C(n,m)，n=3，m=投注号码数量；
				codes = self.Get_Codes_Fushi(codenumlist[0])
				if codenumlist[0] >= 3:
					codes_num = self.Get_Num_Plzh(codenumlist[0], 3)
				else:
					codes_num = 1
			elif methodid == 1149 or methodid == 1147:  # 后三组选 组六单式：012&056&123&167&456&789  每注3个号码，3个号码各不相同；每注以&分割；注数 = 以&分割的字符串数量
				playtype=3
				codeslist = [self.Get_Codes_Danshi_Zoulu(playtype) for i in range(int(listnum))]
				codes = '&'.join(codeslist)
				codes_num = listnum
			elif methodid == 95 or methodid == 61:  # 后三组选 混合组选：001&123（2注）组三和组六混合，即可以输入组三的号码，又可以输入组6的号码;每注3个号码，格式为组三或组六，不能是豹子号；注数 = 以&分割的字符串数量
				codeslist = [self.Get_Codes_Danshi_Hunhezuxuan() for i in range(int(listnum))]
				codes = '&'.join(codeslist)
				codes_num = listnum
			elif methodid == 97 or methodid == 63:  # 后三组选 组选和值：1&5&9（多赔率）
				playtype = 3
				zhixuan = 'N'
				codes,codes_num = self.Get_Codes_Num_Hezhi(playtype, zhixuan,listnum)
			elif methodid == 99 or methodid == 65:  # 后三组选  组选包胆：只能从0-9选一个号码（多赔率）下注包胆3，百十个开3XX或33X（不限顺序）中后三组选 组三；百十个开3XY(顺序不限）中后三组选 组六；注数 = 54注；
				codes = self.Get_Codes_Fushi(codenumlist[0])
				codes_num = 54
			elif methodid == 101 or methodid == 67:  # 后三其他  和值尾数：1&2&3   注数 = 投注号码的数量（个数）；
				codes = self.Get_Codes_Fushi(codenumlist[0])
				codes_num = codenumlist[0]
			elif methodid == 102 or methodid == 68:  # 后三其他 特殊号：豹子&顺子&对子 豹子由三个同样的数字组成；顺子为三连号；对子为有两个相同的号码；顺序不限；注数 = 投注号码的数量；
				numlist = random.sample(xrange(3), codenumlist[0])
				list1 = list_shunzi
				codeslist=[list1[i] for i in numlist]
				codes = '&'.join(codeslist)
				codes_num = codenumlist[0]
			elif methodid == 38 :  # 前二直选复式，0&1&2|3&4 从万千每位至少选择1个或多个号码投注；投注23，开奖万千为23即中奖（顺序一致）； 注数 = 万个数 * 千个数
				playtype = 2
				codeslist = [self.Get_Codes_Fushi(codenumlist[i]) for i in range(playtype)]
				codes = '|'.join(codeslist)
				for i in range(playtype):
					codes_num *= codenumlist[i]
			elif methodid == 39 :  # 前二直选单式，11&12&22&33    注数 = 以&分割的字符串数量 =listnum
				playtype = 2
				codeslist = [self.Get_Codes_Danshi(playtype) for i in range(int(listnum))]
				codes = '&'.join(codeslist)
				codes_num = listnum
			elif methodid == 40 :  # 前二直选和值，0&1&2&3&4&5 （类似后三直选和值，少了1位）
				playtype = 2
				zhixuan = 'Y'
				codes, codes_num = self.Get_Codes_Num_Hezhi(playtype, zhixuan, listnum)
			elif methodid == 41 :  # 前二直选 直选跨度：3&4&5   注数 = SUM(各投注跨度的注数)
				playtype = 2
				codes,codes_num = self.Get_Codes_Num_Kuadu(playtype,listnum)
			elif methodid == 46 :  # 前二组选 组选复式：0&1&2&3&4 从0到9至少选择2个或多个号码对万千进行投注（不含对子）；投注58，开奖58XXX或85XXX即中奖，顺序不限；注数 = C(n,m)，n=2，m=投注号码数量；
				codes = self.Get_Codes_Fushi(codenumlist[0])
				if codenumlist[0] >= 2:
					codes_num = self.Get_Num_Plzh(codenumlist[0], 2)
				else:
					codes_num = 1
			elif methodid == 47:  # 前二组选 组选单式：13&39&58 每注2个号码，不能是对子，如投注 85；开奖 58XXX或85XXX即中奖，顺序不限；注数 = 以&分割的字符串数量
				playtype = 2
				codeslist = [self.Get_Codes_Danshi_Zoulu(playtype) for i in range(int(listnum))]
				codes = '&'.join(codeslist)
				codes_num = listnum
			elif methodid == 48:  # 前二组选 组选和值：10&11&12 从1到17至少选择1个或以上的号码投注；投注号码=万千之和即中奖（不包含对子）。投注和值2，开奖 02XXX或20XXX 算中奖；开奖11XXX不算中奖；注数 = SUM(各投注和值的注数)
				playtype = 2
				zhixuan = 'N'
				codes, codes_num = self.Get_Codes_Num_Hezhi(playtype, zhixuan, listnum)
			elif methodid == 49:  # 前二组选 组选包胆：5  ：下注包胆3，万千开3X或3X（不限顺序）即中奖；开33不算中奖；不包含对子；注数 = 9注；
				codes = self.Get_Codes_Fushi(codenumlist[0])
				codes_num = 9
			elif methodid == 37:  # 定位胆：1&2&3|4&5&6||6|6&7&8  从万千百十个，每位可选择0-N个号码进行投注；注数 = 所投号码的数量；
				playtype = 5
				codeslist = [self.Get_Codes_Fushi(codenumlist[i]) for i in range(playtype)]
				codes = '|'.join(codeslist)
				codes_num = sum(codenumlist)
			elif methodid == 113 :  # 三星 前三一码：2&3&4；从0到9至少选择1个或多个号码进行投注，每注1个号码，开奖号码万千百包含该号码即中奖；注数 = 所投号码的数量；
				playtype=1
				codes = self.Get_Codes_Fushi(codenumlist[0])
				codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
			elif methodid == 114 :  # 三星 前三二码：4&5&6;从0到9至少选择2个或以上号码进行投注，每注2个号码，开奖号码万千百包含该号码即中奖；投注12，开奖号码万千百里有1个1并且1个2即中奖；注数 = C(n,m)，n=2，m=投注号码的数量；
				playtype = 2
				codes = self.Get_Codes_Fushi(codenumlist[0])
				if codenumlist[0] >= playtype:
					codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
				else:
					codes_num = 1
			elif methodid == 115:  # 三星 后三一码：3&4&5 （同113）；
				playtype = 1
				codes = self.Get_Codes_Fushi(codenumlist[0])
				codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
			elif methodid == 116:  # 三星 后三二码：5&6&7 （同114）；
				playtype = 2
				codes = self.Get_Codes_Fushi(codenumlist[0])
				if codenumlist[0] >= playtype:
					codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
				else:
					codes_num = 1
			elif methodid == 117:  # 四星 前四一码：7&8&9 （同113）；
				playtype = 1
				codes = self.Get_Codes_Fushi(codenumlist[0])
				codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
			elif methodid == 118:  # 四星 前四二码：3&4&5 （同114）；
				playtype = 2
				codes = self.Get_Codes_Fushi(codenumlist[0])
				if codenumlist[0] >= playtype:
					codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
				else:
					codes_num = 1
			elif methodid == 244:  # 244 四星 后四一码：3&4&5 （同113）
				playtype = 1
				codes = self.Get_Codes_Fushi(codenumlist[0])
				codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
			elif methodid == 245:  # 245 四星 后四二码：4&5&6 （同114）
				playtype = 2
				codes = self.Get_Codes_Fushi(codenumlist[0])
				if codenumlist[0] >= playtype:
					codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
				else:
					codes_num = 1
			elif methodid == 119:  # 119 五星 五星一码：1&2&3 （同113）
				playtype = 1
				codes = self.Get_Codes_Fushi(codenumlist[0])
				codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
			elif methodid == 120:  # 120 五星 五星二码：0&1&2&3 （同114）
				playtype = 2
				codes = self.Get_Codes_Fushi(codenumlist[0])
				if codenumlist[0] >= playtype:
					codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
				else:
					codes_num = 1
			elif methodid == 121:  # 121 五星 五星三码：1&3&6 从0到9至少选择3个或以上号码投注，每注3个号码，开奖号码里包含该3个号码即中奖 注数 = C(n,m)，n=3，m=投注号码的数量；
				playtype = 3
				codes = self.Get_Codes_Fushi(codenumlist[0])
				if codenumlist[0] >= playtype:
					codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)
				else:
					codes_num = 1
			elif methodid == 111 :  # 111 前二大小单双：大&小&单|单&双；小：01234大：56789单：13579双：02468从万位、千位中的“大、小、单、双”中至少各选一个组成一注；注数 = 万个数 * 千个数；
				playtype = 2
				list1 = list_daxiaodanshuan
				numlist = [random.sample(xrange(len(list1)), codenumlist[i]) for i in range(playtype)]
				codeslist = [[list1[i] for i in range(len(numlist[j]))] for j in range(len(numlist))]
				codes1 = ['&'.join(codeslist[i]) for i in range(playtype)]
				codes = '|'.join(codes1)
				for i in range(playtype):
					codes_num *= codenumlist[i]
			elif methodid == 109:  # 109 后二大小单双：大&单|小       （同111）；
				playtype = 2
				list1 = list_daxiaodanshuan
				numlist = [random.sample(xrange(len(list1)), codenumlist[i]) for i in range(playtype)]
				codeslist = [[list1[i] for i in range(len(numlist[j]))] for j in range(len(numlist))]
				codes1 = ['&'.join(codeslist[i]) for i in range(playtype)]
				codes = '|'.join(codes1)
				for i in range(playtype):
					codes_num *= codenumlist[i]
			elif methodid == 112:  # 112 前三大小单双：小|小|小&双 从万位、千位、百位中的“大、小、单、双”中至少各选一个组成一注。注数 = 万数量 * 千数量 * 百数量；
				playtype = 3
				list1 = list_daxiaodanshuan
				numlist = [random.sample(xrange(len(list1)), codenumlist[i]) for i in range(playtype)]
				codeslist = [[list1[i] for i in range(len(numlist[j]))] for j in range(len(numlist))]
				codes1 = ['&'.join(codeslist[i]) for i in range(playtype)]
				codes = '|'.join(codes1)
				for i in range(playtype):
					codes_num *= codenumlist[i]
			elif methodid == 110:  # 110 后三大小单双：大|小|单       （同112）
				playtype = 3
				list1 = list_daxiaodanshuan
				numlist = [random.sample(xrange(len(list1)), codenumlist[i]) for i in range(playtype)]
				codeslist = [[list1[i] for i in range(len(numlist[j]))] for j in range(len(numlist))]
				codes1 = ['&'.join(codeslist[i]) for i in range(playtype)]
				codes = '|'.join(codes1)
				for i in range(playtype):
					codes_num *= codenumlist[i]
			# elif methodid == 122 :  # 122  任二直选 复式：2&3&4|4||4&5&6&7|1&2&7  从万位、千位、百位、十位、个位中至少两位上各选1个号码组成一注；顺序一致；
			# 	# 投注注数 = 假设 万数量x1，千数量x2，百数量x3，十数量x4，个数量x5。（不计算数量为0的）=  (x1*x2) + (x1*x3) + (x1*x4) + (x1*x5) + (x2*x3) + (x2*x4) + (x2*x5) + (x3*x4) + (x3*x5) + (x4*x5)
			# 	#中奖注数 = 万千百十个的中奖数量 x1 = C(n,m)，n=2，m=万千百十个的中奖数量。
			# 	playtype = 5
			# 	codeslist = [self.Get_Codes_Fushi(codenumlist[i]) for i in range(playtype)]
			# 	codes = '|'.join(codeslist)
			# 	list1 = [i for i in codenumlist if i > 0]
			# 	codes_num = 0
			# 	for i in range(len(list1)):
			# 		for j in range(i, len(list1)):
			# 			if i < j :
			# 				codes_num += list1[i] * list1[j]
			# elif methodid == 123:  # 123 任二直选 单式：11&13&22 注意sPosition字段  位置选择字段sPosition：万千百十个：0&1&2&3&4   十个：3&4   万千：0&1
			# 	# 从万位、千位、百位、十位、个位中至少选择两个位置,至少手动输入一个两位数的号码构成一注；注数 = C(n, m) * 以 & 分割的字符串数量，n = 2，m = 选择的位置数量；
			# 	#如输入11&13&22 = 3个字符串，位置选择 百十个3个，那么，投注注数 = C(2,3) * 3 = 9注；
			# 	playtype = 2
			# 	codeslist = [self.Get_Codes_Danshi(playtype) for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = listnum * self.Get_Num_Plzh(len(position.split('&')),playtype)
			# elif methodid == 124:  # 124 任二直选 和值：2&4&12&13&14      注意sPosition字段 注数 = C(n,m) * （以&分割的和值对应的注数之和），n=2，m=选择的位置数量；
			# 	playtype = 2
			# 	zhixuan = 'Y'
			# 	codeslist, codes_num_list = [self.Get_Codes_Num_Hezhi(playtype, zhixuan) for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = sum(codes_num_list)
			# 	codes_num = codes_num * self.Get_Num_Plzh(len(position.split('&')),playtype)
			# elif methodid == 125:  # 125 任二组选 复式：0&1&2&3&4    注意sPosition字段 从万位、千位、百位、十位、个位中至少选择两个位置,号码区0到9至少选择两个号码构成一注。
			# 	#   注数 = C(2,位置数量) * C(2,投注号码数量） 假设选择3个位置，C(2,3) = 3；假设投注4个号码，C(2,4) = 6       注数 = 3*6 = 18 注；
            #
			# 	codes = self.Get_Codes_Fushi(codenumlist[0])
			# 	if codenumlist[0] >= 2:
			# 		codes_num = self.Get_Num_Plzh(codenumlist[0], 2)
			# 		codes_num = codes_num * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# 	else:
			# 		codes_num = 1
			# elif methodid == 126:  # 126 任二组选 单式：12&13，以前玩法ID是125 注意sPosition字段 从万位、千位、百位、十位、个位中至少选择两个位置,至少手动输入一个两位数的号码构成一注。
			# 	#输入的号码不能是两个相同的数字，如11。      注数 = C(2,位置数量) * 以&分割的字符串数量
			# 	playtype = 2
			# 	codeslist = [self.Get_Codes_Danshi_Zoulu(playtype) for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = listnum * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 127:  # 127 任二组选 和值：3&5&6     注意sPosition字段 从万位、千位、百位、十位、个位中至少选择两个位置,从1到17至少选择一个和值号码构成一注。 注数 = C(2,位置数量) * 和值X在2个位置时的注数
			# 	playtype = 2
			# 	zhixuan = 'N'
			# 	codeslist, codes_num_list = [self.Get_Codes_Num_Hezhi(playtype, zhixuan) for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = sum(codes_num_list)
			# 	codes_num = codes_num * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 128:  # 128 任三直选 直选复式：0&1|0&1|0&1|0&1|0&1 从万位、千位、百位、十位、个位中至少三位上各选1个号码组成一注。 注数 = 参考 122
			# 	playtype = 5
			# 	codeslist = [self.Get_Codes_Fushi(codenumlist[i]) for i in range(playtype)]
			# 	codes = '|'.join(codeslist)
			# 	list1 = [i for i in codenumlist if i > 0]
			# 	codes_num = 0
			# 	for i in range(len(list1)):
			# 		for j in range(i, len(list1)):
			# 			for k in range(j, len(list1)):
			# 				if i < j < k:
			# 					codes_num += list1[i] * list1[j] * list1[k]
			# elif methodid == 129:  # 129 任三直选 单式：111&123&234&456   注意sPosition字段
			# 	# 至少选择3个位置；万位、千位、百位、十位、个位中至少选择三个位置,至少手动输入一个三位数的号码构成一注。注数 = C(playtype,位置数量) * 以&分割的字符串数量
			# 	playtype = 3
			# 	codeslist = [self.Get_Codes_Danshi(playtype) for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = listnum * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 130:  # 130 任三直选 直选和值：4&18&19        注意sPosition字段 至少选择3个位置；从万位、千位、百位、十位、个位中至少选择三个位置,至少选择一个和值号码构成一注。注数 = C(3,位置数量) * 和值X在3个位置时的注数
			# 	playtype = 3
			# 	zhixuan = 'Y'
			# 	codeslist, codes_num_list = [self.Get_Codes_Num_Hezhi(playtype, zhixuan) for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = sum(codes_num_list)
			# 	codes_num = codes_num * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 131:  # 131 任三组选 组三复式：1&2&3   注意sPosition字段  从万位、千位、百位、十位、个位中至少选择三个位置,号码区至少选择两个号码构成一注。
			# 	#   投注号码12，位置百十个，有2注，112，122，只要百十个有2个1，1个2，或1个1，2个2即中奖； 注数 = C(3,位置数量) * (C(2,投注号码数量) * 2)
			# 	playtype=3
			# 	codes = self.Get_Codes_Fushi(codenumlist[0])
			# 	if codenumlist[0] >= 2:
			# 		codes_num = self.Get_Num_Plzh(codenumlist[0], 2) * 2   # (C(2,投注号码数量) * 2
			# 		codes_num = codes_num * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# 	else:
			# 		codes_num = 1
			# elif methodid == 132:  # 132 任三组选 组三单式：112&113（以前玩法ID是131）   注意sPosition字段 从万位、千位、百位、十位、个位中至少选择三个位置,手动至少输入三个号码构成一注。
			# 	# 位置至少选择3个，最多5个；输入的号码必须是2个一样的，1个不一样，如122，不能输入111或123。注数 = C(3,位置数量) * 以&分割的字符串数量
			# 	playtype = 3
			# 	codeslist = [self.Get_Codes_Danshi_Zousan() for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = listnum * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 133:  # 133 任三组选 组六复式：2&3&4&5&6   注意sPosition字段
			# 	#   从万位、千位、百位、十位、个位中至少选择三个位置,号码区0到9至少选择三个号码构成一注。注数 = C(3,位置数量) * C(3,投注号码数量)
			# 	playtype = 3
			# 	codes = self.Get_Codes_Fushi(codenumlist[0])
			# 	if codenumlist[0] >= playtype:
			# 		codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)  # (C(3,投注号码数量)
			# 		codes_num = codes_num * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# 	else:
			# 		codes_num = 1
			# elif methodid == 134:  # 134 任三组选 组六单式：137&567 （以前玩法ID是133）  注意sPosition字段  注数 = C(3,位置数量) * 以&分割的字符串数量
			# 	# 从万位、千位、百位、十位、个位中至少选择三个位置,手动至少输入三个号码构成一注。位置至少选择3个，最多5个；输入的号码必须是3个不一样的数字，如123，不能输入112 111 122等。
			# 	playtype = 3
			# 	codeslist = [self.Get_Codes_Danshi_Zoulu(playtype) for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = listnum * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 135:
			# 	#135 任三组选  混合组选：125 & 137 & 223 注意sPosition字段 从万位、千位、百位、十位、个位中至少选择三个位置,手动至少输入三个号码构成一注(不包含豹子号)。
			# 	# 位置至少选择3个最多5个；输入的号码必须是 112 或 123 这样的，不能输入111（豹子）。注数 = 注数 = C(3,位置数量) * 以&分割的字符串数量
			# 	playtype = 3
			# 	codeslist = [self.Get_Codes_Danshi_Hunhezuxuan() for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = listnum * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 137:  # 137 任三组选 组选和值：4&17&18      注意sPosition字段 从万位、千位、百位、十位、个位中至少选择三个位置,从1-27至少选择一个和值号码构成一注。注数 = C(3,位置数量) * 和值X在3个位置时的注数
			# 	playtype = 3
			# 	zhixuan = 'N'
			# 	codeslist, codes_num_list = [self.Get_Codes_Num_Hezhi(playtype, zhixuan) for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = sum(codes_num_list)
			# 	codes_num = codes_num * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 139:  #139 任四直选 直选复式：0&3|0&2|0&1&2|0|0&1   从万位、千位、百位、十位、个位中至少四位上各选1个号码组成一注。 注数 = 参考 122
			# 	playtype = 5
			# 	codeslist = [self.Get_Codes_Fushi(codenumlist[i]) for i in range(playtype)]
			# 	codes = '|'.join(codeslist)
			# 	list1 = [i for i in codenumlist if i > 0]
			# 	codes_num = 0
			# 	for i in range(len(list1)):
			# 		for j in range(i, len(list1)):
			# 			for k in range(j, len(list1)):
			# 				for h in range(k,len(list1)):
			# 					if i < j < k < h:
			# 						codes_num += list1[i] * list1[j] * list1[k] * list1[h]
			# elif methodid == 140:  # 140 任四直选 直选单式：1122&1371&3313    注意sPosition字段
			# 	# 从万位、千位、百位、十位、个位中至少选择四个位置,至少手动输入一个四位数的号码构成一注。位置至少选择4个最多5个；输入4个数字。注数 = C(playtype,位置数量) * 以&分割的字符串数量
			# 	playtype = 4
			# 	codeslist = [self.Get_Codes_Danshi(playtype) for i in range(int(listnum))]
			# 	codes = '&'.join(codeslist)
			# 	codes_num = listnum * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 141:  # 141 任四组选 组选24：2&3&4&5&6&7         注意sPosition字段 从万位、千位、百位、十位、个位中至少选择四个位置,号码区0到9至少选择四个号码构成一注。
			# 	#   注数 = C(4,位置数量) * C(4,投注号码数量）
			# 	playtype = 4
			# 	codes = self.Get_Codes_Fushi(codenumlist[0])
			# 	if codenumlist[0] >= playtype:
			# 		codes_num = self.Get_Num_Plzh(codenumlist[0], playtype)   # (C(4,投注号码数量)
			# 		codes_num = codes_num * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 142:  # 142 任四组选 组选12：2&3&4|2&3&4  注意sPosition字段  从万位、千位、百位、十位、个位中至少选择四个位置,从“二重号”选择一个号码，“单号”中选择两个号码组成一注。
			# 	#注数= C(4,位置数量) *[ C(1,二重号数量）*C(2,单号数量）-C(1,重复号码数量）*C(1,单号数量-1）]
			# 	playtype = 4
			# 	codeslist = [self.Get_Codes_Fushi(codenumlist[i]) for i in range(2)]
			# 	codes = '|'.join(codeslist)
			# 	codes1=codeslist[0].split('&')
			# 	codes2 = codeslist[1].split('&')
			# 	chongfu_num=0
			# 	for i in codes1:
			# 		if i in codes2:
			# 			chongfu_num +=1
			# 	codes_num = self.Get_Num_Plzh(codenumlist[0], 1) * self.Get_Num_Plzh(codenumlist[1], 2) - self.Get_Num_Plzh(chongfu_num, 1) * self.Get_Num_Plzh((codenumlist[1]-1), 1)
			# 	codes_num * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 143:  # 143 任四组选 组选6：3&4&5&6              注意sPosition字段 从万位、千位、百位、十位、个位中至少选择四个位置,从“二重号”中选择两个号码组成一注。
			# 	#   注数 = C(4,位置数量) * C(2,投注号码数量）
			# 	playtype = 4
			# 	codes = self.Get_Codes_Fushi(codenumlist[0])
			# 	if codenumlist[0] >= 2:
			# 		codes_num = self.Get_Num_Plzh(codenumlist[0], 2)  # (C(2,投注号码数量)
			# 		codes_num = codes_num * self.Get_Num_Plzh(len(position.split('&')), playtype)
			# elif methodid == 142:  # 144 任四组选 组选4：3&4&5|3&4&5          注意sPosition字段 从万位、千位、百位、十位、个位中至少选择四个位置,从“三重号”中选择一个号码，“单号”中选择一个号码组成一注。
			# 	# 注数= C(4,位置数量) *[ C(1,三重号数量）*C(1,单号数量）-重复号码数量*]
			# 	playtype = 4
			# 	codeslist = [self.Get_Codes_Fushi(codenumlist[i]) for i in range(2)]
			# 	codes = '|'.join(codeslist)
			# 	codes1 = codeslist[0].split('&')
			# 	codes2 = codeslist[1].split('&')
			# 	chongfu_num = 0
			# 	for i in codes1:
			# 		if i in codes2:
			# 			chongfu_num += 1
			# 	codes_num = self.Get_Num_Plzh(codenumlist[0], 1) * self.Get_Num_Plzh(codenumlist[1], ) - chongfu_num
			# 	codes_num * self.Get_Num_Plzh(len(position.split('&')), playtype)
			else:
				codes = '9|9|9|9|9'
				codes_num = 1
		#return codes,codes_num,type
		return codes, codes_num

    def Get_Codes_Danshi(self, playtype=None):
		k = int(playtype)
		a = random.randrange(pow(10, k))
		# c = [0 for i in range(k)]
		# for i in range(k):
		# 	c[i] = str(a / (pow(10, (k - i - 1))) % 10)
		c1 = [str(a / (pow(10, (k - i - 1))) % 10) for i in range(k)]
		codes = ''.join(c1)
		return codes

    def Get_Codes_Fushi(self, codenum=None):
		k = int(codenum)
		c2 = random.sample(xrange(10), k)
		for i in range(k):
			c2[i] = str(c2[i])
		codes = '&'.join(c2)
		return codes

    def Get_Codes_Num_Hezhi(self, playtype=None,zhixuan=None,listnum=None):
		a = int(playtype)
		listnum = int(listnum)
		if a==2:
			if zhixuan=='Y':
				codeslist = random.sample(xrange(9 * a +1),listnum)
				c2 = map(str, codeslist)
				codes = '&'.join(c2)
				codes_num = 0
				for h in range(listnum):
					for i in range(10):
						for j in range(10):
							if (i + j) == codeslist[h]:
								codes_num += 1
			elif zhixuan=='N':
				codeslist = random.sample(xrange(1,9 * a),listnum)
				c2 = map(str, codeslist)
				codes = '&'.join(c2)
				codes_num = 0
				for h in range(listnum):
					for i in range(10):
						for j in range(i,10):
							if not(i==j) and(i + j) == codeslist[h]:
								codes_num += 1
		elif a == 3:
			#print zhixuan
			if zhixuan == 'Y':
				codeslist = random.sample(xrange(9 * a + 1), listnum)
				c2 = map(str, codeslist)
				codes = '&'.join(c2)
				codes_num = 0
				for h in range(listnum):
					for i in range(10):
						for j in range(10):
							for k in range(10):
								if (i + j + k) == codeslist[h]:
									codes_num += 1
			elif zhixuan == 'N':
				codeslist = random.sample(xrange(1,9 * a ), listnum)
				c2=map(str,codeslist)
				codes = '&'.join(c2)
				codes_num = 0
				for h in range(listnum):
					for i in range(10):
						for j in range(i,10):
							for k in range(j,10):
								if not(i==j==k) and (i + j + k) == codeslist[h]:
									codes_num += 1
		#codes = str(codes)
		#codes_num = int(codes_num)
		return codes,codes_num

    def Get_Codes_Num_Kuadu(self, playtype=None,listnum=None):
		a = int(playtype)
		listnum = int(listnum)
		codeslist = random.sample(xrange(10),listnum)
		c2 = map(str, codeslist)
		codes = '&'.join(c2)
		codes_num = 0
		if a==2:
			for h in range(listnum):
				for i in range(10):
					for j in range(10):
						list1 = [i, j]
						if (max(list1) - min(list1)) == codeslist[h]:
							codes_num += 1
		elif a == 3:
			for h in range(listnum):
				for i in range(10):
					for j in range(10):
						for k in range(10):
							list1 = [i, j, k]
							if (max(list1) - min(list1)) == codeslist[h]:
								codes_num += 1
		return codes,codes_num

    def Get_Codes_Danshi_Zousan(self):  #3个号码，2个相同，1个不同    （对子，非豹子）
		a = random.randrange(10)
		while True:
			b = random.randrange(10)
			if b == a:
				continue
			else:
				break
		c=a
		codes = str(a)+str(b)+str(c)
		return codes

    def Get_Codes_Danshi_Zoulu(self, playtype=3):  #3个号码，各不相同 （非豹子、非对子）
		k = int(playtype)
		c2 = random.sample(xrange(10), k)
		for i in range(k):
			c2[i] = str(c2[i])
		codes = ''.join(c2)
		return codes

    def Get_Codes_Danshi_Hunhezuxuan(self):   #3个号码：各不相同，或者2同1不同（即非豹子）
		a = random.randrange(10)
		while True:
			b = random.randrange(10)
			c = random.randrange(10)
			if a == b == c:
				continue
			else:
				break
		codes = str(a) + str(b) + str(c)
		return codes

    def NewestPeriodCloseTime(self,sUrl,iGameId):
		'''
		@name    :  PostArrayFive
		@brief   :  Get the response of the poster
		@parem   :  <post_url> :the url of the poster
					<sel_times> :the times of sel #下注倍数  n倍
					<mode> :the mode of sel #元、角、分；（1，2，3）
					<sel_type> :the type of sel
					<methodid> :the id of the method
					<codes> : the code of sel #下注号码
					<nums> :the num
					<money>: the money
					<point>: the point of the user
					<issue_start> :the start of the issue
					<total_nums> :the num of total
					<total_moneynums> :the money of total
					<lotteryid> : the id of lottery #彩种种类 20:排列五
					<lotterytype> :the type  # 下注-2
					<formhash> :hash of the form
					<cookie> : the id of cookie
					<exceptresult> :the result of except
		@return  :
		@pkgpath :
		@remark  :
		@author  :  Jason
		@history :  Create 2016/04/06
		'''
		result=-1
		payload = {
			"iGameId": iGameId,
		  }

		src2=str(payload["iGameId"]) + String_token
		token1=hashlib.md5(src2.decode('raw_unicode_escape')).hexdigest()

		payload["Token"]=token1


		payload=json.dumps(payload,sort_keys=True,separators=(',',':'))

		#print  payload

		function_name = sys._getframe().f_code.co_name
		post_url = sUrl + function_name + "/"
		response = requests.request('POST', post_url, data=payload)
#        print 'response--->',requests.request('POST', post_url, data=payload)

		b=response.json()    #{'ret': '\u53c2\u6570\u975e\u6cd52'}
		#print b
		iCloseTime=b["Records"][0]["iCloseTime"]
		#print iCloseTime
		if iCloseTime>=5:
			sGamePeriod=int(b["Records"][0]["sGamePeriod"])
		else:
			time.sleep(5)
			sGamePeriod=int(b["Records"][0]["sGamePeriod"])+1
		#sGamePeriod=b["Records"][0]["sGamePeriod"]

		return sGamePeriod


    def TestBonus(self,iGameId,iPlayTypeId,sBetCode,nums,iType,sOpenNum,sPosition=None):
		'''
		iGameId = 彩种ID
		iPlayTypeId = 玩法
		sBetCode = 下注号码
		iBetCount = 下注注数
		iType = 默认为0，当所投注的数据是手工输入的时候，标记为1，如 重庆时时彩 五星直选单式。
		sOpenNum = 开奖号码
		fAmount = 投注金额
		fPrize = 赔率
		sPosition = 投注号码位置（一般不需要，当彩种可以勾选位置的时候需要传入，如重庆时时彩任选二直选单式）。
		位置选择字段sPosition：万千百十个：0&1&2&3&4   十个：3&4   万千：0&1

		BonusResult = 结果，0-默认值，1-校验失败，2-中奖，3-未中奖
		iWinCount = 中奖注数
		sWinCode = 中奖号码
		fWinAmount = 中奖金额

		iGameId = 彩种ID
		iPlayTypeId = 玩法ID
		sBetCode = 下注号码
		iBetCount = 下注注数
		fAmount = 下注总金额
		fPrize = 赔率
		sOpenNum = 开奖号码

		示例JSON：
		{"iGameId":1,"iPlayTypeId":15,"sBetCode":"0&1&2&3|0&1&2&3|0&1&2&3","iBetCount":64,"fAmount":100,"fPrize":500,
		"fReward":0,"sOpenNum":"1|2|1","BonusResult":2,"Desc":"OK","iWinCount":1,"sWinCode":"1|2|1","fWinAmount":781.25}
		'''

		'''
		@name    :  PostArrayFive
		@brief   :  Get the response of the poster
		@parem   :  <post_url> :the url of the poster
					<sel_times> :the times of sel #下注倍数  n倍
					<mode> :the mode of sel #元、角、分；（1，2，3）
					<sel_type> :the type of sel
					<methodid> :the id of the method
					<codes> : the code of sel #下注号码
					<nums> :the num
					<money>: the money
					<point>: the point of the user
					<issue_start> :the start of the issue
					<total_nums> :the num of total
					<total_moneynums> :the money of total
					<lotteryid> : the id of lottery #彩种种类 20:排列五
					<lotterytype> :the type  # 下注-2
					<formhash> :hash of the form
					<cookie> : the id of cookie
					<exceptresult> :the result of except
		@return  :
		@pkgpath :
		@remark  :
		@author  :  Jason
		@history :  Create 2016/04/06
		'''
		result=-1
		payload = {
			"iGameId": iGameId,
			"iPlayTypeId": iPlayTypeId,
			"sBetCode": sBetCode,
	        "iBetCount": nums,
	 #       "fAmount": fAmount,
			"iType": iType,
			"sOpenNum": sOpenNum,
	 #       "fPrize": fPrize,
		}
		#print "payload   is  ",payload
		if sPosition != None:
			payload["sPosition"] = sPosition


		src2 = ""
		for key in sorted(payload.keys()):
			src2 += str(payload[key])
		#payload = json.dumps(payload, sort_keys=True, separators=(',', ':'))



		src2=src2 + String_token
		#print src2,src2.decode('raw_unicode_escape')
		#token1=hashlib.md5(src2.decode('raw_unicode_escape')).hexdigest()
		token1 = hashlib.md5(src2).hexdigest()

		payload["Token"]=token1


		payload=json.dumps(payload,sort_keys=True,separators=(',',':'))

		#print  payload

		function_name = sys._getframe().f_code.co_name
		post_url = sUrl + function_name + "/"
		response = requests.request('POST', post_url, data=payload)

		b=response.json()    #{'ret': '\u53c2\u6570\u975e\u6cd52'}

		return b

    def check_paicai(self,list1):
		result = -1
		h = len(list1) - 10
		#print 'h___--->>',h
		iGameId = int(list1[2])
		iPlayTypeId = int(list1[3])
		iType = int(list1[4])
		sOpenNum = list1[5]
		sBetCode = list1[6]
		nums = int(list1[7])
		if type(sOpenNum)==float:
			sOpenNum=int(sOpenNum)
		if type(sBetCode)==float:
			sBetCode=int(sBetCode)
		#print "ok is  ssss" ,sOpenNum,sBetCode
		BonusResult = int(list1[8])
		iWinCount = list1[9]
		if h > 0:
			iWinCountList = list1[-h:]
			#print "iWinCountList  is  ", iWinCountList
		#print type(iWinCount)
		if type(iWinCount) !=str :
			iWinCount = int(iWinCount)
		# if iWinCount.isdigit():
		# 	iWinCount = int(iWinCount)
		response_dict = self.TestBonus(iGameId, iPlayTypeId, sBetCode,nums, iType, sOpenNum)
		#print str(response_dict).decode('raw_unicode_escape')
		#print type(BonusResult), type(iWinCount)
		if BonusResult == response_dict["BonusResult"] == 3:
			result = 0
		elif BonusResult == response_dict["BonusResult"] == 2 and iWinCount == response_dict["iWinCount"]:
			if h > 0:
				for i in range(h):
					if int(iWinCountList[i]) > 0 :
						#print 'iiiiiiiii----->',i
						#continue
						if  int(iWinCountList[i]) == response_dict["iWinCount" + str(i+1)]:
							result = 0
						else:
							result = -1
							print "The BonusResult is %s, the iWinCount is %s ,but the response is %s" % (BonusResult, iWinCount, response_dict)
							break
					else:
						result = 0
			else:
				result = 0
		elif BonusResult == response_dict["BonusResult"] == 1:
			result = 0
		else:
			print "The BonusResult is %s, the iWinCount is %s ,but the response is %s" % (BonusResult, iWinCount, str(response_dict).decode('raw_unicode_escape'))
		return result

    def check_paicai_position(self,list1):
		result = -1
		h=len(list1) - 11
		#print "h is ",h
		iGameId = int(list1[2])
		iPlayTypeId = int(list1[3])
		iType = int(list1[4])
		sPosition = list1[5]
		sOpenNum = list1[6]
		sBetCode = list1[7]
		nums = list1[8]
		if type(sOpenNum)==float:
			sOpenNum=int(sOpenNum)
		if type(sBetCode)==float:
			sBetCode=int(sBetCode)
		#print sBetCode,list1[7]
		#print "iGameId, iPlayTypeId, sBetCode, iType, sOpenNum",iGameId, iPlayTypeId, sBetCode, iType, sOpenNum
		BonusResult = int(list1[9])
		iWinCount = list1[10]
		if h > 0:
			iWinCountList=(list1[-h:])
			#print "iWinCountList  is  " ,iWinCountList
		# print type(iWinCount)
		if type(iWinCount) != str:
			iWinCount = int(iWinCount)
		# if iWinCount.isdigit():
		# 	iWinCount = int(iWinCount)
		response_dict = self.TestBonus(iGameId, iPlayTypeId, sBetCode,nums, iType, sOpenNum, sPosition)
		#print str(response_dict).decode('raw_unicode_escape')
		# print type(BonusResult), type(iWinCount)
		if BonusResult == response_dict["BonusResult"] == 3:
			result = 0
		elif BonusResult == response_dict["BonusResult"] == 2 and iWinCount == response_dict["iWinCount"]:
			if h>0:
				for i in range(h):
					if int(iWinCountList[i]) > 0 :
						#continue
						if int(iWinCountList[i]) == response_dict["iWinCount" + str(i+1)]:
							result = 0
						else:
							result = -1
							print "The BonusResult is %s, the iWinCount is %s ,but the response is %s" % (BonusResult, iWinCount, str(response_dict).decode('raw_unicode_escape'))
							break
					else:
						result = 0
			else:
				result = 0
		elif BonusResult == response_dict["BonusResult"] == 1:
			result = 0
		else:
			print "The BonusResult is %s, the iWinCount is %s ,but the response is %s" % (BonusResult, iWinCount, response_dict)
		return result

    def TestBonus_lhc(self,methodid,iType,sBetCode,sOpenNum):
		#"http://www.700test.com/sixLotPaicai/test.html?openNumber=01|02|03|04|05|06|49&codes=49&methodid=294&type=特码"
		post_url=sUrl+"sixLotPaicai/test.html"
		payload = {
			"openNumber": sOpenNum,
			"codes": sBetCode,
			"methodid": methodid,
			"type": iType,
		}
		#payload =url+"sixLotPaicai/test.html?openNumber="+sOpenNum+"&codes="+sBetCode+"&methodid="+methodid+"&type="+iType
		#payload = json.dumps(payload, sort_keys=True, separators=(',', ':'))
		#print payload
		#print str(payload).decode('raw_unicode_escape')
		#print str(payload).decode('')

		response = requests.request('Post', post_url, data=payload)

		b = response.json()    #{'ret': '\u53c2\u6570\u975e\u6cd52'}

		return b

    def check_paicai_lhc(self, list1):
		#iGameId = int(list1[2])
		methodid = int(list1[3])
		iType = str(list1[4])
		sOpenNum = list1[5]
		sBetCode = list1[6]
		# if type(sOpenNum) == float:
		# 	sOpenNum = int(sOpenNum)
		if type(sBetCode) == float:
			sBetCode = int(sBetCode)
		# print "ok is  ssss" ,sOpenNum,sBetCode
		BonusResult = int(list1[7])
		#print str(list1	).decode('raw_unicode_escape')
		response_dict = self.TestBonus_lhc(str(methodid),iType,str(sBetCode),sOpenNum)
		#print str(response_dict).decode('raw_unicode_escape')
		# print type(BonusResult), type(iWinCount)
		if BonusResult == response_dict["status"]:
			result = 0
			print "The except is %s,and response is %s" % (BonusResult, str(response_dict).decode('raw_unicode_escape'))
		else:
			result = -1
			print "The except is %s,but response is %s" % (BonusResult, str(response_dict).decode('raw_unicode_escape'))
		return result

def sql_update_list(conn,sql_list):
    cursor = conn.cursor()

    sql_result=[[] for i in range(len(sql_list))]

    #for i in range(len(sql_old)):
    for j in range(len(sql_list)):
        sql=sql_list[j]
        #sql = "select iUserKey,fBalance from tuser where sUserid='"+str(user_id)+"'"
        cursor.execute(sql.decode('utf8'))
        #print 'sql---->>>>>', sql, [sql.decode('utf8')]
        cursor.commit()

    cursor.close()
    #return sql_result

def sql_update_one(conn,sql_one):
	"""
	执行单条语句的UPDATE或者DELETE操作。
	:param conn: 已有的数据库连接。
	:param sql_one: 字符串类型的sql语句。
	:return: 无返回值
	"""
	cursor = conn.cursor()
	cursor.execute(sql_one.decode('utf8'))
	conn.commit()
	conn.close()

def sql_query(conn, sql):
	cursor = conn.cursor()

	# sql_list="select * from trebateset ;","select * from tbank ;"
	# sql_result=[]

	cursor.execute(sql.decode('utf8'))
	sql_result = cursor.fetchall()
	cursor.close()
	return sql_result

def sql_query_list(conn,sql_list):
    # conn = pymssql.connect(host='10.10.11.243', user='Lottery01', password='JDhag*7d9aD',
    #         database='Jason02', charset='utf8', port=1433, as_dict=False)  cursorclass = MySQLdb.cursors.DictCursor
    #conn = pyodbc.connect("DSN=700test;UID=Lottery01;PWD=JDhag*7d9aD")
    #conn = pyodbc.connect("DRIVER={SQL Server};SERVER=10.10.11.243;PORT=1433;DATABASE=Jason02;UID=Lottery01;PWD=JDhag*7d9aD")
        # pyodbc.connect(host='10.10.11.243', user='Lottery01', password='JDhag*7d9aD',
        #     database='Jason02', charset='utf8', port=1433, as_dict=False,cursorclass = MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    #cursor = conn.cursor(cursorClass=pyodbc.cursors.DictCursor)

    # user_key=52235
    # user_id='jtest'
    #
    #
    GUserNameA = 'jtest'
    # GPassWordA = 'j12345'
    # game_id=18
    # each_money = 41


    '''
    sql_old=[[],[],[]]
    sql_old=[[insert],[delete],[update]]    #增加、删除、修改  如果有多条sql 就用逗号隔开；  操作前要查询的结果
    sql_new=[[insert],[delete],[update]]    #增加、删除、修改  如果有多条sql 就用逗号隔开；  操作后要查询的结果

    原始语句：
    select iUserKey,fBalance from tuser where sUserid='jtest';
    select fBalance from tuser where sUserid='jtest';
    select count(*) from tbet a  , tuser b where  a.iGameId=18 and a.iUserKey= b.iUserKey and b.sUserid='jtest' and a.fAmount=41 ;

    转化后的语句：
    "select iUserKey,fBalance from tuser where sUserid='"+str(GUserNameA)+"';"
    "select count(*) from tbet a  , tuser b where  a.iGameId="+ str(game_id)+" and a.iUserKey= b.iUserKey and b.sUserid='jtest' and a.fAmount="+str(each_money)+" ;"

    '''

    #sql_list=["select * from trebateset ;","select * from tbank ;"]
    sql_result=[[] for i in range(len(sql_list))]
    #print sql_result
    #sql_list=["select name from syscolumns where id = object_id('tpayset')  ;","select * from tpayset ;"]
    #sql_old=["select * from tuser where sUserid='"+str(GUserNameA)+"';"]
    # sql_old=[["select count(*) from tbet a  , tuser b where  a.iGameId="+ str(game_id)+" and a.iUserKey= b.iUserKey and b.sUserid='jtest' and a.fAmount="+str(each_money)+" ;"],
    #          ["select count(*) from tbet a  , tuser b where  a.iGameId="+ str(game_id)+" and a.iUserKey= b.iUserKey and b.sUserid='jtest' and a.fAmount="+str(each_money)+" ;"],
    #          ["select iUserKey,fBalance from tuser where sUserid='"+str(GUserNameA)+"';","select * from tuser where sUserid='"+str(GUserNameA)+"';"]]
    #sql_new=sql_old
    #sql_old=[["select iUserKey,fBalance from tuser where sUserid='"+str(GUserNameA)+"';","select iUserKey,fBalance from tuser where sUserid='"+GUserNameA+"';"],["select count(*) from tbet a  , tuser b where  a.iGameId="+ str(game_id)+" and a.iUserKey= b.iUserKey and b.sUserid='jtest' and a.fAmount="+str(each_money)+" ;","select count(*) from tbet a  , tuser b where  a.iGameId="+ str(game_id)+" and a.iUserKey= b.iUserKey and b.sUserid='jtest' and a.fAmount="+str(each_money)+" ;"],[]]
    #select iUserKey,fBalance from tuser where sUserid='jtest' and iUserKey= 52235;

    #for i in range(len(sql_old)):
    for j in range(len(sql_list)):
        sql=sql_list[j]
        #sql = "select iUserKey,fBalance from tuser where sUserid='"+str(user_id)+"'"
        cursor.execute(sql.decode('utf8'))
        #print 'sql---->>>>>', sql, [sql.decode('utf8')]
        sql_result[j] = cursor.fetchall()
        #results = cursor.fetchall()
        #results1 = cursor.fetchone()
        #print 'results---->>>',sql_result[j]
        #print 'results1---->>>', results1
        # for row in results:
        #     print row

        #row1 = cursor.execute("select count(*) as user_count from tpayset").fetchone()
        #print('{} users'.format(row1.user_count))
    cursor.close()
    return sql_result


def sql_query_dict(conn,sql_list):
    #conn = pyodbc.connect("DRIVER={SQL Server};SERVER=10.10.11.243;PORT=1433;DATABASE=Jason02;UID=Lottery01;PWD=JDhag*7d9aD")
    cursor = conn.cursor()

    #sql_list=["select * from trebateset ;","select * from tbank ;"]

    sql_result=[[] for i in range(len(sql_list))]
    #print sql_result

    #for i in range(len(sql_old)):
    for j in range(len(sql_list)):
        sql=sql_list[j]

        #sql = "select iUserKey,fBalance from tuser where sUserid='"+str(user_id)+"'"
        #print 'sql-->',sql
        #cursor.execute(sql)
        #cursor = cursor.execute(sql)
        cursor.execute(sql.decode('utf8'))      #支持where 条件下有中文
        #print 'sql---->>>>>', sql, [sql.decode('utf8')]
        columns = [column[0] for column in cursor.description]
        #print columns
        #print len(columns)
        #['name', 'create_date']
        #results = []
        for row in cursor.fetchall():
            sql_result[j].append(dict(zip(columns, row)))

    cursor.close()
    return sql_result

def sql_query_dict_one(conn,sql_one):
    #conn = pyodbc.connect("DRIVER={SQL Server};SERVER=10.10.11.243;PORT=1433;DATABASE=Jason02;UID=Lottery01;PWD=JDhag*7d9aD")
    cursor = conn.cursor()

    #sql_list=["select * from trebateset ;","select * from tbank ;"]

    #sql_result=[[] for i in range(len(sql_list))]
    #print sql_result

    #for i in range(len(sql_old)):

    #sql = "select iUserKey,fBalance from tuser where sUserid='"+str(user_id)+"'"
    #print 'sql-->',sql
    #cursor.execute(sql)
    #cursor = cursor.execute(sql)
    cursor.execute(sql_one.decode('utf8'))      #支持where 条件下有中文
    #print 'sql---->>>>>', sql, [sql.decode('utf8')]
    columns = [column[0] for column in cursor.description]
    #print columns
    #print len(columns)
    #['name', 'create_date']
    sql_result = []
    for row in cursor.fetchall():
        sql_result.append(dict(zip(columns, row)))
    #json.dumps(sql_result)  d = decimal.Decimal('3.5')
#  print simplejson.dumps([d], default=json_encode_decimal)
#     print 'sql_result0---',simplejson.dumps(sql_result, default=json_encode_decimal),type(simplejson.dumps(sql_result, default=json_encode_decimal))
    #conn.close()
    aaaa = simplejson.dumps(sql_result, default=json_encode_decimal)     #支持decimal 转化为数字       转化为字符串
#     aaaa = simplejson.dumps(sql_result)     #支持decimal 转化为数字       转化为字符串
#     bbbb = json.loads(aaaa[1:len(aaaa)-1])
    bbbb = json.loads(aaaa)        #转化为json
#     bbbb = sql_result
#     print 'bbbb----',bbbb
    #cursor.close()
    return bbbb

iUserKey=52235   #jtest
#iUserKey=54399  #jtest403
CurUserKey=iUserKey
#CurPassword='j12345'
CurPassword='d6720b4f645d96c3f7e346c39d39dc7f'
From=1     #    1 PC,2 WAP,3 APP-Android，4 APP-IOS，5 APP-Other
IP='10.10.15.135'    #当前登录者的IP地址
String_token='3cbbbc5ff11b4d418d7a9b7c394c78a8'    #预生产环境 token 要添加的string
#String_token='4cbbbc5ff11b4d418d7a9b7c394c78a8'    #测试环境 token 要添加的string
# payload={"CurUserKey":CurUserKey,
# #         "CurPassword":CurPassword,
# #          "From":From,
#          "IP":IP,}
#     payload["curUserKey"] = CurUserKey
#     payload["CurPassword"] = CurPassword
#     payload["From"] = From
#     payload["IP"] = IP
    
sUrl="http://119.9.124.151:9998/"    #预生产环境url接口
# sUrl="http://10.10.11.246:2000/"   #自动化环境url接口
#sUrl="http://10.10.11.245:2000/"   #自动化环境url接口
#sUrl="http://10.10.14.227:9988/"   #测试环境url接口

sUrl_web="http://lotf.jwoquxoc.com/"


# conn = pyodbc.connect("DRIVER={SQL Server};CHARSET=UTF8;SERVER=119.9.124.151,3344;PORT=1433;DATABASE=CAT01;UID=Lottery01;PWD=adjIUEd8&D817dpA")   #600vip
conn = pymssql.connect(server='119.9.124.151', port='3344', user='Lottery01', password='adjIUEd8&D817dpA', database='CAT01', charset='UTF8' )

# sql_list=["select * from trebateset ;","select * from tbank ;"]
# 
# bb=sql_query_list(conn,sql_list)
# print bb

# def check_hongbao_code(conn):
#     sql_id_date_code=["select skey,igameid,sgameperiod,sluckycode from TLuckyMoneyPeriod where dEndTime is not null and sLuckyCode is not null ORDER BY dEndTime desc ;"]
#     cc=sql_query_dict(conn,sql_id_date_code)
# 
#     for i in range(len(cc[0])):
#         sum = 0
#         n = 100
#         sql_list=["SELECT TOP 50 (convert(varchar(12),dbet,114)) FROM TLuckyMoneyDetail WHERE iGameId = %s AND sGamePeriod = %s ORDER BY iIndex DESC ;" % (cc[0][i]['igameid'],cc[0][i]['sgameperiod'])]
#         bb=sql_query_list(conn,sql_list)
#         a=bb[0]
#         b=a
# 
#         for j in range(len(a)):
#             b[j]=''.join(a[j][0].split(':'))
#             sum += int(b[j])
#         #print cc[0][i]['sluckycode'],type(cc[0][i]['sluckycode'])
#         if sum%n +10000001 == long(cc[0][i]['sluckycode']):
#             pass
#             #print 'the result of %s is Pass. the calc value is %s, and the shiji value is %s'  % (cc[0][i]['skey'],sum%n +10000001,cc[0][i]['sluckycode'] )
#         else:
#             print 'the result of %s is Fail. the calc value is %s, and the shiji value is %s'  % (cc[0][i]['skey'],sum%n +10000001,cc[0][i]['sluckycode'] )
#     print '000000000'        
#check_hongbao_code(conn)


# sql_list=["select  top 1000 sGamePeriod from tgameperiod where igameid=10  and sOpenNum in ('2|4|5','3|4|5','3|5|6','1|1|3')  and dRealOpen is not null order by sGamePeriod desc ;"]
# # 
# bb=sql_query_list(conn,sql_list)
# print 'ok0909'
# print bb
# 
# test1=bb[0]
# for i in range(len(test1)-3):
# 	if (int(test1[i][0]) - int(test1[i+1][0]) == 1) and (int(test1[i+1][0]) - int(test1[i+2][0]) == 1) and (int(test1[i+2][0]) - int(test1[i+3][0]) == 1) :
# 		print 'okkk'
# 		print int(test1[i][0])
	

# sql_list=["select iUserKey,fBalance from tuser where iUserKey=52235 ;"]
#  
# bb = sql_query_dict(conn,sql_list)
# print bb 



