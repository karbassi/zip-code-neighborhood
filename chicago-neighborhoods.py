import scrapy

class NeighborhoodCrawler(scrapy.Spider):
    name = 'neighborhoodcrawler'
    start_urls = ['https://www.zipdatamaps.com/neighborhoods/illinois/city/map-of-chicago-neighborhoods']

    def parse(self, response):
        for next_page in response.css('table tr td:nth-child(2) a'):
            yield response.follow(next_page, self.zip)

    def zip(self, response):
        for title in response.css('table tbody'):
            yield {
                'neighborhood': title.css('tr:nth-child(1) td:nth-child(2) ::text').get(),
                'zip': title.css('tr:nth-child(2) td a ::text').get(),
                'city': title.css('tr:nth-child(3) td:nth-child(2) a ::text').get(),
                'region': title.css('tr:nth-child(4) td:nth-child(2) a ::text').get(),
                'area codes': title.css('tr:nth-child(5) td:nth-child(2) a ::text').getall(),
            }
