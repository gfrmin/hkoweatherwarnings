# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class warningItem(scrapy.Item):
    warningdate = scrapy.Field()
    warning = scrapy.Field()
    issuetime = scrapy.Field()
    issuedate = scrapy.Field()
    canceltime = scrapy.Field()
    canceldate = scrapy.Field()
