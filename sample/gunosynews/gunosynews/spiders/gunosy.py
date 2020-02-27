# -*- coding: utf-8 -*-
import scrapy

from gunosynews.items import GunosynewsItem


class GunosySpider(scrapy.Spider):
    name = 'gunosy'
    allowed_domains = ['gunosy.com']
    start_urls = (
        'http://gunosy.com/categories/1',
        'http://gunosy.com/categories/2',
        'http://gunosy.com/categories/3',
        'http://gunosy.com/categories/4',
        'http://gunosy.com/categories/5',
        'http://gunosy.com/categories/6',
        'http://gunosy.com/categories/7',
        'http://gunosy.com/categories/8',
    )

    def parse(self, response):
        for sel in response.css("div.list_content"):
            article = GunosynewsItem()
            article['title'] = sel.css("div.list_title > a::text").extract_first()
            article['url'] = sel.css("div.list_title > a::attr('href')").extract_first()
            article['subcategory'] = sel.css("div.list_text > a::text").extract_first()

            yield article


        next_page = response.css("div.page-link-option > a::attr('href')")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, callback=self.parse)

