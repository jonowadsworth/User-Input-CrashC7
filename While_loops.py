# While Loops, Crash Course, chapter 7, p118, 30/6/20

# A FOR loop runs a code, or collection of items, through ONCE.
# A WHILE loop runs for as long as, or WHILE, a certain condition is true. or false possibly...

# Example:

current_number = 1

while current_number <= 5: # conditions of the while function.
    print(current_number) # do this.
    current_number +=1 # inside loop, add 1 to counter, code runs WHILE current number <= 5

# User input, with a while loop, with a close program depending on user input.

prompt = "Tell me something, and i will repeat it for you: "
prompt +="\nTo exit the program, enter `quit` to close the program."
message = ""    #assign blank str to message var to keep track of user input
while message != "quit":    #while loop starts, with condition the user doesnt type quit
    message = input(prompt)     #at first, there hasnt been any user input, so the program wont
    # progress. To solve that you assign prompt to the message so the while loop has something to
    #compare itself to. prompt doesnt equate to quit, so it continues the loop. then user inputs
    if message !="quit":    #this is to stop the printing of the word quit being printed as an
        #actual output to the screen. its IN the loop, but stops an output of quit.
        print(message)  #print the message (providing its not quit....)


# Using FLAGS. Flags determine whether a program should continue or not. Useful if there are several
# conditions that could impact whether a program should run or not. Flags are Boolean, true or false
prompt = "Tell me SOMETHING, and i will repeat it for you: "
prompt +="\nTo exit the program, enter `quit` to close the program."

active = True
while active:
    message = input(prompt)
    if message =="quit":
        active = False
    else:
        print(message)

# Using BREAK to exit a loop

prompt = "Name a city, you have visited: "
prompt +="\nTo exit the program, enter `quit` to close the program."

while True:     # A loop that starts with WHILE TRUE: runs forever until it reaches a BREAK statement.
    city = input(prompt)    # prompt in brackets to engage the loop, as no input as yet

    if city =="quit":   #quit condition, while loop continues as long as quit isnt entered
        break   # breaks the code at this point: ends the loop end exits.
    else:   #if quit isnt met, print the following.
        print(f"I would love to visit {city.title()}, it sounds great.")

# CONTINUE STATEMENTin a LOOP
# Rather than BREAKing out of a loop and closing, you can use CONTINUE to return to the beginning
# of a loop based on the result of a CONDITIONAL TEST. For example, a loop that counts from 1-10
# but only prints the ODD numbers in that range.

new_number = 0      #sets our number to 0
while new_number <10:       #while loop starts, num is < 10 so it starts
    new_number +=1          # num = num + 1, to increment up
    if new_number %2 == 0:  # if num divided by 2 = 0, (ie, NOT ODD) CONTINUE (ignore the print line
                            # and loop back to the start)
        continue            # either loop to start, or goto next line if num % 2 == 0 is false
    print(new_number)       # depending on num, execute this line.


