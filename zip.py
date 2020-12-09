import scrapy

class ZipCrawler(scrapy.Spider):
    name = 'zipcrawler'
    start_urls = ['https://www.zipdatamaps.com/list-of-zip-codes-in-illinois.php']

    def parse(self, response):
        # print("---------------------")
        # res = response.xpath('//table//tr//td[1]//a/text()')
        # print(res)
        # print("---------------------")
        for next_page in response.xpath('//table//tr//td[1]//a'):
            yield response.follow(next_page, self.zip)

            # /html/body/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]/table/tbody/tr/td[4]/a

    def zip(self, response):
        if response.status != 200:
            return


        print(response)
        # pass
        # for title in response.css('table tbody'):
        #     yield {
        #         'neighborhood': title.css('tr:nth-child(1) td:nth-child(2) ::text').get(),
        #         'zip': title.css('tr:nth-child(2) td a ::text').get(),
        #         'city': title.css('tr:nth-child(3) td:nth-child(2) a ::text').get(),
        #         'region': title.css('tr:nth-child(4) td:nth-child(2) a ::text').get(),
        #         'area codes': title.css('tr:nth-child(5) td:nth-child(2) a ::text').getall(),
        #     }
