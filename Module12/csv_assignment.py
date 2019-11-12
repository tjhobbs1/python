"""
Program:  csv_assignment.py
Author:  Ty Hobbs
Last Day Modified:  11/12/2019

The purpose of the program demo the use of reading from a CSV file and using the data that it contains.
"""
import csv

# A class with all the attributes from the CSV file
class Census_data:
    """
    This a class that creates and object of all the census data that can be used in the program.
    """
    def __init__(self,rank,county,per_capita_income,median_household_income,median_family_income,population,num_of_households):
        """
        Constructor
        :param rank: The rank of the county.
        :param county: The county name.
        :param per_capita_income: The per capita income of that county
        :param median_household_income: The median household income of that county
        :param median_family_income:  The median family income for that county
        :param population:  The population of the county.
        :param num_of_households:  The number of households in the county.
        :return:
        """
        self.rank = rank
        self.county = county
        self.per_capita_income = per_capita_income
        self.median_household_income = median_household_income
        self.median_family_income = median_family_income
        self.population = population
        self.num_of_households = num_of_households



with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    """Open the CSV file and determine the delimiter"""
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    # initialize empty dictionary


    next(csv_reader)  # Skips the first "Header" row

    census={}
    # Loop over each row in the file
    for row in csv_reader:

        if row[0] =='':
            continue  # Skip State of Iowa and US

        census[str(row[1])] = Census_data(row[0],row[1],row[2],row[3],row[4],row[5],row[6])


    # Determine the total populatiomn of Iowa in 2010
    pop_sum = 0
    for key in census:
        pop_sum += int(census[key].population.replace(',',''))
    print(f'The 2010 Iowa Population was: {pop_sum}')

    # Determine the Population of Dallas County

    print(f'The Population of Dallas County in 2010 was: {census["Dallas"].population}')

    # Determine the Number of  households in Dallas County
    print(f'The Number of households in Dallas County in 2010 was: {census["Dallas"].num_of_households}')








