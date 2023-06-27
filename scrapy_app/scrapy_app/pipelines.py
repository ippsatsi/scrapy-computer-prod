# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from main.models import Quote
from asgiref.sync import sync_to_async


class ScrapyAppPipeline(object):
    @sync_to_async
    def process_item(self, item, spider):
        quote = Quote(text=item.get('text'), author=item.get('author'))
        quote.save()
        return item