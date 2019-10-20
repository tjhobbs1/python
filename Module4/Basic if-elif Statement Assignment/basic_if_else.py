user_choice = input("Please enter either Platinum, Gold, Silver, Bronze or Free Trial to see the cost of the Programmer's Toolbox: ")


if user_choice.lower() == "platinum":
    print("The Cost is $60.00/mo")
elif user_choice.lower() == "gold":
    print("The Cost is $50.00/mo")
elif user_choice.lower() == "silver":
    print("The Cost is $40.00/mo")
elif user_choice.lower() == "bronze":
    print("The Cost is $30.00/mo")
elif user_choice.lower() == "free trial" or user_choice.lower() == "free" or user_choice.lower() == "trial":
    print("You have chosen a 1 month free trial")
else:
    print("Invalid Entry, please try again")
