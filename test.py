#! /usr/bin/env python
# coding:utf-8

from SQLWatch import SQLWatcher

RES = {}

def showSQLi(Dict):
	flag = True
	for url in Dict:
		print 'payload: %s' % url
		print 'SQLi:'
		for l in Dict[url]:
			if l[1]:
				flag = False
				print '\t%s' % l[0]
		if flag:
			print '\tthis payload is safe!'
		print '\n'


if __name__ == '__main__':
	sqlw = SQLWatcher()

	with open('test.txt', 'r') as f:
		urls = f.readlines()
	for url in urls:
		m = []
		res = sqlw.watch(url.strip())
		for key in res:
			m.append([key, res[key]])
		RES[url.strip()] = m

	showSQLi(RES)