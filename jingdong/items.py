# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdBookUrlItem(scrapy.Item):
    # define the fields for your item here like:
    category_url = scrapy.Field()
    book_url = scrapy.Field()
    pn_next_url = scrapy.Field()
