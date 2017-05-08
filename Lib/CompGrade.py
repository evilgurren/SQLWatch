#! /usr/bin/env python
# coding: utf-8

import re

from GlobalValue import GlobalValuer
from antlr4.error.ErrorListener import ErrorListener

KETER = [['\'', '--', '@@', '/*', '*/', '#'],\
		 ['select', 'union', 'and', 'or', 'information_schema']]

EUCLID = [['||', '=', '>', '<', '(', ')'],\
		  ['create', 'from', 'order by', 'group by', 'table', 'column',\
		   'rand', 'floor', 'version', 'columns', 'tables', 'schemata',\
		   'user_privileges', 'schema_privileges', 'table_privileges',\
		   'column_privileges', 'columns']]

class CompGrader(object):
	"""对语法分析器报错结果及用户原始payload进行综合评分."""
	def __init__(self, payload, msg):
		# 记录原始payload
		self.payload = payload
		# 语法分析器报错结果
		self.msg = msg

	def __grading(self, payload, keyword, grade, times):
		"""对payload进行keyword类评分.

		payload是进行评分的string变量.

		keyword是包含字符和关键字的list变量.

		grade是每次增加的小分.

		times是最多可重复评分的次数.

		返回值为int型评分.
		"""

		score = 0
		n = 0
		for op in keyword[0]:
			if op in payload:
				score += grade
		for key in keyword[1]:
			regex = r'\b%s\b'
			regex = regex % key
			m = re.findall(regex, payload)
			if m:
				score += grade
				n += 1
				if n >= times:
					return score
		return score

	def __getscore(self, payload):
		"""对payload进行综合评分.

		payload是进行综合评分的string变量.

		返回值为int型综合评分.
		"""

		return self.__grading(payload, KETER, 5, 1) + self.__grading(payload, EUCLID, 2, 2)

	def compgrade(self):
		"""根据msg对payload进行综合评分.

		payload是进行综合评分的dict变量.

		msg是语法分析器的报错信息.

		返回值为int型最终评分.
		"""

		self.score = 0
		if self.msg:
			# 当语法分析器报错时，即语句不符合SQL语法不会被DBMS执行，因此不是注入，评分设为-1
			self.score = -1
			return self.score;
		else:
			# 未报错时，也不能判断不是注入，需要对payload进行综合评分
			self.score = self.__getscore(self.payload)
			return self.score


class MyErrorListener(ErrorListener):
	def __init__(self):
		super(MyErrorListener, self).__init__()
		self.glovar = GlobalValuer()

	def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
		self.glovar.set_msg(msg)
	def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
		pass
	def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
		pass
	def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
		pass