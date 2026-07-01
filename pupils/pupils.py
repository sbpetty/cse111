import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def main():
    students_list = read_compound_list("pupils.csv")
    extract_birthdate = lambda student : student[BIRTHDATE_INDEX]
    students_by_birthdate = sorted(students_list, key=extract_birthdate)
    extract_given_name = lambda student : student[GIVEN_NAME_INDEX]
    students_by_given_name = sorted(students_list, key=extract_given_name)
    extract_birth_month_and_day = lambda student : student[BIRTHDATE_INDEX][5:]
    students_by_birth_month_and_day = sorted(students_list, key=extract_birth_month_and_day)
    print("Ordered from Oldest to Youngest")
    print_list(students_by_birthdate)
    print()
    print("Ordered by Given Name")
    print_list(students_by_given_name)
    print()
    print("Ordered by Birth Month and Day")
    print_list(students_by_birth_month_and_day)


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(list):
    """Takes a list as a parameter and prints each element of the list
    on a separate line"""

    for item in list:
        print(item)


if __name__ == "__main__":
    main()