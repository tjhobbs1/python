SENTINEL_VALUE = "-99"
sentinel_value_quit = "quit"
input_list = []

user_input = input("Input Something")
sentinel_value_quit = sentinel_value_quit.islower()

while user_input != sentinel_value_quit:
    print(sentinel_value_quit)
    print(user_input)
    print(type(user_input))
    print("Enter Number")
    break



print("You Quit")
