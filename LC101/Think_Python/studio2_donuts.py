# Create two strings to make daily changes to the app easier:
donut = "Crunch Jelly"
description = "A traditional jelly donut in which the jelly filling is made entirely of Capn' Crunch Oops! All Berries"

# Display the welcome message and menu
print("Welcome to the Loop Hole!")
print("Today's Manager's Special is:")
print(donut + ":", description)

# Take their order
quantity = float(input("How many would you like?"))
price = float(input("How much would you like to pay per donut?",
         "(suggested price is $4.35 each)"))

# Calculate the total with tax
tax_rate = .05
total = (quantity * price) * (1 + tax_rate)

# Round  and trim to 2 decimal places
adjusted_total = ( round( total * 100 ) /  100)

# Order prep 
print("Ok, let me prepare that for you...")
print("After tax, your total is:", "$" + str(adjusted_total))
print("Thank you for snacking! Loop back around here soon!")
