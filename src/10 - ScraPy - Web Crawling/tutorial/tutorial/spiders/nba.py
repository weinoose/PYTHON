import scrapy

class QuotesSpider(scrapy.Spider):
    name = "nba"
    start_urls = ["https://www.espn.com/nba/stats"]
    def parse(self, response):
        for content in response.xpath('//*[@id="fittPageContainer"]/div[3]/div/div/section[1]/div/div[4]/div[1]/div/div[2]/div/div/div[2]/table/tbody/tr'):
            yield {
                "name" : content.xpath('td[1]/div/a/text()').get(),
                "team" : content.xpath('td[1]/div/span[2]/text()').get(),
                "ppg" : content.xpath('td[2]/text()').get()
            }
        
        next_page = response.xpath('').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)

# scrapy crawl nba -o nba.json
# scrapy startproject tutorial