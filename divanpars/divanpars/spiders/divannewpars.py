import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/category/divany-i-kresla/page-3"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name' : divan.css('div.lsooF span::text').get(),
                'price' : divan.css('div.pY3d2 span::text').get(),
                'url' : divan.css('a').attrib['href']
            }
