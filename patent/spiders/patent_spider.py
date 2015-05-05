# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from patent.items import PatentItem


class PatentSpiderSpider(CrawlSpider):
    name = 'patent-spider'
    allowed_domains = ['patents.justia.com']
    start_urls = ['http://patents.justia.com/inventor/alberto-dal-lago']

    rules = (
        Rule(LinkExtractor(allow=['/patent/\d+']), 'parse_patent'),
    )

    def parse_patent(self, response):
        patent = PatentItem()
        patent["application"] = response.xpath('//*[@id="history"]/div[@class="wrap"]/text()[2]').extract()[0].split(":")[1]
        patent["filed"] = response.xpath('//*[@id="history"]/div[@class="wrap"]/text()[6]').extract()[0].split(":")[1]
        patent["issued"] = response.xpath('//*[@id="history"]/div[@class="wrap"]/text()[8]').extract()[0].split(":")[1]
        return patent
