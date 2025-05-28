import string
import random

def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    alls = s1 + s2 + s3 + s4
    passlen = int(input("Enter the length of the password:-"))

    s = []
    print("Do you have any specific format for your password(like 1 uppercase, 1 lowercase, 1 digit, 1 special character)?- ")
    con = input(("Y/N:-"))
    if con.upper() == "Y":
        lenpass = passlen
        ul = int(input("Enter the number of uppercase letters:- ({} characters left)".format(lenpass)))
        if(lenpass>=ul):
            lenpass-=ul
            ll = int(input("Enter the number of lowercase letters:-({} characters left)".format(lenpass)))
        else:
            print("Password Character length exceeded")
        if(lenpass>=ll):
            lenpass-=ll
            di = int(input("Enter the number of digits:-({} characters left)".format(lenpass)))
        else:
            print("Password Character length exceeded")
        if(lenpass>=di):
            lenpass-=di
            sc = int(input("Enter the number of special characters:-({} characters left)".format(lenpass)))
            lenpass-=sc
        else:
            print("Password Character length exceeded")
        if(lenpass>0):
            remain = lenpass
            password_random = random.sample(alls,remain)
            s.extend(password_random)
        password_part1 = random.sample(s1,ul)
        password_part2 = random.sample(s2, ll)
        password_part3 = random.sample(s3, di)
        password_part4 = random.sample(s4, sc)
        s.extend(list(password_part1))
        s.extend(list(password_part2))
        s.extend(list(password_part3))
        s.extend(list(password_part4))
        random.shuffle(s)
        password = ''.join(s)
        print(password)

    elif con.upper()== "N":
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        random.shuffle(s)
        password =("".join(s[0:passlen]))
        print("Password Generated is "+password)
gen()