import scrapy


class LightingparsSpider(scrapy.Spider):
    name = "lightingpars"
    allowed_domains = ["divan.ru"]
#    start_urls = ["https://www.divan.ru/category/svet"]
    start_urls = ["https://www.divan.ru/category/svet/page-5"]

    def parse(self, response):
        lightins = response.css('div._Ud0k')
        for light in lightins:
            yield {
                'name' : light.css('div.lsooF span::text').get(),
                'price' : light.css('div.pY3d2 span::text').get(),
                'url' : light.css('a').attrib['href']
            }
