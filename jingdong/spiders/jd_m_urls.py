# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
import codecs


class GetDetailSpider(CrawlSpider):
    name = 'jd_m_detail'
    allowed_domains = ['jd.com']
    def start_requests(self):
        headers = {
            'Host': 'item.jd.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10001-5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
        }
        url = 'http://item.jd.com/11514245.html'
        yield scrapy.Request(url, headers=headers, callback=self.parse_item)

    def parse_item(self, response):
        self.logger.info(response.url)
        # self.logger.info(response.body_as_unicode())
        with codecs.open('11514245.html', 'wb', 'utf-8') as file:
            file.writelines(response.body_as_unicode())
