import string  # Importing the string module for predefined character sets
import random  # Importing the random module to shuffle characters and generate randomness

def password_generator():
    # Ask the user to input the desired password length
    passlen = int(input("Enter the length of the password:-"))
    
    # Define character sets
    s1 = string.ascii_uppercase  # All uppercase letters (A-Z)
    s2 = string.ascii_lowercase  # All lowercase letters (a-z)
    s3 = string.digits           # All digits (0-9)
    s4 = string.punctuation      # All special characters (e.g., !, @, #, etc.)

    # Create an empty list to store all possible characters
    s = []
    
    # Add all character sets to the list
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)

    # Shuffle the characters to ensure randomness
    random.shuffle(s)

    # Generate the password by selecting the first 'passlen' characters from the shuffled list
    password = "".join(s[0:passlen])

    # Display the generated password
    print("Generated password :-" + password)

# Call the function to generate a password
password_generator()
