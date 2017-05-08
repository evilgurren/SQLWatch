#! /usr/bin/env python
# coding:utf-8

import sys

from antlr4 import *
from Lib.RecDecode import *
from Lib.CompGrade import *
from Lib.SQLLexer import SQLLexer
from Lib.SQLParser import SQLParser
from Lib.GlobalValue import GlobalValuer
from Lib.SQLParserVisitor import SQLParserVisitor

class SQLWatcher(object):
	"""SQL防注入检测引擎"""

	def watch(self, url):
		"""封装成类，方便调用"""

		res = {}
		glovar = GlobalValuer()
		recd = RecDecoder(url)

		recd_dict = recd.getparams()
		payload_dict = recd.decvalue(recd_dict)
		for key in payload_dict:
			glovar.set_msg('')
			suffix = ''' select a from b where c='%s' '''
			payload = payload_dict[key]
			sql = suffix % payload
			input = InputStream(sql)
			lexer = SQLLexer(input)
			stream = CommonTokenStream(lexer)
			parser = SQLParser(stream)
			parser._listeners = [MyErrorListener()]
			tree = parser.sql()
			v = SQLParserVisitor()
			v.visit(tree)
			grader = CompGrader(payload, glovar.get_msg())
			score = grader.compgrade()
			if score >= 10:
				res[key+'='+payload] = True
			else:
				res[key+'='+payload] = False
		return res


def main():
	url = '''a=123&b=sdfhofrom from from = () select union FHOI&c=1'&d=1' oR '1'='1&e=and 0<>(select user_blank>_name()--'''

	res = {}
	glovar = GlobalValuer()
	recd = RecDecoder(url)
	recd_dict = recd.getparams()
	payload_dict = recd.decvalue(recd_dict)
	for key in payload_dict:
		glovar.set_msg('')
		suffix = ''' select a from b where c='%s' '''
		payload = payload_dict[key]
		sql = suffix % payload
		input = InputStream(sql)
		lexer = SQLLexer(input)
		stream = CommonTokenStream(lexer)
		parser = SQLParser(stream)
		parser._listeners = [MyErrorListener()]
		tree = parser.sql()
		v = SQLParserVisitor()
		v.visit(tree)
		grader = CompGrader(payload, glovar.get_msg())
		score = grader.compgrade()
		res[key+'='+payload] = score
	
	for key in res:
		print key, res[key]

if __name__ == '__main__':
    main()