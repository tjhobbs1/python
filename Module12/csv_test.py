import csv

class CountyDemos:
    def __init__(self,population,num_households):
        self.population = population
        self.num_households = num_households

with open('Example CSV.csv') as csv_file:
 csv_reader = csv.reader(csv_file, delimiter=',')
 line_count = 0
 for row in csv_reader:
        # I'm treating the first row different because it is the header row
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    else:
        print(row)
        line_count += 1
    print (f'processed {line_count} rows')

