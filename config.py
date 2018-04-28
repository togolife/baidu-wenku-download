#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 日志定义
log_dir = 'log'
log_name = 'wenku-download.log'

# 百度文库get请求头
reqHeaderBDWK = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip,deflate,br',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Connection': 'keep-alive',
	'DNT': '1',
	'HOST': 'wkbos.bdimg.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/'
	}

docTypeBDWK = {
	'0': '',
	'1': 'doc',
	'2': 'xls',
	'3': 'ppt',
	'4': 'docx',
	'5': 'xlsx',
	'6': 'pptx',
	'7': 'pdf',
	'8': 'txt',
	'9': 'wps',
	'10': 'et',
	'11': 'dps',
	'12': 'vsd',
	'13': 'rtf',
	'14': 'pot',
	'15': 'pps',
	'16': 'epub'
	}

# 下载文档保存路径
file_dir = 'down'
