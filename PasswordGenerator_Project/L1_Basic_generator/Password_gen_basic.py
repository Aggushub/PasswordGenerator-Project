import string
import random

def password_generator():
    passlen = int(input("Enter the length of the password:-"))
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    s =[]
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    password = "".join(s[0:passlen])
    print("Generated password :-"+password)

password_generator()