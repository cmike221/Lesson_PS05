import scrapy


class LemanaproSpider(scrapy.Spider):
    name = "lemanapropars"
    allowed_domains = ["lemanapro.ru"]
    start_urls = ["https://lemanapro.ru/catalogue/lyustry/"]

    def parse(self, response):
        items = response.css('div.p155f0re_plp')
        for item in items:
            yield {
                'name' : item.css('div.lsooF span::text').get(),
                'price' : item.css('div.pY3d2 span::text').get(),
                'url' : item.css('a').attrib['href']
            }
