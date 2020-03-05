import os
import re
import sys
import json
import scrapy


_DST_DIR = './category'


class FetchCategory(scrapy.Spider):
    count = 0
    name = "fetchcategory"
    start_urls = ['https://www.bh-recipe.jp/recipe/list.php']

    def parse(self, response):
        end_point = 'https://www.bh-recipe.jp/recipe'
        dom = '//html/body/div/table[2]/tr[2]/td[1]/table[2]/'
        for i in range(2, 18):
            target_dom = dom + 'tr[' + str(i) + ']'
            if not response.xpath(target_dom):
                break

            fname = response.xpath(target_dom).get().split('<a href="')[1].split('">')[0].replace('./', '/')
            url = end_point + fname
            title = response.xpath(target_dom).get().split('</a>')[1].split('html">')[1]
            comment = response.xpath(target_dom + '/td/font/text()').get().replace('\r\n', '').replace('\t', '')
            servings = response.xpath(target_dom + '/td[3]').get().split('</td>')[0].split('<td>')[1]
            time = response.xpath(target_dom + '/td[4]').get().split('</td>')[0].split('<td>')[1]
            calory = response.xpath(target_dom + '/td[5]').get().split('</td>')[0].split('<td>')[1]
            genre = response.xpath(target_dom + '/td[6]').get().split('</td>')[0].split('<td>')[1]
            category = response.xpath(target_dom + '/td[7]').get().split('</td>')[0].split('<td>')[1]

            yield {
                'url': url,
                'title': title,
                'comment': comment,
                'servings': servings,
                'time': time,
                'calory': calory,
                'genre': genre,
                'category': category
            }

            output = {
                'url': url,
                'title': title,
                'comment': comment,
                'servings': servings,
                'time': time,
                'calory': calory,
                'genre': genre,
                'category': category
            }

            if not os.path.isdir(_DST_DIR):
                os.makedirs(_DST_DIR)

            basename = os.path.basename(url)
            fname, _ = os.path.splitext(basename)
            filepath = os.path.join(_DST_DIR, fname + '_' + title + '.json')
            print('filepath')
            print(filepath)
            with open(filepath, 'w', encoding='utf-8') as w:
                json.dump(output, w, indent=4, ensure_ascii=False)

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
