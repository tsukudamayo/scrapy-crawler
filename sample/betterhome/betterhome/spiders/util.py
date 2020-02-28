import re
from typing import List, Dict


def process_ingredients(ingredients: List, quantity: List, servings: str) -> Dict:
    print('servings')
    servings = process_servings(servings)
    print(servings)
    preprocesser = Preprocesser(ingredients, quantity, servings)
    output = preprocesser.build()

    return output


def process_servings(strings: str) -> str:
    regex = re.compile('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]')
    strings = regex.sub('', strings)

    return strings


class Preprocesser:
    def __init__(self, ingredients: List, quantity: List, servings: str):
        self.ingredients = ingredients
        self.quantity = quantity
        self.servings = servings
        self.output = {}
        self.ingque = iter(ingredients)
        self.quaque = iter(quantity)
        self.group = None
        self.group_pattern = re.compile(r'^\u3000')

    def build(self):
        self.output['食材'] = self.servings
        self.ingque.__next__()
        for i in self.ingredients:
            try:
                next_ing = self.ingque.__next__()
                is_group_next = self.group_pattern.match(next_ing)
            except StopIteration:
                is_group_next = None

            print('i : ', i)
            print('next ing : ', next_ing)

            if is_group_next and not self.group:
                print('match')
                self.group = i
                self.output[self.group] = {}
                continue
            elif is_group_next and self.group:
                print('match')
                value = self.quaque.__next__()
                self.output[self.group].update({i.replace('\u3000', ''): value})
            elif not is_group_next and self.group:
                print('match')
                value = self.quaque.__next__()
                self.output[self.group].update({i.replace('\u3000', ''): value})
                self.group = None
            else:
                print('not match')
                value = self.quaque.__next__()
                self.output.update({i: value})
                self.group = None                

        return self.output

