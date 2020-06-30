# While loop practices. crash course Chapter 7 p 123, 30/6/20

# Pizza toppings.

pizza_top = "Please type what topping you would like on your pizza."
pizza_top += "\nOnce you have entered all of your toppings, type `done` to exit."

pizza = ""
while pizza != "done":
    pizza =input(pizza_top)
    if pizza != "done":
        print(f"Thank you, {pizza} has been added to your order.")


# Movie Ticket prices.
print("\tWELCOME TO THE TICKET BOOKING OFFICE.")
age = input("How old are you, your age will determine your ticket price: ")
age  = int(age)
if age < 3:
    price = 0
    print(f"at age {age}, your admission price is £{price}")
elif age < 12:
    price = 10
    print(f"at age {age}, your admission price is £{price}")
elif age > 12:
    price = 15
    print(f"at age {age}, your admission price is £{price}")
