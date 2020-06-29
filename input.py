# Crash Course User Input, Chapter 7, day 1, 29/06/20
# input() function

# parrot.py,  easy peasy

message = input("Tell me something interesting, and I will repeat it:")
print (message)

# Using input as past of a response:

name = input("What is your name? ")
print (f"Hello {name.title()}")

# Multi Line prompting.

prompt = "if you tell me who you are, we can see if you have permission to enter"
prompt += "\nWhat is your name? "
name = input(prompt)
print(f"Hello {name.title()}, you may pass")

# Above code, += continues the prompt onto a second line of text
# multi line prompt, followed by a clean input line

## INPUT() ALWAYS ASSUMES THE INPUT IS A STR, SO IF YOU EVER NEED NUMERICAL INPUT, AND TO BE ABLE TO
## USE THAT NUMBER FOR ANYTHING USEFUL, YOU MUST DECLARE IT AS AN INTEGER.

age = input("How old are you? ")
age = int(age)
if age >= 20:
    print("This worked because we declared your age as an integer....")
else:
    print("Alright, this worked too, but it wouldnt have if you hadnt declared the int!!")

# above, initially the age input is a STR, we then convert it in the next line to an integer, replace
# str(age, with int(age)

# Another example, to beat it in.

height = input("How tall are you in inches? ")
height = int(height)
if height >= 48:
    print("\nYou are tall enough, hazaa....")
else:
    print("Sorry, you are too short, off you trot...")

# MODULO operator:  "%", modulo gives the remainder of two numbers, ie 7%3 = 1, thats the number
# left after dividing the preceding numbers.

# even_or_odd

number = input("Please enter a number, and I will tell you if its even or odd: ")
number = int(number)
if number % 2 == 0:
    print ("The number is even!")
else:
    print("The number is odd!")
