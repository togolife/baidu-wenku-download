#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

class Log(object):
	def __init__(self, dirName, fileName):
		dirName = './' + dirName
		self.fileName = dirName + '/' + fileName
		if not os.path.exists(dirName):
			os.mkdir(dirName)

	def __log(self, level, message):
		curr_time = int(time.time())
		time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(curr_time))
		message = time_str + " [" + level + "] " + message + "\n"
		fp = open(self.fileName, 'a')
		fp.write(message)
		fp.close()

	def info(self, message):
		self.__log("INFO", message)

	def error(self, message):
		self.__log("ERROR", message)

	def warn(self, message):
		self.__log("WARNING", message)

# test
if __name__ == '__main__':
	log = Log('log', 'wenku-download.log')
	log.info("测试开始")
	log.error("发生错误了")
	log.warn("龟拳警告")
