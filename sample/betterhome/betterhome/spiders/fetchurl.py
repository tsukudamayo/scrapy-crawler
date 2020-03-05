import re
import sys
import scrapy


class FetchurlSpider(scrapy.Spider):
    count = 0
    name = "fetchurl"
    start_urls = ['https://www.bh-recipe.jp/recipe/list.php']
    def parse(self, response):
        url = 'https://www.bh-recipe.jp/recipe'
        all_html_a = [s for s in response.xpath('//a').getall()
                      if re.findall(r'html', s)]
        not_img_a = [s for s in all_html_a if not re.findall(r'img', s)]
        all_url = [s.split('"')[1].replace('./','/') for s in not_img_a]
        fullpath = [url + s for s in all_url]
        yield {'urls': fullpath}

        next_page = [s.split('"')[1] for s
                     in response.xpath('//tr/td/a').getall()
                     if re.findall(r'次', s)]
        if next_page:
            next_page = next_page[0]
        else:
            sys.exit(1)

        print('next_page')
        print(next_page)
        if next_page is not None:
            self.count += 1
            print('next_page is not None')
            next_url = 'https://www.bh-recipe.jp/recipe/list.php?&sc=k&s_type=and&__utma=227822030.237155212.1582943972.1582980620.1583032357.4&__utmb=227822030.3.10.1583032357&__utmc=227822030&__utmz=227822030.1582977772.2.2.utmcsr%3Dgoogle%7Cutmccn%3D%28organic%29%7Cutmcmd%3Dorganic%7Cutmctr%3D%28not+provided%29&__utmt=1&pg=' + str(self.count)
            print('next_url')
            print(next_url)
            yield scrapy.Request(next_url, callback=self.parse)
