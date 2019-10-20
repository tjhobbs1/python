"""
Program:  function_keyword.py
Author:  Ty Hobbs
Last Day Modified:  10/08/2019

The purpose of the program is to demo arbitrary argument lists and keyword arguments and output a string

"""


def average_scores(*args, **kwargs):
    # Takes in multiple arguments and averages the scores that were given.
    # Param:
    # Returns the average score and the other arguments that are passed in.

    # Use *args for average calculation
    scores_length=len(args)  # Gets the length of the scores list passed in
    scores_sum=sum(args)  # Gets the SUM of the scores list that is passed in.
    scores_average = round(scores_sum/scores_length,2)  # Gets the average of the score list that is passed in.

    # returns the formatted string.
    return ' '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()]), "average score: ", scores_average


if __name__ == '__main__':
    print(average_scores(45,56,67,name="Ty", gpa="3.80", course="CIS189"))
    print(average_scores(48,67,56,99,88,47,22,first_name="Jim", occupation="chef", hobbies="biking"))
    print(average_scores(93,21,100,0,45,88,last_name="Hobbs", occupation="paramedic", color="blue",town="Ankeny"))
