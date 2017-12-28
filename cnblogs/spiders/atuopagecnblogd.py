#!usr/bin/python/
# -*-conding:utf-8-*-
# -*- coding: utf-8 -*-
import scrapy
from cnblogs import items


class CnblogsspiderSpider(scrapy.Spider):
	name = 'cnblogsspiderv2'
	allowed_domains = ['cnblogs.com']
	start_urls = ['http://www.cnblogs.com/yincheng01/default.html?page=1']

	def parse(self, response):
		papers = response.xpath(".//*[@class=\"day\"]")
		titlelist = []
		urllist = []
		contentlist = []
		for paper in papers:
			titlelist = paper.xpath(".//*[@class=\"postTitle\"]/a/text()").extract()
			urllist = paper.xpath(".//*[@class=\"postTitle\"]/a/@href").extract()
			contentlist = paper.xpath(".//*[@class=\"postCon\"]/div/text()").extract()

		for i in range(len(titlelist)):
			paperitem = items.CnblogsItem()
			paperitem["title"] = titlelist[i]
			paperitem["url"] = urllist[i]
			paperitem["content"] = contentlist[i]

			yield paperitem
		last = []
		next_page = response.xpath(".//div[@id=\"nav_next_page\"]/a/href").extract()

		if len(next_page) != 0:
			last.append(next_page[0])
		next_page = response.xpath(".//div[@clas\"pager\" //a").extract()
		for line in next_page:
			if line.text == "下一页":
				last.append(line.xpath("@href")[0])

		print(last)

		if len(last) != 0:
			yield scrapy.Request(url=last[0], callback=self.parse)
