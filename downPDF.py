#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# pdf操作库reportlab
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from PIL import Image  # PIL是python内部模块，不是reportlab库的

import config
import log

logger = log.Log(config.log_dir, config.log_name)

class DownPDF(object):
	def __init__(self, fileDir, url, info):
		self.fileDir = './' + fileDir + '/'
		self.URL = url
		self.WkInfo = info
		if not os.path.exists(self.fileDir):
			os.mkdir(self.fileDir)

	# 获取每页URL
	@staticmethod
	def geturl(urls, index):
		for url in urls:
			if url['pageIndex'] == index:
				return url['pageLoadUrl']
		return ''

	def down(self):
		urlBase = self.URL[self.URL.rfind('/') + 1 : self.URL.find('.html')]
		reqHeader = config.reqHeaderBDWK
		reqHeader['Referer'] = self.URL
		i = 1
		first = 0
		pdfFileName = self.fileDir + self.WkInfo['title'] + '.' + self.WkInfo['docType']
		while i <= self.WkInfo['totalPageNum']:
			pngUrl = DownPDF.geturl(self.WkInfo['htmlUrls']['png'], i)
			if len(pngUrl) == 0:
				logger.error('下载文档失败，查找URL失败！')
				return False
			pngUrl = pngUrl.replace('\\', '')
			pngUrl = pngUrl.replace(' ', '%20')
			req = urllib2.Request(pngUrl, None, reqHeader)
			res = urllib2.urlopen(req)
			res = res.read()
			imgFileName = self.fileDir + urlBase + '-'+str(i)+'.png'
			fp = open(imgFileName, 'wb')
			fp.write(res)
			fp.close()
			if first == 0:
				first = 1
				img = Image.open(imgFileName)
				pdfHandler = canvas.Canvas(pdfFileName, pagesize=img.size)
				img.close()
			pdfHandler.drawImage(imgFileName, 0, 0)
			pdfHandler.showPage()
			os.remove(imgFileName)
			if i == self.WkInfo['totalPageNum']:
				pdfHandler.save()
			i += 1
		return True