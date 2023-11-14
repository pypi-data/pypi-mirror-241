from ._dicts import *
from ._objects import *

_ARMOR_DICT = load_dict('armor')
_WEAPONS_DICT = load_dict('weapons')
_GENERAL_ITEMS_DICT = load_dict('general_items')
_TRADE_ITEMS_DICT = load_dict('trade_items')

_MASTER_DICT = {**_TRADE_ITEMS_DICT, **_GENERAL_ITEMS_DICT, **_WEAPONS_DICT, **_ARMOR_DICT}

def get_item(term: int | str = None):
    from pprint import pprint
    if isinstance(term, str):
        item_name = term
        if _MASTER_DICT.get(item_name) is None:
            raise ValueError(f'No item with name {item_name} found')
        print(item_name)
        pprint(_MASTER_DICT[item_name])
    elif isinstance(term, int):
        item_id = term
        for item in _MASTER_DICT:
            if _MASTER_DICT[item]['item_id'] == item_id:
                print(item)
                pprint(_MASTER_DICT[item])
                return
        raise ValueError(f'No item with id {item_id} found')


def get_category(category: str = None):

    from pprint import pprint
    if category is None:
        from ._objects import _ITEM_CATEGORIES
        pprint(_ITEM_CATEGORIES)
        return
    cat_dict = {}
    for item in _MASTER_DICT:
        item_category = _MASTER_DICT[item].get('category')
        if item_category == category.upper():
            cat_dict[item] = _MASTER_DICT[item]
    cat_dict = sorted(cat_dict.items(), key=lambda x: x[1]['item_id'])
    pprint(cat_dict)
