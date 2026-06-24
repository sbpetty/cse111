import csv


def main():
    products_dict = read_dictionary("products.csv", 0)
    print(products_dict)
    print_receipt("request.csv", products_dict)


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
    print("Requested Items")

    with open(request_file) as file:
        reader = csv.reader(file)
        
        next(reader)

        for row in reader:
            if len(row) > 0:
                product_key = row[0]
                quantity = row[1]
                product = products_dict[product_key]
                product_name = product[0]
                product_price = product[1]
                print(f"{product_name}: {quantity} @ {product_price}")


if __name__ == "__main__":
    main()