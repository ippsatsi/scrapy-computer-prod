# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from main.models import Quote, Producto
from asgiref.sync import sync_to_async


class ScrapyAppPipeline(object):
    @sync_to_async
    def process_item(self, item, spider):
        quote = Quote(text=item.get('text'), author=item.get('author'))
        quote.save()
        return item
    

class ProductoPipeline(object):
    @sync_to_async
    def process_item(self, item, spider):
        producto = Producto(titulo=item.get('titulo').lower().capitalize(), 
                        precio_soles= price_format(price_clean(item.get('precio_soles'))),
                        precio_dolares= price_format(price_clean(item.get('precio_dolares'))),
                        categoria=item.get('categoria').lower(),
                        marca= item.get('marca').lower() if item.get('marca') else  '',
                        proveedor=item.get('proveedor'),
                        )       
        producto.save()
        return item
    
def price_clean(price):
    price = price.replace('S/.','')\
            .replace('\xa0','')\
            .replace('(','')\
            .replace(')','')\
            .replace(',','.')\
            .replace('PEN', '')\
            .replace('$','')\
            .replace('S/', '')\
            .strip()
    return price
        
def price_format(price):
    return None if price == '' else float(price)