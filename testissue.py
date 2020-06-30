print("Welcome to the ticket office.")
print("\nUnder 3s go free, uner 12s are £10, and over 12 is £15")
print("\nPress 0 to quit")
message = ""
while message != 0:    #while loop starts, with condition the user doesnt type 0
    message = input("How old are you?")  #
    message  = int(message)
    if message < 3:
        print(f"At {message} years old, your cost is £0")
    elif message > 3 and message < 12:
        print(f"At {message} years old, your cost is £10")
    elif message >= 13:
        print(f"At {message} years old, your cost is £15")
    if message != 0:    # this is to stop the printing of the word quit being printed as an
        # actual output to the screen. its IN the loop, but stops an output of quit.
        print(message)  # print the message (providing its not quit....)
