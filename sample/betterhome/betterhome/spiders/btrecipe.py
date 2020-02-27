# -*- coding: utf-8 -*-
import scrapy


class BtrecipeSpider(scrapy.Spider):
    name = 'btrecipe'
    allowed_domains = ['www.bh-recipe.jp']
    start_urls = ['https://www.bh-recipe.jp/recipe/011701151.html']

    def parse(self, response):
        print(response)
        print('url')
        print(response.url)
        print('title')
        print(response.title)
        print(response.selector.xpath('//html/body/div/div/table/tbody/tr[2]/td[1]/div/table[1]/tbody/tr[1]/td[2]/span[1]/h1').get())
