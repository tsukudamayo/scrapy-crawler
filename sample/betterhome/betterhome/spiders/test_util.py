from . import util


def test_preprocess_ingredients():

    test_data1 = ['米', 'あさり（殻つき・砂抜きずみ）', '酒', 'しょうが',
                 'Ａ', '\u3000あさりの蒸し汁＋水', '\u3000しょうゆ', '\u3000みりん']
    test_data2 = ['米用カップ２', '４００ｇ', '大さじ４', '１かけ（１０ｇ）',
                  '合わせて３５０ｍｌ', '大さじ１／２', '小さじ１']
    servings = '〈4人分〉'

    expected = {
        '食材': '4人分',
        '米': '米用カップ２',
        'あさり（殻つき・砂抜きずみ）': '４００ｇ',
        '酒': '大さじ４',
        'しょうが': '１かけ（１０ｇ）',
        'Ａ': {
            'あさりの蒸し汁＋水': '合わせて３５０ｍｌ',
            'しょうゆ':  '大さじ１／２',
            'みりん': '小さじ１'
        }
    }

    result = util.process_ingredients(test_data1, test_data2, servings)
    print('result')
    print(result)

    assert result == expected


def test_process_servings():
    test_data = '〈4人分〉'
    expected = '4人分'
    result = util.process_servings(test_data)

    assert result == expected
