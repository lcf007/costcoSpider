import scrapy
import csv
from costcoSpider.items import CostcospiderItem
from costcoSpider.db import Sql

class CostcoSpider(scrapy.Spider):
    name = "costco"

    def start_requests(self):
        urls = [
            'https://www.costco.ca/laptops.html?currentPage=1&pageSize=24',
        ]
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        myData = []
        for desc in response.css("p.description"):
            myData.append(desc.css("a::attr(href)").extract_first())

        item = CostcospiderItem()
        #myFile = open('level_1.csv', 'a+')
        #with myFile:
        #    for l in myData:
        #        myFile.write(l+'\n');
        for l in myData:
            item['url'] = l
            item['price'] = 100
            print(item)
            #Sql.insert_product(item);


