import re #importing regular expression(re) to use search & IGNORECASE functions.
city = input("What is the capital of France? ")
answer = "Paris" #initializing the correct answer
if re.search(answer , city, re.IGNORECASE): #using if statement to check if the given input matches the correct answer 
    print("The answer is correct!")
else: 
    print("The answer is incorrect!")