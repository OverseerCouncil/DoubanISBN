import scrapy
import sys
from douban_isbn.items import DoubanIsbnItem
from googlesearch import search

class DoubanisbnSpider(scrapy.Spider):
    name = 'doubanISBN'
    allowed_domains = ['book.douban.com']
    start_urls = []

    def start_requests(self):
        book_list = []
        with open('book.txt',mode = 'r',encoding = "UTF-8") as f:
            for line in f:
                book_list.append(line.strip('\n'))
        print(book_list)
        for book_name in book_list:
            search_content = "%s site:book.douban.com/subject" % (book_name)
            urls = search(search_content)
            url = urls[0]
            print(url)
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        item = DoubanIsbnItem()
        item['name'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first()
        ##print(item['name'])
        item['publisher'] = response.xpath('//*[@id="info"]/span[2]/following::text()[1]').extract_first()
        ##print(item['publisher'])
        item['isbn'] = response.xpath('//*[@id="info"]/span[11]/following::text()[1]').extract_first()
        ##print(item['isbn'])
        yield item