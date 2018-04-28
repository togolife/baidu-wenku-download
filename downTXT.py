#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib2
import time
import json
import gzip
from cStringIO import StringIO
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import config
import log

logger = log.Log(config.log_dir, config.log_name)

def gzip_uncompress(c_data):
	buf = StringIO(c_data)
	f = gzip.GzipFile(mode = 'rb', fileobj = buf)
	try:
		r_data = f.read()
	finally:
		f.close()
	return r_data

class DownTXT(object):
	getDocInfo = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb'
	downDocUrl = 'https://wkretype.bdimg.com/retype/text/'

	def __init__(self, fileDir, url, info):
		self.fileDir = './' + fileDir + '/'
		self.URL = url
		self.WkInfo = info
		if not os.path.exists(self.fileDir):
			os.mkdir(self.fileDir)

	def down(self):
		docID = self.URL[self.URL.rfind('/') + 1 : self.URL.find('.html')]
		reqHeader = config.reqHeaderBDWK
		reqHeader['Referer'] = self.URL
		reqHeader['HOST'] = 'wenku.baidu.com'
		# 获取文档信息
		# url: https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=60108d36336c1eb91a375dd2&t=1524896355038&_=1524896354264
		ms = int(time.time() * 1000)
		reqUrl = DownTXT.getDocInfo + '&doc_id=' + docID + '&t=' + str(ms+2000) + '&_=' + str(ms)
		logger.info(reqUrl)
		req = urllib2.Request(reqUrl, headers=reqHeader)
		response = urllib2.urlopen(req)
		res = response.read()
		logger.info('响应头信息：' + str(response.headers))
		#if response.headers['Transfer-Encoding'] == 'chunked':
		#	res = decode_chunked(res)
		if response.headers['Content-Encoding'] == 'gzip':
			res = gzip_uncompress(res)
		logger.info('getDocInfo 响应信息： ' + res)
		docInfo = res[res.find('(')+1 : res.rfind(')')]
		docInfo = json.loads(docInfo)
		# 获取文档内容
		reqUrl = DownTXT.downDocUrl + docID + '?type=txt&callback=cb&pn=1&rn=' + str(self.WkInfo['totalPageNum']) +\
				 '&rsign=' + docInfo['rsign'] + '&_=' + str(ms) + docInfo['md5sum']
		reqHeader['HOST'] = 'wkretype.bdimg.com'
		req = urllib2.Request(reqUrl, headers=reqHeader)
		response = urllib2.urlopen(req)
		res = response.read()
		if response.headers['Content-Encoding'] == 'gzip':
			res = gzip_uncompress(res)
		docContent = res[res.find('(')+1 : res.rfind(')')]
		docContent = json.loads(docContent)
		# 保存内容到txt文件
		txtFileName = self.fileDir + self.WkInfo['title'] + '.' + self.WkInfo['docType']
		fp = open(txtFileName, 'w')
		for dc in docContent:
			fp.write(dc['parags'][0]['c'])
		fp.close()
		return True