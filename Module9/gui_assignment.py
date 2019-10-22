"""
Program:  gui_assignment.py
Author:  Ty Hobbs
Last Day Modified:  10/20/2019

The purpose of the program is show a basic use of a GUI application in Python.
"""
import tkinter

#  Functions that add messages when a selection is made in the GUI.
def pick_breakfast():
    label.config(text="Good Morning")

def pick_2_breakfast():
    label.config(text="Yum")

def pick_lunch():
    label.config(text="Good Afternoon")

def pick_dinner():
    label.config(text="Good Evening")

# Creates the main GUI window
m = tkinter.Tk()
m.title('Favorite Meal')

# Creates the breakfast checkbox in the GUI window.
breakfast = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=breakfast, command=pick_breakfast).grid(row=1)

# Creates the second breakfast checkbox in the GUI window.
second_breakfast = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=second_breakfast, command=pick_2_breakfast).grid(row=2)

# Creates the lunch checkbox in the GUI window.
lunch = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=lunch, command=pick_lunch).grid(row=3)

# Creates the dinner checkbox in the GUI window.
dinner = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=dinner, command=pick_dinner).grid(row=4)

# Creates the default label.
label = tkinter.Label(m, text="Choose your favorite meal")
label.grid(row=5)

# Creates the exit button.
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)

m.mainloop()  # infinite loop that waits for events to happen
