# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

from betterhome.items import BetterhomeItem
from .util import process_ingredients


class BtrecipeSpider(scrapy.Spider):
    name = 'btrecipe'
    allowed_domains = ['www.bh-recipe.jp']
    start_urls = ['https://www.bh-recipe.jp/recipe']

    rules = [Rule(LinkExtractor('*.html'), callback='parse', follow=True)]

    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        url = response.url
        print('url')
        print(url)
        recipe = '\n'.join(response.css('span.instruction::text').getall())
        time = [s for s in response.xpath('//td/text()').getall() if re.match(r'[0-9]{2,}分*', s)][0]
        calory = response.css('span.calories::text').get() + 'kcal'
        name = response.css('span.name::text').getall()
        amount = response.css('span.amount::text').getall()
        servings = response.css('span.yield::text').get()
        ingredients = process_ingredients(name, amount, servings)

        yield {
            "title": title,
            "url": url,
            "recipe": recipe,
            "time": time,
            "calory": calory,
            "ingredients": ingredients
        }
