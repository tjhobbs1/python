"""
Program: average_scores.py
Author: Ty Hobbs
Last date modified: 09/10/2019



The purpose of this program is to take a last name, first name and three test scores and return the average of those three scores.
It then displays the results to the user.
"""

def average():
    score1 = int(input("Enter the first score: "))
    score2 = int(input("Enter the second score: "))
    score3 = int(input("Enter the third score: "))
    return (score1 + score2 + score3)/3


if __name__ == '__main__':

    last_name = input("Enter a last name: ")
    first_name = input("Enter a first name: ")
    average_score = average()

    print(last_name,',',first_name, "- average grade:", round(average_score,2))
