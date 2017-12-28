# cnblogs
使用scrapy对博客园的博客进行抓取
* 主要是对博客园的网页进行翻页抓取
---------------------------------------------
* cnblogsspider.py是用offset偏移量实现翻页的规则
* cnblogsspiderv2 是用xpath找出下一页的标签，然后实现翻页
* cnblogsspiderv3 是用正则表达式，匹配出标签元素，进行翻页处理

------------------------------------------------
* git clone https://github.com/danwenxuan/cnblogs
* pip install scrapy 
* python starts.py
