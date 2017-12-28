import urllib
import urllib.request
from bs4 import BeautifulSoup
import lxml
import lxml.etree

data=urllib.request.urlopen("http://www.cnblogs.com/yincheng01/default.html?page=3").read()
last = []
mytree = lxml.etree.HTML(data)
# papers = mytree.xpath(".//*[@class=\"day\"]")
# for paper in papers:
# 	title = paper.xpath(".//*[@class=\"postTitle\"]/a/text()")
# 	url = paper.xpath(".//*[@class=\"postTitle\"]/a/@href")
# 	content = paper.xpath(".//*[@class=\"postCon\"]/div/text()")
# 	print(title, url)
next_page = mytree.xpath(".//div[@class=\"pager\"]//a")

if len(next_page) != 0:
	last.append(next_page[0])
for line in next_page:
	if line.text == "下一页":
		#print(line.text,line.xpath("@href"))
		last.append(line.xpath("@href")[0])

print(last)


'''
datalist=soup.find_all("div","list_item article_item")
#print(datalist)
for line  in  datalist:
    print(line.find("span","link_title").a.get_text())
    print(line.find("span", "link_title").a.get("href"))
    print(line.find("div", "article_description").get_text())

'''
