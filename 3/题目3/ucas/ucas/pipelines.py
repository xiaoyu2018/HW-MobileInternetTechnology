# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class UcasPipeline:
    def __init__(self):
        self.file=open("ucas.txt","w")
    
    def __del__(self):
        self.file.close()
    
    def process_item(self, item, spider):
        item = dict(item)

        json_data = json.dumps(item, ensure_ascii=False)
        self.file.write(json_data+',\n')
        
        return item
