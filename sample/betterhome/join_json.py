import os
import json


_RECIPE_DIR = './dest'
_CATEGORY_DIR = './category'
_METHOD_DIR = './method'
_POSTPROCESS_DIR = './postprocess'


def main():
    if not os.path.isdir(_POSTPROCESS_DIR):
        os.makedirs(_POSTPROCESS_DIR)

    recipe_files = os.listdir(_RECIPE_DIR)

    for f in recipe_files:
        recipe_filepath = os.path.join(_RECIPE_DIR, f)
        category_filepath = os.path.join(_CATEGORY_DIR, f)
        method_filepath = os.path.join(_METHOD_DIR, f)
        with open(recipe_filepath, 'r', encoding='utf-8') as r:
            recipe_data = json.load(r)
        with open(category_filepath, 'r', encoding='utf-8') as c:
            category_data = json.load(c)
        recipe_data.update(category_data)
        try:
            with open(method_filepath, 'r', encoding='utf-8') as m:
                method_data = json.load(m)
            recipe_data.update(method_data)
        except FileNotFoundError:
            print('FileNotFoundError')
            print(method_filepath)
            recipe_data.update({"method": ""})
            pass
        dest_filepath = os.path.join(_POSTPROCESS_DIR, f)
        with open(dest_filepath, 'w', encoding='utf-8') as w:
            json.dump(recipe_data, w, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
