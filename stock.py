import scrapy
import re
import datetime
import csv

# export result into a json file: scrapy runspider quotes_spider.py -o quotes.json 


reader = csv.reader(open("stocks.csv", "rb"))
for row in reader:
    print row

now = datetime.datetime.now()

class QuotesSpider(scrapy.Spider):

    name = "quotes"
    start_urls = ['https://www.bloomberg.com/quote/BABA:US','https://www.bloomberg.com/quote/RTN:US']

    def parse(self, response):
        yield{
        'company': response.url,
        'date': now.strftime("%Y-%m-%d"),
        'current price': response.css('span[class*="priceText"]::text').extract(),
        'low': response.css('section[class*="rangeoneday"] div[class="text"] span[class="textLeft"]::text').extract(),
        'high': response.css('section[class*="rangeoneday"] div[class="text"] span[class="textRight"]::text').extract(),
        }

   	

           