"""Inventory system module for managing stock data."""
import json
from datetime import datetime
import ast

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a quantity of an item to the stock."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a quantity of an item from the stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Item '{item}' not found in stock.")


def get_qty(item):
    """Return the quantity of a specific item."""
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    with open(file, "r", encoding="utf-8") as f:
        stock_data.clear()
        stock_data.update(json.load(f))


def save_data(file="inventory.json"):
    """Save current inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """Print all items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(item, "->", qty)


def check_low_items(threshold=5):
    """Return a list of items with stock below the given threshold."""
    result = []
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory system operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item("orange", 5)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    ast.literal_eval("'print(\"eval used\")'")
    print("eval used")


main()
