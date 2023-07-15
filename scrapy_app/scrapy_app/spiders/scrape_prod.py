import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.html import remove_tags
from ..items import ProductoItem
from scrapy_playwright.page import PageMethod
import json


class CYCSpider(CrawlSpider):
    name = "cyccomputer_run"
    item_count = 0
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_app.pipelines.ProductoPipeline': 300
        }
    }
    allowed_domain = ["cyccomputer.pe"]
    start_urls = ['https://cyccomputer.pe/739-perifericos-gamer',
                  'https://cyccomputer.pe/781-tarjetas-graficas',
                  ]
    proveedor = 'cyccomputer'

    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//h2[@class="productName"]/a') ),callback= 'parse_item',),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a[@class="next js-search-link"]'))) ,
        
    }


    def parse_item(self, response):
        sc1_item = ProductoItem()

        #items de productos
        sc1_item['titulo'] = response.xpath("normalize-space(//h1[@class='h1']/text())").get()
        sc1_item['precio_soles'] = response.xpath("normalize-space(/html/body/main/section/div/div/div[2]/section/div[1]/div/div[2]/div[2]/div[1]/div[1]/span[2]/text())")\
            .get().replace('.','') # eliminamos el punto, como separador de miles


        sc1_item['precio_dolares'] = response.xpath("normalize-space(/html/body/main/section/div/div/div[2]/section/div[1]/div/div[2]/div[2]/div[1]/div[1]/span[1]/text())")\
            .get().replace('.','') # eliminamos el punto, como separador de miles

        sc1_item['categoria'] = response.xpath("//li[@itemprop='itemListElement']/a/span/text()").extract()[-2]
        sc1_item['marca'] = self.extract_data_table(response, '//tbody', 'MARCA', 2)
        sc1_item['proveedor'] = self.proveedor

        #//nav/ol/li[last()-1]/a
        #//nav[@class='breadcrumb hidden-sm-down']//li[last()-1]/a
        #response.xpath('//li[@itemprop="itemListElement"]/a/span/text()').getall()[-2]
        
        self.item_count += 1
        #print("item_count" + str(self.item_count))
        #if self.item_count > 5:
        #    raise CloseSpider('item_exceeded')
        yield sc1_item


    def extract_data_table(self, response, xpath_table, data_title, pos):
        """xpath_table: es la ruta al table, de la que vamos a extraer la fila(tr) y
            los campos(td)
            data_title: es el nombre del dato a buscar
            pos: es la posicion del dato dentro del tr, comenzado en 0 la primera posicion"""
        
        lista_tr = response.xpath(xpath_table + '/tr')

        for tr in lista_tr:
            td_var = tr.xpath('.//td/text()').getall()
            if len(td_var) > pos and data_title in td_var[0].upper():
                return td_var[pos]
            

class Yamoshi_Spider(CrawlSpider):
    name = "yamoshi_run"
    item_count = 0
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_app.pipelines.ProductoPipeline': 300
        }
    }
    allowed_domain = ["yamoshi.com.pe"]
    start_urls = ['https://yamoshi.com.pe/98-mouses-gaming',
                  'https://yamoshi.com.pe/97-audifonos-gaming',
                  'https://yamoshi.com.pe/99-teclados-gaming',
                  'https://yamoshi.com.pe/101-microfonos-gaming',
                  'https://yamoshi.com.pe/118-pad-mouse-gaming',
                  'https://yamoshi.com.pe/120-kit-perifericos-gaming',
                  'https://yamoshi.com.pe/104-sillas-gamer',
                  'https://yamoshi.com.pe/192-camaras-web',
                  'https://yamoshi.com.pe/193-accesorios-para-streaming',
                  'https://yamoshi.com.pe/66-tarjeta-de-video',
                  ]
    proveedor = 'Yamoshi'

    rules = {
        Rule(LinkExtractor(allow = ("yamoshi.com.pe"), restrict_xpaths = ('//h5[@class="product-title-item"]/a') ),callback= 'parse_item', cb_kwargs={'proveedor1': 'Yamoshi'}),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li/a[@class="next js-search-link"]'))) ,
        
    }

    def parse_item(self, response, proveedor1):
        sc1_item = ProductoItem()

        #items de productos
        sc1_item['titulo'] = response.xpath("normalize-space(//div[@class='h1 product-name-detail']/h1/text())").get()
        sc1_item['precio_soles'] = response.xpath("normalize-space(//span[@class='text-price-contrary-money']/text())").get().replace(',','') # eliminamos las comas, como separador de miles

        sc1_item['precio_dolares'] = ""
        sc1_item['categoria'] = response.xpath("normalize-space(//div[@class='product-more-opt']//li/a/span/text())").get()
        sc1_item['marca'] = self.extract_data_table(response, '//div[@class="product-information"]//table/tbody', 'MARCA', 1)
        sc1_item['proveedor'] = proveedor1
  

        self.item_count += 1
        #print("item_count" + str(self.item_count))
        #if self.item_count > 5:
        #    raise CloseSpider('item_exceeded')
        yield sc1_item

    def extract_data_table(self, response, xpath_table, data_title, pos):
        """xpath_table: es la ruta al table, de la que vamos a extraer la fila(tr) y
            los campos(td)
            data_title: es el nombre del dato a buscar
            pos: es la posicion del dato dentro del tr, comenzado en 0 la primera posicion"""
        
        lista_tr = response.xpath(xpath_table + '/tr')

        for tr in lista_tr:
            td_var = tr.xpath('.//td')
            if len(td_var) > pos and data_title in td_var[0].xpath(".//span/text()").get().upper():
                return td_var[pos].xpath(".//span/span/text()").get()
            

