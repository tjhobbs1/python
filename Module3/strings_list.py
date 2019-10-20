"""
Program: strings_list.py
Author: Ty Hobbs
Last date modified: 09/09/2019



The purpose of this program is to take a string and use the different methods on that string to see the results.
"""

favorite_movie_character = "Chevy Chase in Christmas Vacation"  # Starting String.

print('Starting String: ', favorite_movie_character)  # Prints to the console the starting string so you can observe the changes.

print('Example of capitalize method: ',favorite_movie_character.capitalize())  # Returns the first letter of the string in caps and the rest in lowercase.

find_result = favorite_movie_character.find('Christmas') # Find the location of the word Christmas in the string.

print('The word Christmas is at location: ' , find_result,'.') # Prints the result of find().

index_result = favorite_movie_character.index('in')  # Gives the index level in the string for the word 'in'.

print("The index of the word in is: ", index_result) # Prints the result of index method.

isalnum_result = favorite_movie_character.isalnum()  # Checks to see if all the characters of the string are alphanumeric.

print('The result of isalnum() is: ', isalnum_result) # Prints the result of isalnum_result.

isalpha_results = favorite_movie_character.isalpha()  # Checks to see if all characters of the string are alphabet letters

print('The string contains only alphabet characters: ', isalpha_results)  # Prints the results of isalpha_results.

isdigit_results = favorite_movie_character.isdigit()  # Checks to see if all the characters are digits.

print('The string contains only numbers: ', isdigit_results)  # Prints the results of isdigit.

result_islower = favorite_movie_character.islower()  # Returns true if all characters of the string are in lowercase.

print('All characters of the string are in lowercase: ', result_islower)  # Prints the results of result_islower

result_isupper = favorite_movie_character.isupper()  # Returns true if all characters of the string are in uppercase.

print('All characters of the string are in uppercase: ', result_isupper)  # Prints the results of result_isupper

result_isspace = favorite_movie_character.isspace()  # Checks the string to see if only contains spaces.

print('The string contains only spaces: ', result_isspace)  # Prints the results of result_isspace.

result_startswith = favorite_movie_character.startswith("Chevy")  # Checks the string to see if it starts with the word Chevy.

print("The string starts with Chevy:" ,result_startswith)  # Prints the results of result_startswith.






