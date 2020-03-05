# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import os
import re
import json
import itertools

from betterhome.items import BetterhomeItem
from .util import process_ingredients


class BtrecipeSpider(scrapy.Spider):
    name = 'btrecipe'
    allowed_domains = ['www.bh-recipe.jp']
    # start_urls = ['https://www.bh-recipe.jp/recipe/']

    with open('./url.json', 'r', encoding='utf-8') as r:
        data = json.load(r)
    start_urls = list(itertools.chain.from_iterable([d['urls'] for d in data]))

    if not os.path.isdir('./dest'):
        os.makedirs('./dest')

    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        url = response.url
        print('url')
        print(url)
        recipe = '\n'.join(response.css('span.instruction::text').getall())
        print('recipe')
        print(recipe)        
        time = [s for s in response.xpath('//td/text()').getall() if re.match(r'[0-9]{2,}分*', s)][0]
        print('time')
        print(time)
        calory = response.css('span.calories::text').get() + 'kcal'
        print('calory')
        print(calory)
        name = response.css('span.name::text').getall()
        amount = response.css('span.amount::text').getall()
        servings = response.css('span.yield::text').get()
        ingredients = process_ingredients(name, amount, servings)
        print('ingredients')
        print(ingredients)

        yield {
            "title": title,
            "url": url,
            "recipe": recipe,
            "time": time,
            "calory": calory,
            "ingredients": ingredients
        }

        # file output
        output = {
            "title": title,
            "url": url,
            "recipe": recipe,
            "time": time,
            "calory": calory,
            "ingredients": ingredients
        }
        print(output)
        # XXX duplicate XXX
        basename = os.path.basename(url)
        fname, _ = os.path.splitext(basename)
        filepath = os.path.join('./dest', fname + '_' + title + '.json')
        print('filepath')
        print(filepath)
        with open(filepath, 'w', encoding='utf-8') as w:
            json.dump(output, w, indent=4, ensure_ascii=False)
        # XXX duplicate XXX
