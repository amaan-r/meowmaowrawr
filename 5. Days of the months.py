Calendar_Dict = {1:31 , 2:28 , 3:31 , 4:30 , 5:31 , 6:30
        , 7:31 , 8:31 , 9:30 , 10:31 , 11:30 , 12:31}
month = int(input("Enter the number of the month: "))
if month < 1 or month > 12: #using if statement to limit the input betweeen 1 to 12.
    print("Incorrect! Enter a number between 1-12")
elif month == 2: #using elif statement if the user input is month 2 .
    leap_year = input("Is it a leap year? [y/n]")
    if   leap_year == "y":
          Calendar_Dict[2] = 29 #modifying the dictionary if user input is a leap year.
          days_in_month = Calendar_Dict[month] #initializing the user input and the dictionary in a single variable if its a leap year
else:
    leap_year = "n"
days_in_month = Calendar_Dict[month] #line 10 but if the input is not a leap year
print(f"There are {days_in_month} days in the month {month}")
