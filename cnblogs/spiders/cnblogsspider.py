# -*- coding: utf-8 -*-
import scrapy
from cnblogs import items
from scrapy import Selector

class CnblogsspiderSpider(scrapy.Spider):
    name = 'cnblogsspider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/yincheng01/default.html?page=1']
    offset = 0

    def parse(self, response):
        papers = response.xpath(".//*[@class=\"day\"]")
        titlelist = []
        urllist = []
        contentlist = []
        for paper in papers:
            titlelist = paper.xpath(".//*[@class=\"postTitle\"]/a/text()").extract()
            urllist =  paper.xpath(".//*[@class=\"postTitle\"]/a/@href").extract()
            contentlist = paper.xpath(".//*[@class=\"postCon\"]/div/text()").extract()

        for i in range(len(titlelist)):
            paperitem = items.CnblogsItem()
            paperitem["title"] = titlelist[i]
            paperitem["url"] = urllist[i]
            paperitem["content"] = contentlist[i]


            yield paperitem

            #实现自动翻页
        # next_page = paper.xpath('.//div[@id]')
        # if next_page != None:
        #         yield scrapy.Request(url = next_page[0],callback= self.parse)
        #实现自动翻页
        if self.offset < 27:
            self.offset +=1
            yield scrapy.Request(url="http://www.cnblogs.com/yincheng01/default.html?page=" + str(self.offset),
                                 callback=self.parse)