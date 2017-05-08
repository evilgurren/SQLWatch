#! /usr/bin/env python
# coding:utf-8

import sys
import base64
import urllib
import string
import urlparse

BASE64CODE = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
			  'Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f',
			  'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
			  'w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/',
			  '=','\n']

class RecDecoder(object):
	"""解析用户GET|POST传入的数据，取出各个参数值并进行递归解码."""
	def __init__(self, url):
		# 需要解析的url
		self.url = url
		# 递归解码出的payload
		self.payload = {}

	def __isurl(self, url):
		"""检查传入url是否规范.

		url是需要进行合法性检查的string变量.

		若：
			为真，返回url.
			为假，返回False.
		"""

		# 先对传入url进行url递归解码
		url = self.__recurldecode(url)
		# 记录'='符号出现位置
		list_1 = []
		# 记录'&'符号出现位置
		list_2 = []
		for i in range(len(url)):
			if url[i] == '=':
				list_1.append(i)
			elif url[i] == '&':
				list_2.append(i)
		if len(list_1) == len(list_2) + 1:
			for j in range(len(list_2)):
				if list_2[j] < list_1[j] or list_2[j] > list_1[j+1]:
					return False
			return url
		return False

	def __recurldecode(self, rawstring):
		"""对数据进行url递归解码.

		rawstring是进行递归解码的string变量.

		返回值为递归解码后的string.
		"""

		decstring = urllib.unquote(rawstring)
		if decstring != rawstring:
			return self.__recurldecode(decstring)
		else:
			return decstring


	def __recb64decode(self, rawstring):
		"""对数据进行base64递归解码.

		rawstring是进行递归解码的string变量.

		返回值为递归解码后的string.
		"""

		if (rawstring != '' and \
			self.__char_check(rawstring) and \
			self.__length_check(rawstring) and \
			self.__equalsign_check(rawstring)):
			decstring = base64.b64decode(rawstring)
			for _ in decstring:
				if _ not in string.printable:
					return rawstring
			try:
				tmp = base64.b64decode(decstring)
			except:
				return decstring
			return self.__recb64decode(tmp)
		else:
			return rawstring

	def __char_check(self, rawstring):
		"""检查字符串是否只包含规定字符.

		rawstring是需要判断的string变量.

		返回值为布尔数.
		"""

		for c in rawstring:
			if c not in BASE64CODE:
				return False
		return True

	def __length_check(self, rawstring):
		"""检查字符串长度是否为4的倍数.

		rawstring是需要判断的string变量.

		返回值为布尔数.
		"""

		if len(rawstring) % 4 == 0:
			return True
		else:
			return False

	def __equalsign_check(self, rawstring):
		"""检查字符串包含的'='是否只存在于后缀且数量不大于3.

		rawstring是需要判断的string变量.

		返回值为布尔数.
		"""

		if rawstring[:-2].find('=') == -1:
			return True
		else:
			return False

	def __getquery(self, parsedtuple):
		"""从parsedtuple中获取query字符串.

		parsedtuple是包含query的string变量.

		返回值为query请求的string变量.
		"""
		if parsedtuple.query:
			if parsedtuple.fragment:
				return parsedtuple.query + '#' + parsedtuple.fragment
			else:
				return parsedtuple.query
		elif parsedtuple.path:
			if parsedtuple.fragment:
				return parsedtuple.path + '#' + parsedtuple.fragment
			else:
				return parsedtuple.path
		else:
			return False

	def getparams(self):
		"""解析用户传入数据，取出其中的键值对.

		无实参.

		返回值为参数与值一一对应的dict.
		"""

		# 存放query语句
		query = ''
		# 存放参数与对应值的字典 
		query_dict = {}

		# url合法性检测
		result_q = self.__isurl(self.url)
		if result_q:
			self.url = result_q

		# 使用urlparse对url进行拆分
		parsedtuple = urlparse.urlparse(self.url)
		# print parsedtuple
		# 根据GET或POST的不同取出query
		query = self.__getquery(parsedtuple)
		if query:
			# 根据&符分隔query各参数
			query_list = query.split('&')

			# 取出参数和值存入字典
			for key_value in query_list:
				# 由于是已分隔好的键值对，因此只分割一次键值
				tmp = key_value.split('=', 1)
				# 存入字典
				query_dict[tmp[0]] = tmp[1]
			return query_dict
		else:
			print 'Input Error!!!' + '\n'
			sys.exit()

	def decvalue(self, query_dict):
		"""对键值对的每个value进行递归解码

		query_dict是包含需要解码value的字典

		返回值为完成递归解码后的字典
		"""

		# 对各个值进行base64和url递归解码
		for key in query_dict:
			# 先进行base64递归解码
			query_dict[key] = self.__recb64decode(query_dict[key])
			# 以防万一进行第二次url递归解码
			query_dict[key] = self.__recurldecode(query_dict[key])
			# 转为小写字母，存入self.payload中
			self.payload[key] = query_dict[key].lower()
		return self.payload


def main():
	url = '''
	/SEARCH/SUPPLIES?a=JTIyK29yKyUyMjElMjIlM0QlMjIx&b=c
	'''
	recd = RecDecoder(url)
	recd_dict = recd.getparams()
	payload = recd.decvalue(recd_dict)
	for i in payload:
		print i, payload[i]

if __name__ == '__main__':
	main()