# CharObj
## Description
CharObj is a package to allow for the creation/management of items for use in a text-based RPG game. It is designed to be used with the [CharActor](https://github.com/primal-coder/CharActor) package, but can be used independently.

## Installation
To install CharObj, use the following command:

```bash
pip install CharObj
```

## Usage
CharObj can be used as a Python module or as a command-line tool.

### Module
To use CharObj as a module, import it into your Python script:

```python
import CharObj
```

### Command-Line
To use CharObj as a command-line tool, use the following command:

```bash
python -m CharObj -h
# usage: CharObj [-h] {Get,Make} ...

# options:
#   -h, --help  show this help message and exit

# Commands:
#   {Get,Make}
#     Get       Gather information about an item by name or id
#     Make      Create an item
```

## Examples

### Module

Each already existing item is stored in its respective json file in the 'dict' directory. Upon importing the module items are accessible through the 'CharObj.Goods' or 'CharObj.Armory' classes. A new instance of the item can be created by simply calling its name as a function.


```python
>>> import CharObj
# Create a new instance of an item
>>> gold_coin_1 = CharObj.Goods.goldcoin()
>>> gold_coin_2 = CharObj.Goods.goldcoin()
# Print the name of the item
>>> print(gold_coin_1.name)
Gold Coin
>>> print(gold_coin_2.name)
Gold Coin
# Check if the two items are the same
>>> print(gold_coin_1 == gold_coin_2)
False
```

### Command-Line

```bash
$ python -m CharObj Get 1
Gold Coin
{'binding': 'UNBOUND',
 'category': 'MISC',
 'description': 'A gold coin',
 'item_id': 1,
 'material': 'GOLD',
 'mundane': True,
 'name': 'Gold Coin',
 'quality': 'COMMON',
 'quest_item': False,
 'relic': False,
 'stackable': True,
 'value': [1, 'gp'],
 'weight': [0.01, 'kg']}
```
