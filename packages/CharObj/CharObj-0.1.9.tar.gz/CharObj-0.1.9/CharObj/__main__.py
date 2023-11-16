from argparse import ArgumentParser

argparser = ArgumentParser(prog='CharObj')
subparsers = argparser.add_subparsers(title='Commands', dest='command')

getparser = subparsers.add_parser('Get', help='Gather information about an item by name or id')
makeparser = subparsers.add_parser('Make', help='Create an item')

getparser.add_argument('--category', '-c', action='store_true', help='Return all items in a given category')
getparser.add_argument(dest='TERM', type=str, nargs='?', help='The term related to the search. If no flag is \
present the term will be treated as either an item name or id.')

makeparser.add_argument('--name', '-n', type=str)
makeparser.add_argument('--item_id', '-id', type=int)
makeparser.add_argument('--slot', '-s', type=str)
makeparser.add_argument('--weight', '-w', type=float)
makeparser.add_argument('material', type=str)
makeparser.add_argument('mundane', type=bool)
makeparser.add_argument('description', type=str)
makeparser.add_argument('quality', type=str)
makeparser.add_argument('value', type=int)
makeparser.add_argument('binding', type=bool)
makeparser.add_argument('quest_item', type=bool)
makeparser.add_argument('relic', type=bool)
makeparser.add_argument('armor_class', type=int)
makeparser.add_argument('set_name', type=str)

args = argparser.parse_args()

if __name__ == '__main__':
    from CharObj import get_item, get_category
    if args.command == 'Get':
        if args.category:
            get_category(args.TERM)
        elif args.TERM.isdigit():
            get_item(int(args.TERM))
        else:
            get_item(args.TERM)
    elif args.name == 'make':
        from CharObj import _Item
        print(_Item(
            item_id=args.item_id,
            name=args.name,
            slot=args.slot,
            weight=args.weight,
            material=args.material,
            mundane=args.mundane,
            description=args.description,
            quality=args.quality,
            value=args.value,
            binding=args.binding,
            quest_item=args.quest_item,
            relic=args.relic,
            armor_class=args.armor_class,
            set_name=args.set_name
        ))
    else:
        raise ValueError('Invalid command')