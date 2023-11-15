import os
import json

def load_json(path):
    """Load a JSON file from the given path."""
    with open(path, 'r') as f:
        return json.load(f)
    
# Desc: Loads dicts from JSON files
_dicts = [d[:-5] for d in os.listdir(os.path.abspath(os.path.dirname(__file__))) if d.endswith('.json') and d != '__init__.py']


def load_dict(name):
    if name in _dicts:
        return load_json(f'{os.path.join(os.path.dirname(__file__), name)}.json')
    else:
        raise ValueError(f'No such dict: {name}')
    
def load_all_dicts():
    return {d: load_dict(d) for d in _dicts}

# Desc: Loads lists from text files
_lists = [d[:-9] for d in os.listdir(os.path.dirname(__file__)) if d.endswith('_list.txt') and d != '__init__.py']

def load_list(name):
    if name not in _lists:
        raise ValueError(f'No such list: {name}')
    with open(f'{os.path.join(os.path.dirname(__file__), name)}_list.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]

def _set_ids(MASTER_CATALOGUE):
    _ITEM_ID = 0
    for I, catalogue in enumerate(_MASTER_CATALOGUE):
        if I != 0:
            _ITEM_ID += len(_MASTER_CATALOGUE.copy()[catalogue])
        for name, info in _MASTER_CATALOGUE[catalogue].copy().items():
            _MASTER_CATALOGUE[catalogue][name]['item_id'] = _ITEM_ID
            _ITEM_ID += 1
        
    
_MASTER_CATALOGUE = load_all_dicts()

_set_ids(_MASTER_CATALOGUE)

_ARMOR_DICT = _MASTER_CATALOGUE['armor']
_WEAPONS_DICT = _MASTER_CATALOGUE['weapons']
_GENERAL_DICT = _MASTER_CATALOGUE['general_items']
_TRADE_DICT = _MASTER_CATALOGUE['trade_items']
_TOOLS_DICT = _MASTER_CATALOGUE['tools']