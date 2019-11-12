#!/usr/bin/env python
# coding: utf-8

# # Module 12: Data Gathering, Custom Exceptions, Abstracting

# ## Topic 1: Gathering Data Using Classes

# ### Let's learn how to import data from a CSV file

# ### A CSV file is a file format that is structured so that many different applications are able to access the data easily.  
# ### CSV stands for comma separated value

# ![csv_sample.png](attachment:csv_sample.png)

# In[ ]:


import csv
with open('NOAA Des Moines Weather data 11_18 to 10_19.csv') as csv_file:
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


# ### Now that we can import data into our program, let's do some OOP, putting the data into an object with attributes

# ![CityWeatherDataUML.png](attachment:CityWeatherDataUML.png)

# ### This code uses an OrderedDict data type.  OrderedDict is just a dictionary that remembers the order items were added.  This guarantees that the items added to the dictionary can be pulled from the dictionary in the same order they were added.

# In[ ]:


from collections import OrderedDict

class CityWeatherData:
    def __init__(self,date,day_max_temp,day_min_temp,day_ave_temp,day_precip,day_new_snow):
        self.date = date
        self.day_max_temp = day_max_temp
        self.day_min_temp = min_temp
        self.day_ave_temp = ave_temp
        self.day_precip = precip
        self.day_new_snow = new_snow
    
    def max_max_temp_week(self):
        date_max_temp_dict = OrderedDict()
        sum_temps = 0
        date_list = []
        temp_list= []
        for r in range (len(self.date)):
            date_max_temp_dict[self.date[r]] = int(self.day_max_temp[r])
        for k,v in date_max_temp_dict.items():
            date_list.append(k)
            temp_list.append(v)
            if len(date_list) >= 7:
                if sum(temp_list)/7 > sum_temps:
                    sum_temps = sum(temp_list)/7
                    date_first = date_list[0]
                    date_last = date_list[6]
            if len(date_list) == 7:
                del date_list[0]
                del temp_list[0]
        return (f'Maximum Max Temp: {sum_temps} from {date_first} to {date_last}')
                
    def min_max_temp_week(self):
        date_max_temp_dict = OrderedDict()
        sum_temps = 1000
        date_list = []
        temp_list= []
        for r in range (len(self.date)):
            date_max_temp_dict[self.date[r]] = int(self.day_max_temp[r])
        for k,v in date_max_temp_dict.items():
            date_list.append(k)
            temp_list.append(v)
            if len(date_list) >= 7:
                if sum(temp_list)/7 < sum_temps:
                    sum_temps = sum(temp_list)/7
                    date_first = date_list[0]
                    date_last = date_list[6]
            if len(date_list) == 7:
                del date_list[0]
                del temp_list[0]
        return (f'Minimum Max Temp: {sum_temps} from {date_first} to {date_last}')


# In[ ]:


#NOTE: THIS IS JUST TO DISPLAY THE LARGE CLASS IN PARTS
#from collections import OrderedDict
#class CityWeatherData:
#    def __init__(self,date,day_max_temp,day_min_temp,day_ave_temp,day_precip,day_new_snow):
#        self.date = date
#        self.day_max_temp = day_max_temp
#        self.day_min_temp = min_temp
#        self.day_ave_temp = ave_temp
#        self.day_precip = precip
#        self.day_new_snow = new_snow


# In[ ]:


#NOTE: THIS IS JUST TO DISPLAY THE LARGE CLASS IN PARTS
#def max_max_temp_week(self):
#        date_max_temp_dict = OrderedDict()
#        sum_temps = 0
#        date_list = []
#        temp_list= []
#        for r in range (len(self.date)):
#            date_max_temp_dict[self.date[r]] = int(self.day_max_temp[r])
#        for k,v in date_max_temp_dict.items():
#            date_list.append(k)
#            temp_list.append(v)
#            if len(date_list) >= 7:
#                if sum(temp_list)/7 > sum_temps:
#                    sum_temps = sum(temp_list)/7
#                    date_first = date_list[0]
#                    date_last = date_list[6]
#            if len(date_list) == 7:
#                del date_list[0]
#                del temp_list[0]
#        return (f'Maximum Max Temp: {sum_temps} from {date_first} to {date_last}')


# ### Now that we have our class with some methods, we can instantiate our new des_moines object

# ![csv_sample_with_list_circles.png](attachment:csv_sample_with_list_circles.png)

# In[ ]:


import csv
with open('NOAA Des Moines Weather data 11_18 to 10_19.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # Short way to initialize multiple empty lists
    date,max_temp,min_temp,ave_temp,precip,new_snow = ([] for i in range(6))
    
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        date.append(row[0])
        max_temp.append(row[1])
        min_temp.append(row[2])
        ave_temp.append(row[3])
        precip.append(row[4])
        new_snow.append(row[5])
    des_moines = CityWeatherData(date,max_temp,min_temp,ave_temp,precip,new_snow)


# In[ ]:


print(des_moines)


# In[ ]:


print(des_moines.max_max_temp_week())
print(des_moines.min_max_temp_week())


# ## Topic 2: Custom Exceptions

# ### While Python does come with a significant number of built in exceptions, there are times when you may want to have a specific exception class for your programs

# ### Custom exception classes should inherit the built in "Exception" class

# ### A simple example of a custom exception class is just a defined class with pass as the body.  You should have some kind of commenting in these classes explaining what the exception is and when it happens.

# In[ ]:


class NumberTooLow(Exception):
    # This custom exception gets raised if the value entered is too low
    pass

class NumberTooHigh(Exception):
    # This custom exception gets raised if the value entered is too high
    pass


# ### When using these simple exception classes, you can just pass the error message when raising the exception.

# In[ ]:


your_number = int(input("Give me an integer between 1 and 10: "))
if your_number < 1:
    raise NumberTooLow("That number is lower than asked for")
elif your_number > 10:
    raise NumberTooHigh("That number is higher than asked for")


# ### Custom exception classes can also have default messages

# In[ ]:


class NumberTooLow(Exception):
    # This custom exception gets raised if the value entered is too low
    def __init__(self,message=None):
        if message==None:
            message="Your number was far too low for my tastes"
        super(NumberTooLow, self).__init__(message)
    
class NumberTooHigh(Exception):
    # This custom exception gets raised if the value entered is too high
    def __init__(self,message=None):
        if message==None:
            message="What kind of crazy high number are you sending me?"
        super(NumberTooHigh,self).__init__(message)
    pass


# In[ ]:


your_number = int(input("Give me an integer between 1 and 10: "))
if your_number < 1:
    raise NumberTooLow
elif your_number > 10:
    raise NumberTooHigh


# ## Topic 3: Abstraction

# ### Abstract classes are special classes that cannot be instantiated.  Any class that inherits these abstract classes must override any abstract methods of the abstract class

# ### In the same way that a class can be considered a blueprint for objects, an abstract class can be considered a blueprint for other classes

# In[ ]:


from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def age_range(self):
        return "A person's age range is between 0 and 120"
    
class Child(Person):
    def age_range(self):
        return "my age is between 0 and 18."
jimmy = Child()
print(jimmy.age_range())


# ### A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden

# In[ ]:


from abc import ABC, abstractmethod

class Person(ABC):
    def number_of_limbs(self):
        return "A person typically has 4 limbs"
    
    @abstractmethod
    def age_range(self):
        return "A person's age range is between 0 and 120"
    
class Child(Person):
    def age_range(self):
        return "my age is between 0 and 18. " + super().age_range()

jimmy = Child()
print(jimmy.age_range())
print(jimmy.number_of_limbs())
#billy = Person()

