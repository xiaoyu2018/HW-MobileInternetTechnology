import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ucas.items import UcasItem


class CrawlSpider(CrawlSpider):
    name = 'crawl'
    allowed_domains = ['ucas.edu.cn']
    start_urls = ['http://www.ucas.edu.cn/site/26?pn=1']

    # 翻页链接提取规则
    rules = (
        # 使用Rule类生成链接提取规则对象
        Rule(LinkExtractor(allow=r'site/26\?pn=\d+'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = UcasItem()
        sc = response.xpath('//html/body/div[4]/div[2]/div[2]/div[3]/p')
        
        for p in sc:
            item['title']= p.xpath('./a/@title').extract_first()
            item['link'] = p.xpath('./a/@href').extract_first()
            item['date'] = p.xpath('./span/text()').extract_first()
            yield item
        # print(response.url)
        
