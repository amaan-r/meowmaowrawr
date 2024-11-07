def odd_or_even(): 
    number = float(input("Enter a number: "))
    if number % 2 == 0: 
        return("Given number is even") #if the input is even, exit the function and return the string to where the function was called
    else:
        return("Given number is odd")#else return the given string 
user_input = odd_or_even() #calling the function
print(user_input)