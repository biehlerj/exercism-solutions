"""Functions to keep track and alter inventory."""

from collections import Counter
from typing import TypeAlias

Inventory: TypeAlias = dict[str, int]
Items: TypeAlias = list[str]


def create_inventory(items: Items) -> Inventory:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    return dict(Counter(items))


def add_items(inventory: Inventory, items: Items) -> Inventory:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item, count in Counter(items).items():
        inventory[item] = inventory.get(item, 0) + count

    return inventory


def decrement_items(inventory: Inventory, items: Items) -> Inventory:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item, count in Counter(items).items():
        if item in inventory:
            inventory[item] = max(0, inventory[item] - count)

    return inventory


def remove_item(inventory: Inventory, item: str) -> Inventory:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    inventory.pop(item, None)

    return inventory


def list_inventory(inventory: Inventory) -> list[tuple[str, int]]:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(k, v) for k, v in inventory.items() if v > 0]
