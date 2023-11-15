from ._dicts import _MASTER_CATALOGUE, _ARMOR_DICT, _WEAPONS_DICT, _GENERAL_DICT, _TRADE_DICT, _TOOLS_DICT
from ._objects import *

def get_item(term: int | str = None):
    from pprint import pprint
    if isinstance(term, str):
        item_name = term
        if _MASTER_CATALOGUE.get(item_name) is None:
            raise ValueError(f'No item with name {item_name} found')
        print(item_name)
        pprint(_MASTER_CATALOGUE[item_name])
    elif isinstance(term, int):
        item_id = term
        for item in _MASTER_CATALOGUE:
            if _MASTER_CATALOGUE[item]['item_id'] == item_id:
                print(item)
                pprint(_MASTER_CATALOGUE[item])
                return
        raise ValueError(f'No item with id {item_id} found')


def get_category(category: str = None):
    from pprint import pprint
    if category is None:
        from ._objects import _ITEM_CATEGORIES
        pprint(_ITEM_CATEGORIES)
        return
    cat_dict = {}
    for item in _MASTER_CATALOGUE:
        item_category = _MASTER_CATALOGUE[item].get('category')
        if item_category == category.upper():
            cat_dict[item] = _MASTER_CATALOGUE[item]
    cat_dict = sorted(cat_dict.items(), key=lambda x: x[1]['item_id'])
    pprint(cat_dict)
