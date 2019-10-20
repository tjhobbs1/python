def get_input():
    # This function gets and checks user input for the make_list() function.
    # No Params
    # Returns user_input which should be a integer.
    list_of_numbers = []
    user_input = 0

    while user_input != -1:
        try:
            # test that the user input is an number else throw a ValueError
            user_input = int(input("Enter a number: "))
            list_of_numbers.append(user_input)
        except ValueError:
            # Show an error if the value is not a number and then ask for a new number.
            print("Error")
            user_input = int(input("Enter a number: "))
        except:
            print("Something worse happened!")
            raise #a worse error occurred, now we kill it

    return list_of_numbers


if __name__ == '__main__':
   print(get_input())
