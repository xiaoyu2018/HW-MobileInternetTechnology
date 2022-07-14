from re import U
import scrapy
from ucas.items import UcasItem

class BaseSpider(scrapy.Spider):
    name = 'base'
    allowed_domains = ['ucas.edu.cn']
    start_urls = ['http://www.ucas.edu.cn/site/26?pn=1']

    def parse(self, response):
        
        # 爬取目标信息
        item = UcasItem()
        sc = response.xpath('//html/body/div[4]/div[2]/div[2]/div[3]/p')

        for p in sc:
            item['title'] = p.xpath('./a/@title').extract_first()
            item['link'] = p.xpath('./a/@href').extract_first()
            item['date'] = p.xpath('./span/text()').extract_first()
            yield item
        
        # 翻页
        temp = response.xpath(
            '//html/body/div[4]/div[2]/div[2]/div[4]/span[last()]/a/@href').extract()
        # print(temp)
        if(len(temp) != 0):
            url = "http://www.ucas.edu.cn"+str(temp[0])
            yield scrapy.Request(url=url)
