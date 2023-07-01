# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyAppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProductoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    precio_soles = scrapy.Field()
    precio_dolares = scrapy.Field()
    categoria = scrapy.Field()
    marca = scrapy.Field()
    proveedor = scrapy.Field()