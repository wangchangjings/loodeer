# -*- coding: utf-8 -*-
import scrapy
from Xiaohongshu.items import XiaohongshuItem

class XiaohongshuSpider(scrapy.Spider):
    name = 'xiaohongshu'
    allowed_domains = ['m.xiaohongshu.com']
    start_urls = ['http://m.xiaohongshu.com/']

    def parse(self, response):
        print('xxxxxxxxxxxxxxx=====================>')
        #from scrapy.shell import inspect_response
        #inspect_response(response, self)

        selector = scrapy.Selector(response)

        # https://stackoverflow.com/questions/1604471/how-can-i-find-an-element-by-css-class-with-xpath
        meta_divs = selector.xpath('//div[contains(concat(@class," "), "dual-column-layout ")]//div[contains(@class, "note-item")]')
        for index,single_div in enumerate(meta_divs):
            xitem = XiaohongshuItem()
            xitem['article_url'] = 'http://m.xiaohongshu.com/' + single_div.xpath('a/@href').extract()[0]
            desc_list = single_div.xpath('.//p[contains(@class, "note-desc")]/text()').extract()
            if desc_list:
                xitem['desc'] = desc_list[0]
            else:
                xitem['desc'] = ''

            title = single_div.xpath('.//h3[contains(@class, "note-title")]/text()').extract()
            if title:
                xitem['title'] = title[0]
            else:
                xitem['title'] = ''
            xitem['author'] = single_div.xpath('.//div[contains(@class, "note-author")]//a[contains(@class, "note-author-nickname")]/text()').extract()[0]
            xitem['avatar'] = single_div.xpath('.//div[contains(@class, "note-author")]//img[contains(@class, "avatar-img")]/@src').extract()[0]
            xitem['likes'] = single_div.xpath('.//span[contains(@class, "note-likes")]//text()').extract()[0].replace('\n', '').replace(' ', '')
            yield xitem

        print('yyyyyyyyyyyy---------------------->')


        # 去掉注释即可爬取完整个feed流数据.
        # next_url = 'http://m.xiaohongshu.com/' + selector.xpath('//a[contains(@class, "next link")]/@href').extract()[0]
        # if next_url:
        #     yield scrapy.Request(next_url, callback=self.parse)
        #

