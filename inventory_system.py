"""
Inventory Management System
---------------------------
Handles adding, removing, loading, and saving stock data securely.
Includes input validation, proper logging, and error handling.
"""

import json
import logging
from datetime import datetime


# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def add_item(stock_data, item="default", qty=0, logs=None):
    """Add quantity of an item to stock_data."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input: item=%s, qty=%s", item, qty)
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def remove_item(stock_data, item, qty):
    """Remove quantity of an item from stock_data."""
    try:
        if item not in stock_data:
            logging.warning(
                "Attempted to remove non-existent item: %s",
                item
            )
            return
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed %s from stock_data", item)
    except (KeyError, TypeError) as err:
        logging.error("Error removing item '%s': %s", item, err)


def get_qty(stock_data, item):
    """Return the quantity of a given item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from a JSON file and return it."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logging.info(
                "Inventory data loaded successfully from %s",
                file_path
            )
            return data
    except FileNotFoundError:
        logging.warning(
            "File not found: %s. Starting with empty stock.",
            file_path
        )
        return {}
    except json.JSONDecodeError:
        logging.error("Error decoding JSON from %s.", file_path)
        return {}


def save_data(stock_data, file_path="inventory.json"):
    """Save inventory data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)
    logging.info("Inventory data saved successfully to %s", file_path)


def print_data(stock_data):
    """Print a report of all inventory items."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    """Return a list of items with quantity below the given threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution block for inventory system."""
    stock_data = load_data()

    add_item(stock_data, "apple", 10)
    add_item(stock_data, "banana", 3)
    remove_item(stock_data, "apple", 3)

    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")

    save_data(stock_data)
    print_data(stock_data)


if __name__ == "__main__":
    main()
