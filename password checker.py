import string

print(" Welcome to the Password Strength Checker")

while True:
    paw = input("Enter your password (or type 'exit' to quit): ")

    if paw.lower() == "exit":
        print("Exiting the process.")
        break

    length = len(paw)
    has_upper = False
    has_lower = False
    has_digit = False
    has_spc = False

    for char in paw:
        if char in string.ascii_uppercase:
            has_upper = True
        elif char in string.ascii_lowercase:
            has_lower = True
        elif char in string.digits:
            has_digit = True
        elif char in string.punctuation:
            has_spc = True

    if length < 6:
        print("Minimum 6 characters required.")
    elif not has_upper or not has_lower:
        print("Include both uppercase and lowercase letters.")
    elif not has_digit:
        print("Include at least one number.")
    elif not has_spc:
        print("Include at least one special character (!,@,#, etc.).")
    else:
        print("Strong password!")

    print("-" * 40)
