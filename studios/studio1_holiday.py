'''
It is possible to name the days 0 through 6, where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day 3 (a Wednesday) and you return home after 10 nights, you arrive home on day 6 (a Saturday).

Write a general version of the program which asks for the day number that your vacation starts on and the length of your holiday, and then tells you the number of the day of the week you will return on.
'''

start = int(input("What day does your vacation start?"))
length = int(input("What is the length of your holiday?"))

return_day = (start + length) % 7

print("You will return on day", return_day)



