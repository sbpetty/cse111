import csv
from datetime import datetime


STORE_NAME = "Walmart"
SALES_TAX_RATE = 0.06


def main():
    try:
        products_dict = read_dictionary("products.csv", 0)
        print(products_dict)
        print_receipt("request.csv", products_dict)
    except FileNotFoundError:
        print("Error: file doesn't exist")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    with open(filename) as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:
            if len(row) > 0:
                key = row[key_column_index]
                row.pop(key_column_index)
                if len(row) == 1:
                    dictionary[key] = row[0]
                else:
                    dictionary[key] = row

    return dictionary


def print_receipt(request_file, products_dict):
    """Reads data from a request csv and prints a formatted receipt.

    Parameters:
        request_file: a csv file containing keys and quantity for a grocery order.
        products_dict: the dictionary containing all the data on the products
            with the product number as the key.
    Return:
        Nothing
    """
    print(f"{STORE_NAME}\n")

    subtotal = 0.0
    try:
        with open(request_file) as file:
            reader = csv.reader(file)
            
            next(reader)

            for row in reader:
                if len(row) > 0:
                    product_key = row[0]
                    quantity = float(row[1])
                    product = products_dict[product_key]
                    product_name = product[0]
                    product_price = float(product[1])
                    print(f"{product_name}: {quantity} @ {product_price}")
                    subtotal += product_price * quantity

            print(f"\nSubtotal: {subtotal:.2f}")
            sales_tax = subtotal * SALES_TAX_RATE
            print(f"Sales tax: {sales_tax:.2f}")
            total = subtotal + sales_tax
            print(f"Total: {total:.2f}")
            print()
            print(f"Thank you for shopping at {STORE_NAME}.")
            timestamp = datetime.now()
            print(f"{timestamp:%a %b %d %H:%M:%S %Y}")
    except KeyError:
        print("Error: invalid product key")

if __name__ == "__main__":
    main()