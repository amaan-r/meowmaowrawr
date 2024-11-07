names = ["Jake" , "Zac" , "Ian" , "Ron" , "Sam" , "Dave"] #declaring a list
user_input = input("Enter the name you want to find: ")
if user_input in names:
    print( f"{user_input} is in the list") 
else:
    print("Given name is not registered.")