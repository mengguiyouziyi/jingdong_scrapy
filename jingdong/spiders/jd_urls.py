# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from jingdong.items import JdBookUrlItem
import codecs


class GetDetailSpider(CrawlSpider):
    name = 'jd_urls'
    allowed_domains = ['jd.com']
    def __init__(self):
        self.st = 'http:'

    def start_requests(self):
        # 所有图书类别网站
        url = 'https://book.jd.com/booksort.html'
        yield scrapy.FormRequest(url, callback=self.parse_list)

    def parse_list(self, response):
        book_item = JdBookUrlItem()
        category_urls = response.xpath('//div[@class="mc"]//dd//em//a//@href').extract()
        for url in category_urls:
            category_url = self.st + url
            book_item['category_url'] = category_url
            # 将每个图书类别url发送请求
            yield scrapy.Request(url=category_url, meta={'item': book_item}, callback=self.parse_category)
            print('category_url~~' + category_url)

    def parse_category(self, response):
        book_item = response.meta['item']
        book_urls = response.xpath('//div[@class="gl-i-wrap j-sku-item"]/div[@class="p-img"]/a/@href').extract()
        with codecs.open('book_url.txt', 'a', 'utf-8') as file:
            for url in book_urls:
                # 图书url存储
                book_url = self.st + url
                file.writelines(book_url + '\n')
                print('book_url~~' + book_url)
                book_item['book_url'] = book_url

        pn_next = response.xpath('//a[@class="pn-next"]//@href').extract()
        if len(pn_next) != 0:
            pn_next_url = 'https://list.jd.com' + pn_next[0]
            book_item['pn_next_url'] = pn_next_url
            # 依然是图书类别url，下一页
            yield scrapy.Request(pn_next_url, callback=self.parse_category)
            print('pn_next_url~~' + pn_next_url)










