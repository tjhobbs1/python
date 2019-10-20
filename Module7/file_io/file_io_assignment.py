"""
Program:  file_io_assignment.py
Author:  Ty Hobbs
Last Day Modified:  10/08/2019

The purpose of the program is to get a users input of student's test scores and write them to an external file.
At the end of the program it will print the file to the console.
"""


def write_to_file(name, *args):
    # The purpose of this function is to take in a name and student scores and then write them to a file.
    # Param:  name takes a in a student's name.
    # Param:  Takes in a list of student scores.
    # Returns:  None

    f = open('student_info.txt', 'a')
    input_list = args  # Assigns the passed in scores to input_list
    input_score = (name,input_list)  # Creates a tuple to be written to the file.
    input_score = str(input_score)  # Cast to a string so it can be written to a file.

    #  Loops through the input_scores and writes them to a file.
    for t in input_list:
       f.writelines(input_score)
    f.write('\n')  # Inserts a line break
    f.close()  # Closes the file for memory management.

def get_student_info():
    #  The purpose of this function is to get the name and scores of a student.  It will then send those parameters
    #  to the write_to_file function.
    # Params:  none
    # Return:  None,  calls the write_to_file sending the name and scores

    student_score =[]  # Creates an empty list to store the scores.
    student_name = input("Enter student name: ")  # Gets the users input of the student's name.
    score = 0  # variable to store the test score.

    while score != -1:
        # While loop that keeps prompting the user for a score till -1 is used to exit the loop.
        # It will store these scores in the student_scores variable.
        try:
            score = int(input("Enter a number or -1 to end: "))
            student_score.append(score)
            print(score)
        except ValueError:
            print("Error: Enter a number") #An error occurred, but the script continues
        except:
            print("Error: Program Ended")
            raise #a worse error occurred, the program stops
    student_score.pop()
    print(student_score)
    write_to_file(student_name,student_score)


def read_from_file():
    # The purpose of this function is to read from the file and display on the console.
    # Params:  None
    # Return:  Prints to the console.

    f = open('student_info.txt', 'r')  # Opens the file.
    line1 = f.read()  # Reads data from the file.
    print(line1)   # Prints data to the console.
    f.close()   # Closes the file for memory management.


if __name__ == '__main__':
    get_student_info()
    read_from_file()
