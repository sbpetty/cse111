# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.

    # Print the results for the user to see.
    while True:
        gender = input("Please enter your gender (M or F): ").upper()
        if gender in ["M", "F"]:
            break
        else:
            print("Invalid input. Please try again.")

    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    age = compute_age(birth_str)

    pounds = float(input("Enter your weight in U.S. pounds: "))
    inches = float(input("Enter your height in U.S. inches: "))
    kilograms = kg_from_lb(pounds)
    centimeters = cm_from_in(inches)

    print(f"Age (years): {age}")
    print(f"Weight (kg): {kilograms}")
    print(f"Height (cm): {centimeters}")
    print(f"Body mass index: {body_mass_index(kilograms, centimeters)}")
    print(f"Basal metabolic rate (kcal/day): {basal_metabolic_rate(gender, kilograms, centimeters, age)}")

    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    return round(pounds * 0.45359237, 2)


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    return round(inches * 2.54, 1)


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    return round(weight * 10000 / height ** 2, 1)


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper() == 'F':
        return round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))
    elif gender.upper() == 'M':
        return round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
    else:
        return None


# Call the main function so that
# this program will start executing
main()
