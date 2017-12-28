# -*- coding: utf-8 -*-
import scrapy
import cnblogs.items
from  scrapy import Selector
from scrapy.linkextractors import LinkExtractor #提取链接
from  scrapy.spiders import CrawlSpider,Rule #循环抓取规则

class CnblogsspiderSpider(CrawlSpider):
    name = 'cnblogsspiderV3'
    allowed_domains = ['cnblogs.com']
    offset=0
    start_urls = ['http://www.cnblogs.com/yincheng01/default.html?page=2']
    rules = (
        #正则表达式转义字符
        Rule(LinkExtractor(allow="http:\/\/www.cnblogs.com\/yincheng01\/default.html\?page=\d+"),follow=True, callback="parse_content"),  # 子链接
        # Rule(LinkExtractor(allow=r"http://www.cnblogs.com/yincheng01/default.html?page=\d+"), follow=True,
        #      callback="parse_content"),  # 子链接
    )
    # parse执行一次
    #parse_content，正则表达式提取了多个URL，执行多少次
    def parse_content(self, response):
        papers = response.xpath(".//*[@class=\"day\"]")
        titlelist=[]
        urllist=[]
        contentlist=[]
        for paper in papers:
            titlelist= paper.xpath(".//*[@class=\"postTitle\"]/a/text()").extract()
            urllist=paper.xpath(".//*[@class=\"postTitle\"]/a/@href").extract()
            contentlist=paper.xpath(".//*[@class=\"postCon\"]/div/text()").extract()

        for  i in range(len(titlelist)):
            paperitem=cnblogs.items.CnblogsItem()
            paperitem["title"] = titlelist[i]
            paperitem["url"] = urllist[i]
            paperitem["content"] = contentlist[i]

            yield paperitem










