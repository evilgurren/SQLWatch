# coding:utf-8

global msg
msg = ''
class GlobalValuer(object):
	def set_msg(self, input_msg):
		global msg
		msg = input_msg

	def get_msg(self):
		global msg
		return msg