class InfotecSpider(CrawlSpider):
    name = "infotec_run"
    item_count = 0
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_app.pipelines.ProductoPipeline': 300
        }
    }
    allowed_domain = ["infotec.com.pe"]
    start_urls = ['https://www.infotec.com.pe/103-teclados-gamer',
                  'https://www.infotec.com.pe/102-pad-mouse-gamer',
                  'https://www.infotec.com.pe/100-mouse-gamer',
                  'https://www.infotec.com.pe/101-audifonos-gamer',
                  'https://www.infotec.com.pe/920-accesorios-gamer',
                  'https://www.infotec.com.pe/34-tarjetas-de-video',
                  ]
    proveedor = 'infotec'

    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//h2[@class="h3 product-title"]/a') ),callback= 'parse_item',),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//nav[@class="pagination"]//li[last()]/a'))) ,
        
    }

    def start_requests(self):
        return super().start_requests()

    def parse_item(self, response):
        sc1_item = ProductoItem()

        #items de productos
        sc1_item['titulo'] = response.xpath("//h1/span/text()").get()
        sc1_item['precio_soles'] = response.xpath("normalize-space(//span[@class='current-price']/span/text())")\
            .get()

        sc1_item['precio_dolares'] = ''

        #sacamos categoria de 2 fuentes:
        # 1) del breadcrumb Inicio > Zona Gamer > ....> ...
        # 2) de la tabla de caracteristicas, del item producto
        breadcrumb = response.xpath('//ol/li//span/text()').getall()
        categoria_xpath = remove_tags(response.xpath("normalize-space(//ul/li[3][contains(translate(text(), 'producto', 'PRODUCTO'), 'PRODUCTO')])").extract()[-1])\
                            .replace('\xa0','')\
                            .split(':')[1]
        sc1_item['categoria'] = categoria_xpath #if 'ZONA' in breadcrumb[-2].upper() else breadcrumb[2]
        
        #buscamos todos los li con el texto 'marca' (con translate, lo haces case-insensitive), usamos el primero
        #removemos los tags html, separamos el str por ':'
        sc1_item['marca'] = remove_tags(response.xpath("//ul/li[1][contains(translate(text(), 'marca', 'MARCA'), 'MARCA')]").get())\
                                .replace('\xa0','')\
                                .split(':')[1]
        
        sc1_item['proveedor'] = self.proveedor

        sc1_item['titulo'] = sc1_item['titulo'].strip()
        sc1_item['categoria'] = sc1_item['categoria'].strip()
        sc1_item['marca'] = sc1_item['marca'].strip()
        
        self.item_count += 1
        yield sc1_item


