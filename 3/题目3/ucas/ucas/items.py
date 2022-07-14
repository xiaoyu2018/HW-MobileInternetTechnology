# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UcasItem(scrapy.Item):
    # define the fields for your item here like:
    # 新闻标题
    title = scrapy.Field()
    # 新闻链接
    link = scrapy.Field()
    # 发布日期
    date = scrapy.Field()
    
