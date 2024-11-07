allowed_entries = 5
entries = 0 #initial entries
while entries < allowed_entries: 
    password_entry = int(input("Enter your password: "))
    correct_password = 12345 
    if password_entry == correct_password: 
        print("Entered password is correct") 
        break #breaking the while loop if user entry is correct
    else:
        entries +=1 # reiterating if the user entry is incorrect
        remaining_entries = allowed_entries - entries #subtracting the attempts from the remaining allowed entries
        print(f"Invalid password! You have {remaining_entries} attempts left.")
if allowed_entries == entries: 
   print("Maximum attempts reached. Authorities have been alerted!")