class MemoryKingSpider(CrawlSpider):
    name = "memoryking_run"
    item_count = 0
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_app.pipelines.ProductoPipeline': 300
        }
    }
    allowed_domain = ["www.memorykings.pe"]
    start_urls = ['https://www.memorykings.pe/listados/703/gaming-keyboard',
                  'https://www.memorykings.pe/listados/706/gaming-accesories',
                  'https://www.memorykings.pe/listados/800/gaming-chair',
                  'https://www.memorykings.pe/listados/719/gaming-cpu-cooler',
                  'https://www.memorykings.pe/listados/702/gaming-headset',
                 # 'https://www.memorykings.pe/listados/709/gaming-display-monitors',
                  'https://www.memorykings.pe/listados/701/gaming-mice',
                  'https://www.memorykings.pe/subcategorias/64/tarjetas-graficas-amd-radeon-rx-radeon-pro',
                  'https://www.memorykings.pe/subcategorias/16/tarjetas-graficas-nvidia-geforce-nvidia-quadro',
                  'https://www.memorykings.pe/listados/705/gaming-mouse-pad']
    proveedor = 'memorykings'

    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('/html/body/form/section[2]/div[3]/div/ul/li//a') ),callback= 'parse_item',),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//ul/li/div/a'))),
        # //ul/li/div/a
    }

    def parse_item(self, response):
        sc1_item = ProductoItem()

        #items de productos
        sc1_item['titulo'] = response.xpath("//div//h1[@class='h1']/text()").get()
        precios = response.xpath('//div[contains(@class, "border-card")]//div[contains(@class, "price")]/text()').get() #$ 45.00 ó S/ 167.50
        precios = precios.replace('$','').replace('S/','') # 45.00 ó  167.50
        precios = precios.strip().split('ó')
        sc1_item['precio_soles'] = precios[1].replace(',','') # eliminamos las comas, como separador de miles

        sc1_item['precio_dolares'] = precios[0].replace(',','') # eliminamos las comas, como separador de miles

        sc1_item['categoria'] = response.xpath('//section[2]/div[contains(@class, "breadcrumb")]//li[last()]/a/text()').get()
        
        sc1_item['marca'] = ''
        
        sc1_item['proveedor'] = self.proveedor
      
        self.item_count += 1
        yield sc1_item


class MMStoreSpider(CrawlSpider):
    name = "mmstore_run"
    item_count = 0
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_app.pipelines.ProductoPipeline': 300
        }
    }
    allowed_domain = ["mmstoreperu.com"]
    start_urls = ['https://mmstoreperu.com/es-pe/collections/teclados-gaming',
                  'https://mmstoreperu.com/es-pe/collections/mouse-gamer',
                  'https://mmstoreperu.com/es-pe/collections/audifonos',
                  'https://mmstoreperu.com/es-pe/collections/soportes-audifono',
                  'https://mmstoreperu.com/es-pe/collections/microfonos',
                  'https://mmstoreperu.com/es-pe/collections/combos-y-kits',
                  'https://mmstoreperu.com/es-pe/collections/combos-gaming',
                  'https://mmstoreperu.com/es-pe/collections/kits',
                  'https://mmstoreperu.com/es-pe/collections/mousepad',
                  ]
    proveedor = 'mmstore'

    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//div[contains(@class,"product-item__info")]/a[2]') ),callback= 'parse_item',),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//div[contains(@class,"pagination")]/a[@class="pagination__next link"]'))) ,
        
    }

    def parse_item(self, response):
        sc1_item = ProductoItem()

        #items de productos
        sc1_item['titulo'] = response.xpath("//h1/text()").get()
        sc1_item['precio_soles'] = ''
        sc1_item['precio_dolares'] = response.xpath('//div[contains(@class,"product-form")]//span[contains(@class, "mw-price")]/text()')\
                                            .get()\
                                            .strip()
        
        #string(//div[contains(@class,"product-form")]//span[contains(@class, "mw-price")]/@data-mw-orig-price)
        lista_scripts = response.xpath('//script/text()').getall()
        json_prod_data = json.loads(lista_scripts[12])

        sc1_item['categoria'] = json_prod_data['category']
        
        sc1_item['marca'] = response.xpath('//a[contains(@class, "product-meta__vendor")]/text()').get()
        
        sc1_item['proveedor'] = self.proveedor
      
        self.item_count += 1
        yield sc1_item


