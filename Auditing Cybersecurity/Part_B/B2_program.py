def evaluate_password(password):
    # Boolean flag variables corresponding to each rule (criteria)
    booleanFlag1 = False  # Rule 1
    booleanFlag2 = False  # Rule 2
    booleanFlag3 = False  # Rule 3
    booleanFlag4 = False  # Rule 4
    booleanFlag5 = False  # Rule 5

    # Check for the length of the python string.
    if len(password) >= 12:
        booleanFlag1 = True

    # Loop through every character to check for an uppercase letter.
    i = 0
    for characters in password:
        if password[i].isupper():
            booleanFlag2 = True
            break
        i += 1

    # Loop through every character to check for a lowercase letter.
    j = 0
    for characters in password:
        if password[j].islower():
            booleanFlag3 = True
            break
        j += 1

    # Loop through every character to check for a number.
    x = 0
    for characters in password:
        if password[x].isnumeric():
            booleanFlag4 = True
            break
        x += 1

    # Verify that the password contains symbols by making sure it's not entirely characters and numbers.
    if password.isalnum() == False:
        booleanFlag5 = True
            
    # Evaluate the final result using logical AND between flags.
    if booleanFlag1 and booleanFlag2 and booleanFlag3 and booleanFlag4 and booleanFlag5:
        return "Compliant"
    else:
        non_compliant_message = "Non-compliant.\n The given password did not pass the following criteria:"
        if not booleanFlag1:
            non_compliant_message += "\n Password should have at least 12 characters."
        if not booleanFlag2:
            non_compliant_message += "\n Password should contain uppercase letters."
        if not booleanFlag3:
            non_compliant_message += "\n Password should contain lowercase letters."
        if not booleanFlag4:
            non_compliant_message += "\n Password should contain numbers."
        if not booleanFlag5:
            non_compliant_message += "\n Password should contain symbols."
        return non_compliant_message


# User input
password = input("Enter your password: ")
print(evaluate_password(password))
