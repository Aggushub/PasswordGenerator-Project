import string
import random

def gen():
    print("\t\tPASSWORD GENERATOR\t\t")
    print("---------------------------------------------------")
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    alls = s1 + s2 + s3 + s4
    while True:
        passlen = int(input("Enter the length of the password:-"))
        if passlen >0:
            break
        else:
            print("❌Invalid password length.Try again")
    s = []
    while True:
        print("Do you have any specific format for your password(like 1 uppercase, 1 lowercase, 1 digit, 1 special character)?- ")
        con = input(("Y/N:-"))
        if con.upper() == "Y" or con.upper() == "YES":
            lenpass = passlen
            while True:
                ul = int(input("Enter the number of uppercase letters ({} characters left):- ".format(lenpass)))
                if ul <= lenpass:
                    break
                else:
                    print("❌ Too many characters! Please enter a value less than or equal to {}.".format(lenpass))

            lenpass-=ul
            if lenpass == 0:
                print("Password length completed")
                password_part1 = random.sample(s1,ul)
                s.extend(list(password_part1))
                random.shuffle(s)
                password = ''.join(s)
                print("Your generated password with {} characters({} uppercase letters) is {}".format(passlen,ul,password))
                break
            else:
                while True:
                    ll = int(input("Enter the number of lowercase letters ({} characters left):-".format(lenpass)))
                    if ll <= lenpass:
                        break
                    else:
                        print("❌ Too many characters! Please enter a value less than or equal to {}.".format(lenpass))
                lenpass-=ll
                if lenpass == 0:
                    print("Password length completed")
                    password_part1 = random.sample(s1,ul)
                    password_part2 = random.sample(s2, ll)
                    s.extend(list(password_part1))
                    s.extend(list(password_part2))
                    random.shuffle(s)
                    password = ''.join(s)
                    print("Your generated password with {} characters({} uppercase letters & {} lowercase letters) is {}".format(passlen,ul,ll,password))
                    break
                else:
                    while True:
                        di = int(input("Enter the number of digits ({} characters left):-".format(lenpass)))
                        if(di<=lenpass):
                            break
                        else:
                            print("❌ Too many characters! Please enter a value less than or equal to {}.".format(lenpass))
                    lenpass-=di
                    if(lenpass == 0):
                        print("Password length completed")
                        password_part1 = random.sample(s1,ul)
                        password_part2 = random.sample(s2, ll)
                        password_part3 = random.sample(s3, di)
                        s.extend(list(password_part1))
                        s.extend(list(password_part2))
                        s.extend(list(password_part3))
                        random.shuffle(s)
                        password = ''.join(s)
                        print("Your generated password with {} characters({} uppercase letters, {} lowercase letters & {} digits) is {}".format(passlen,ul,ll,di,password))
                        break

                    else:
                        while True:
                            sc = int(input("Enter the number of special characters ({} characters left):-".format(lenpass)))
                            if(sc<=passlen):
                                break
                            else:
                                print("❌ Too many characters! Please enter a value less than or equal to {}.".format(lenpass))
                        lenpass-=sc
                        if (lenpass == 0):
                            print("Password length completed")
                            password_part1 = random.sample(s1, ul)
                            password_part2 = random.sample(s2, ll)
                            password_part3 = random.sample(s3, di)
                            password_part4 = random.sample(s4, sc)
                            s.extend(list(password_part1))
                            s.extend(list(password_part2))
                            s.extend(list(password_part3))
                            s.extend(list(password_part4))
                            random.shuffle(s)
                            password = ''.join(s)
                            print("Your generated password with {} characters({} uppercase letters, {} lowercase letters, {} digits & {} special characters) is {}".format(passlen, ul, ll, di, sc, password))
                            break
                        else:
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
                            print("Your generated password with {} charcters({} uppercase letters, {} lowercase letters, {} digits, {} special characters and {} random characters) is {}".format(passlen, ul, ll, di, sc, remain, password))
                            break

        elif con.upper()== "N" or con.upper()=="NO":
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            random.shuffle(s)
            password =("".join(s[0:passlen]))
            print("Your generated password with {} characters is {}".format(passlen,password))
            break
        else: 
            print("Invalid choice. Please enter Y or N.")
        
gen()