class MMStoreSearchSpider2(scrapy.Spider):
    name = "mmstore_js"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_app.pipelines.ProductoPipeline': 300
        },
        # 'DOWNLOAD_DELAY': 4,
        # 'CONCURRENT_REQUESTS' : 1,
        'PLAYWRIGHT_LAUNCH_OPTIONS': {
            "headless": False,
            "timeout": 6 * 1000,  # 6 seconds
        },
    }
    allowed_domains = ["mmstoreperu.com"]
    start_urls = [ 'https://mmstoreperu.com/es-pe/collections/teclados-gaming',     #142
                  'https://mmstoreperu.com/es-pe/collections/mouse-gamer',          # 98
                  'https://mmstoreperu.com/es-pe/collections/audifonos',            # 99
                  'https://mmstoreperu.com/es-pe/collections/soportes-audifono',    #  9
                  'https://mmstoreperu.com/es-pe/collections/microfonos',           # 27
                  'https://mmstoreperu.com/es-pe/collections/combos-y-kits',         # 33
                  'https://mmstoreperu.com/es-pe/collections/combos-gaming',         # 12
                  'https://mmstoreperu.com/es-pe/collections/kits',                   #  8 
                  'https://mmstoreperu.com/es-pe/collections/mousepad',              # 98
                  ]                                                                  # total 526
    proveedor = "mmstore"

    def start_requests(self):
        print(self.start_urls)
        for link in self.start_urls:
            print("------------{}-------------".format(link))
            yield scrapy.Request(link, callback=self.parse,meta=dict(
            playwright = True,
            playwright_include_page = True,
            playwright_page_methods = [
                PageMethod('wait_for_selector', '[data-mw-orig-price]')
            ],
            errback = self.errback
        ))
       

    def parse(self, response):
        for product in response.xpath("//div[contains(@class, 'product-item__info-inner')]"):

            sc1_item = ProductoItem()

            #items de productos
            sc1_item['titulo'] = product.xpath("normalize-space(./a[contains(@class,'product-item__title')]/text())").get()
            sc1_item['precio_soles'] = product.xpath("normalize-space(.//div[contains(@class, 'product-item__price-list')]/span[1]/span[2]/text())").get()
            sc1_item['precio_dolares'] = product.xpath("normalize-space(.//div[contains(@class, 'product-item__price-list')]/span[1]/span[2]/@data-mw-orig-price)")\
                                                .get()\
                                                .strip()
            
            sc1_item['categoria'] = ''
            sc1_item['marca'] = product.xpath("normalize-space(./a[contains(@class,'product-item__vendor')]/text())").get()
            sc1_item['proveedor'] = self.proveedor
            yield sc1_item

        next_page = response.xpath('//div[contains(@class,"pagination")]/a[@class="pagination__next link"]/@href').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, meta=dict(
            playwright = True,
            playwright_include_page = True,
            playwright_page_methods = [
                PageMethod('wait_for_selector', '[data-mw-orig-price]')
            ],
            errback = self.errback
        ))

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()


class ITStoreSearchSpider(scrapy.Spider):

    name = "itstore_searh_run"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_app.pipelines.ProductoPipeline': 300
        }
    }
    allowed_domain = ["itstore.pe"]
    start_urls = ['https://itstore.pe/product-category/teclados-mouse/',
                  'https://itstore.pe/product-category/microfono-audifono/',
                  'https://itstore.pe/product-category/gaming/',
                  'https://itstore.pe/product-category/accesorios/',
                #   '',
                #   '',
                #   '',
                #   '',
                #   '',
                  ]
    proveedor = 'itstore'


    def start_requests(self):
        for link in self.start_urls:
            yield scrapy.Request(link, callback=self.parse)


    def parse(self, response):
        for product in response.xpath("//div[@class='mf-product-details']"):

            sc1_item = ProductoItem()

            #items de productos
            sc1_item['titulo'] = product.xpath("normalize-space(.//div[@class='mf-product-content']//a/text())").get()
            sc1_item['precio_soles'] = product.xpath("normalize-space(./div[2]/span/span//span/bdi/text())").get()
            sc1_item['precio_dolares'] = product.xpath("normalize-space(./div[2]/span/p/span//bdi)").get()\
                                                .strip()
            
            sc1_item['categoria'] = ''
            sc1_item['marca'] = ''
            sc1_item['proveedor'] = self.proveedor
            yield sc1_item

        next_page = response.xpath('//a[@class="next page-numbers"]/@href').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


class ITStoreSpider(CrawlSpider):
    name = "itstore_run"
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy_app.pipelines.ProductoPipeline': 300
        }
    }
    allowed_domain = ["mmstoreperu.com"]
    start_urls = ['https://itstore.pe/product-category/teclados-mouse/',
                  'https://itstore.pe/product-category/microfono-audifono/',
                  'https://itstore.pe/product-category/gaming/',
                  'https://itstore.pe/product-category/accesorios/',
                  'https://itstore.pe/product-category/tarjetas-de-video/',
                #   '',
                #   '',
                #   '',
                #   '',
                  ]
    proveedor = 'itstore'

    rules = {
        Rule(LinkExtractor(allow = (), restrict_xpaths = ("//div[@class='mf-product-content']//h2[@class='woo-loop-product__title']/a") ),callback= 'parse_item',),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//a[@class="next page-numbers"]'))) ,
        
    }

    def parse_item(self, response):
        sc1_item = ProductoItem()

        #items de productos
        sc1_item['titulo'] = response.xpath("//h1/text()").get()
        sc1_item['precio_soles'] = response.xpath("normalize-space(//div[contains(@class, 'entry-summary')]/p/span//span/bdi/text())").get()
        sc1_item['precio_dolares'] = response.xpath("normalize-space(//div[contains(@class, 'entry-summary')]/p[2]/span//bdi)").get()

        sc1_item['categoria'] = response.xpath("normalize-space(//span[@class='posted_in']/a[1]/text())").get()
        
        sc1_item['marca'] = response.xpath("normalize-space(//li[@class='meta-brand']/a/text())").get()
        
        sc1_item['proveedor'] = self.proveedor
      
        yield sc1_item