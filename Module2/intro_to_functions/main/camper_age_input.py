"""
Program: camper_age_input.py
Author: Ty Hobbs
Last date modified: 09/01/2019



The purpose of this program is to take a an age in months and output to the console its equivalent
in years.
"""

# Function that takes the months that have been passed to it and divide it by 12 to give you years.
def convert_to_months(months):
   return months / 12

if __name__ == '__main__':
    # Ask for input in months from user.
    age_in_months = input("Enter a age in months: ")

    # Converts the string to a float and then calls the function.
    age_in_years = convert_to_months(float(age_in_months))

    # Rounds the result to one decimal point.
    age_in_years = round(age_in_years,1)

    # Changes the results to a string.
    age_in_years = str(age_in_years)

    # Prints the results to the console.
    print(age_in_months + " months is equal to " + age_in_years + " years old")
