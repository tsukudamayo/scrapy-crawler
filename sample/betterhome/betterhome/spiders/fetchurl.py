import re
import scrapy

class FetchurlSpider(scrapy.Spider):
    name = "fetchurl"
    start_urls = ['https://www.bh-recipe.jp/recipe/list.php']
    def parse(self, response):
        url = 'https://www.bh-recipe.jp/recipe'
        all_html_a = [s for s in response.xpath('//a').getall()
                      if re.findall(r'html', s)]
        not_img_a = [s for s in all_html_a if not re.findall(r'img', s)]
        all_url = [s.split('"')[1].replace('.','') for s in not_img_a]
        fullpath = [url + s for s in all_url]
        yield {'urls': fullpath}

        next_page = [s.split('"')[1] for s
                     in response.xpath('//tr/td/a').getall()
                     if re.findall(r'次', s)][0]
        print('next_page')
        print(next_page)
        if next_page is not None:
            print('next_page is not None')
            next_page = response.urljoin(next_page)
            print('next_page')
            print(next_page)
            yield scrapy.Request(next_page)

