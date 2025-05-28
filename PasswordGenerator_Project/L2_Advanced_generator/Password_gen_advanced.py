import string  # Import string module for ready-made character sets
import random  # Import random module for shuffling and sampling

def gen():
    # Define character sets
    s1 = string.ascii_uppercase     # Uppercase letters A-Z
    s2 = string.ascii_lowercase     # Lowercase letters a-z
    s3 = string.digits              # Digits 0-9
    s4 = string.punctuation         # Special characters

    # Combine all characters into one string
    alls = s1 + s2 + s3 + s4

    # Ask user for the desired password length
    passlen = int(input("Enter the length of the password:-"))

    # Initialize the list to store selected characters
    s = []

    # Ask user if they want a specific password format
    print("Do you have any specific format for your password (like 1 uppercase, 1 lowercase, 1 digit, 1 special character)?- ")
    con = input("Y/N:-")

    if con.upper() == "Y":
        # Initialize length tracker
        lenpass = passlen

        # Collect number of uppercase letters
        ul = int(input("Enter the number of uppercase letters:- ({} characters left)".format(lenpass)))
        if lenpass >= ul:
            lenpass -= ul
            # Collect number of lowercase letters
            ll = int(input("Enter the number of lowercase letters:-({} characters left)".format(lenpass)))
        else:
            print("Password Character length exceeded")

        if lenpass >= ll:
            lenpass -= ll
            # Collect number of digits
            di = int(input("Enter the number of digits:-({} characters left)".format(lenpass)))
        else:
            print("Password Character length exceeded")

        if lenpass >= di:
            lenpass -= di
            # Collect number of special characters
            sc = int(input("Enter the number of special characters:-({} characters left)".format(lenpass)))
            lenpass -= sc
        else:
            print("Password Character length exceeded")

        # If some characters are still remaining, fill with random characters
        if lenpass > 0:
            remain = lenpass
            password_random = random.sample(alls, remain)
            s.extend(password_random)

        # Add required characters from each category
        password_part1 = random.sample(s1, ul)
        password_part2 = random.sample(s2, ll)
        password_part3 = random.sample(s3, di)
        password_part4 = random.sample(s4, sc)

        # Combine all parts
        s.extend(password_part1)
        s.extend(password_part2)
        s.extend(password_part3)
        s.extend(password_part4)

        # Shuffle the final list to mix the characters
        random.shuffle(s)

        # Convert list to string and display
        password = ''.join(s)
        print(password)

    elif con.upper() == "N":
        # If no specific format, just shuffle all characters and pick from the combined list
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        random.shuffle(s)
        password = "".join(s[0:passlen])
        print("Password Generated is " + password)

# Call the password generator function
gen()
