# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
import codecs


class GetDetailSpider(CrawlSpider):
    name = 'jd_detail'
    allowed_domains = ['jd.com']
    def start_requests(self):
        headers = {
            'Host': 'item.jd.com',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10001-5',
            # 'Cookie': '__jda=122270672.118127146.1479889456.1491470499.1492050403.2; unpl=V2_ZzNtbRZeRh0gDUMGeR5bUmIGFw8SAksUJ1pPB3lJWQdkBBtbclRCFXMUR1FnGV4UZwIZXkVcRhBFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VHsQXAZhAxdacmdEJUU4RFR8GV4AVwIiXHIVF0lxAE9deRERBWcKEl5EV0YSRQl2Vw%3d%3d; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_e849d44c366f444cad90cc8b3a432687|1492050403297; __jdu=118127146; ipLoc-djd=1-72-2799-0; ipLocation=%u5317%u4EAC; areaId=1; __jdc=122270672; 3AB9D23F7A4B3C9B=2FKTJEKON5Z2VU5Q4MJ2GHO5XGBQMXEO4E4VSIRL65GS4LJU7I5DUXNQ4VRYH3VSU2A7VNAJSRAHKPOGWXCOJWP2DU',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            # 'If-Modified-Since': 'Thu, 13 Apr 2017 02:27:30 GMT',
            'Cache-Control': 'max-age=0',
        }
        url = 'http://item.jd.com/11514245.html'
        yield scrapy.FormRequest(url, headers=headers, callback=self.parse_item)

    def parse_item(self, response):
        self.logger.info(response.url)
        # self.logger.info(response.body_as_unicode())
        with codecs.open('11514245.html', 'wb', 'utf-8') as file:
            file.writelines(response.body_as_unicode())
