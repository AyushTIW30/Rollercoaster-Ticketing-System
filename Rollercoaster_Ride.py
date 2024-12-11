def calculate_price(age):
    """Calculate the ticket price based on age."""
    if age < 12:
        return 5
    elif age <= 18:
        return 7
    else:
        return 12

print("Welcome to the Rollercoaster Adventure!")

height = int(input("What is your height in cm? "))

if height > 120:
    print("\nGreat! You can ride the rollercoaster!")
    age = int(input("Please enter your age: "))

    price = calculate_price(age)
    print(f"\nYour ticket price is: ${price}.")
else:
    print("\nSorry, you must be taller than 120 cm to ride the rollercoaster.")
