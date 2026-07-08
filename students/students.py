import csv


def main():
    students_dict = read_dictionary("students.csv", 0)
    find_student(students_dict)


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


def find_student(students_dict):
    inumber = input("Please enter an I-Number (xxxxxxxxx): ")
    inumber = inumber.replace("-", "")

    if not inumber.isdigit():
        print("Invalid I-Number")
        return

    if len(inumber) == 9:
        if inumber in students_dict:
            print(students_dict[inumber])
        else:
            print("No such student")
    elif len(inumber) > 9:
        print("Invalid I-Number: too many digits")
    else:
        print("Invalid I-Number: too few digits")


if __name__ == "__main__":
    main()