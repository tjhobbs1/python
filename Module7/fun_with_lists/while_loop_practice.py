def start_program():
    score = 0
    while score != -1:
        try:
            score = int(input("Enter a number or -1 to stop"))
            student_score.append(score)
            print(score)
        except ValueError:
            print("Something bad happened!") #An error occurred, but the script continues
        except:
            print("Something worse happened!")
            raise #a worse error occurred, now we kill it
    student_score.pop()
    print(student_score)

student_score =[]  # Creates an empty list to store the scores.
student_name = input("Enter student name: ")  # Gets the users input of the student's name.






if __name__ == '__main__':
    start_program()
