name = input("Enter your name: ")
hometown = input("Enter your hometown: ") 
while True:
 try:  #using try block to test the code for an error
    age = int(input("Enter your age: ")) 
    print(f"Name: {name} \nHometown: {hometown} \nAge: {age}")
    break 
 except ValueError: #using except block to manage the error
    print("Enter a numeric value for the age please.")