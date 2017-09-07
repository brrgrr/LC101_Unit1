#1 - Runtime error
miles = int(input("How many miles do you have to drive? "))
kilometers = miles * 1.60934
print("That distance is equal to", kilometers, "kilometers")


#2 - Semantic error
spins = input("How many times did you spin? (Enter a negative number for counter-clockwise spins) ")
degrees = (float(spins) * 360) % 360
print("You are facing", degrees, "degrees relative to north")


#3 - Syntax error
current_temp_string = input("Enter a temperature in degrees Fahrenheit: ")
current_temp = int(current_temp_string)
current_temp_celsius = (current_temp - 32) * (5/9)
print("The temperature in Celsius is:", current_temp_celsius)


#4
value_touchdown = int(input("How many points is a touchdown worth?"))
value_field_goal = int(input("How many points is a field goal worth?"))
num_touchdowns = int(input("How many touchdowns were scored? "))
num_field_goals = int(input("How many field goals were scored? "))

total_score = (value_touchdown * num_touchdowns) + (value_field_goal * num_field_goals)

print("The team has", total_score, "points")


# Weekly Graded Assignment
## Generic code with input:
## clicks = int(input("How many clicks?"))
## current_temperature = (clicks % 50) + 40
## print("The temperature is", current_temperature)

click_1 = 0
current_temperature_1 = (click_1 % 50) + 40
print("The temperature is", current_temperature_1)

click_2 = 49
current_temperature_2 = (click_2 % 50) + 40
print("The temperature is", current_temperature_2)

click_3 = 74
current_temperature_3 = (click_3 % 50) + 40
print("The temperature is", current_temperature_3)

click_4 = 51
current_temperature_4 = (click_4 % 50) + 40
print("The temperature is", current_temperature_4)

click_5 = -1
current_temperature_5 = (click_5 % 50) + 40
print("The temperature is", current_temperature_5)

click_6 = 200
current_temperature_6 = (click_6 % 50) + 40
print("The temperature is", current_temperature_6)
