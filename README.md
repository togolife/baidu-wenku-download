# baidu-wenku-download
下载百度文库文档

目前只简单实现了PDF,DOC,DOCX,TXT格式的文档下载

依赖库：
# pdf操作库
pip install reportlab

# word操作库
pip install python-docx

# 下载文库方法
比如要下载https://wenku.baidu.com/search?word=%B1%C8%CC%D8%B1%D2&lm=5&od=0&page=search&sort_type=0&type=sort_click&org=0 这篇文章
执行： python main.py https://wenku.baidu.com/search?word=%B1%C8%CC%D8%B1%D2&lm=5&od=0&page=search&sort_type=0&type=sort_click&org=0  即可
下载成功后会保存在down目录下，下载过程的日志在log目录下
