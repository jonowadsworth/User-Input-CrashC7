# User input practices.
# rental car

print("\tCar rental program.")
car = "Good morning, thank you for accessing the Vehicle rental program"
car += "\nWould you please enter the type of vehicle you would require: "

vehicle = input(car)
print(f"\nThankyou....\nWe are just processing your request for a {vehicle}....")

# Restaurant seating.

party = input("\nGood Evening, thank you for choosing our restraunt, how many seats will your party require?")
party = int(party)
if party > 8:
    print("\nUnfortunately, a group that large would need to wait for a table.")
else:
    print("Excellent, please follow me to your table.")


# Multiples of X game.

game = "Please enter a number, and we can see if it is a multiple of 10: "
game +="If it is not a multiple of 10, I will also inform you of this."
guess = input(game)
guess = int(guess)
if guess % 10 == 0:
    print("Your number is a multiple of 10!")
else:
    print("Sorry, your number is not a multiple of 10")


