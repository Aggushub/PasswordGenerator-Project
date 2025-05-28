import string  # To use predefined character sets
import random  # To generate randomness

def gen():
    # Display the header
    print("\t\tPASSWORD GENERATOR\t\t")
    print("---------------------------------------------------")

    # Define character sets
    s1 = string.ascii_uppercase     # Uppercase letters A-Z
    s2 = string.ascii_lowercase     # Lowercase letters a-z
    s3 = string.digits              # Digits 0-9
    s4 = string.punctuation         # Special characters like !, @, #
    alls = s1 + s2 + s3 + s4        # Combine all character sets

    # Ensure user enters a valid password length
    while True:
        passlen = int(input("Enter the length of the password:-"))
        if passlen > 0:
            break
        else:
            print("❌ Invalid password length. Try again.")

    s = []  # Final character list for password

    while True:
        # Ask if the user wants a specific character format
        print("Do you have any specific format for your password (like 1 uppercase, 1 lowercase, 1 digit, 1 special character)?")
        con = input("Y/N:-")

        # If YES: Custom format
        if con.upper() in ["Y", "YES"]:
            lenpass = passlen  # Initialize the remaining length

            # Ask for number of uppercase letters
            while True:
                ul = int(input("Enter the number of uppercase letters ({} characters left):- ".format(lenpass)))
                if ul <= lenpass:
                    break
                else:
                    print("❌ Too many characters! Please enter a value ≤ {}".format(lenpass))
            lenpass -= ul

            # If length exactly filled with uppercase letters
            if lenpass == 0:
                password_part1 = random.sample(s1, ul)
                s.extend(password_part1)
                random.shuffle(s)
                password = ''.join(s)
                print("Your generated password with {} characters ({} uppercase letters) is {}".format(passlen, ul, password))
                break

            # Ask for lowercase letters
            while True:
                ll = int(input("Enter the number of lowercase letters ({} characters left):- ".format(lenpass)))
                if ll <= lenpass:
                    break
                else:
                    print("❌ Too many characters! Please enter a value ≤ {}".format(lenpass))
            lenpass -= ll

            if lenpass == 0:
                password_part1 = random.sample(s1, ul)
                password_part2 = random.sample(s2, ll)
                s.extend(password_part1 + password_part2)
                random.shuffle(s)
                password = ''.join(s)
                print("Your generated password with {} characters ({} uppercase, {} lowercase) is {}".format(passlen, ul, ll, password))
                break

            # Ask for digits
            while True:
                di = int(input("Enter the number of digits ({} characters left):- ".format(lenpass)))
                if di <= lenpass:
                    break
                else:
                    print("❌ Too many characters! Please enter a value ≤ {}".format(lenpass))
            lenpass -= di

            if lenpass == 0:
                password_part1 = random.sample(s1, ul)
                password_part2 = random.sample(s2, ll)
                password_part3 = random.sample(s3, di)
                s.extend(password_part1 + password_part2 + password_part3)
                random.shuffle(s)
                password = ''.join(s)
                print("Your generated password with {} characters ({} uppercase, {} lowercase, {} digits) is {}".format(passlen, ul, ll, di, password))
                break

            # Ask for special characters
            while True:
                sc = int(input("Enter the number of special characters ({} characters left):- ".format(lenpass)))
                if sc <= lenpass:
                    break
                else:
                    print("❌ Too many characters! Please enter a value ≤ {}".format(lenpass))
            lenpass -= sc

            # All characters filled exactly
            if lenpass == 0:
                password_part1 = random.sample(s1, ul)
                password_part2 = random.sample(s2, ll)
                password_part3 = random.sample(s3, di)
                password_part4 = random.sample(s4, sc)
                s.extend(password_part1 + password_part2 + password_part3 + password_part4)
                random.shuffle(s)
                password = ''.join(s)
                print("Your generated password with {} characters ({} uppercase, {} lowercase, {} digits, {} special characters) is {}".format(passlen, ul, ll, di, sc, password))
                break
            else:
                # Fill remaining characters with random from all sets
                remain = lenpass
                password_random = random.sample(alls, remain)
                password_part1 = random.sample(s1, ul)
                password_part2 = random.sample(s2, ll)
                password_part3 = random.sample(s3, di)
                password_part4 = random.sample(s4, sc)
                s.extend(password_random + password_part1 + password_part2 + password_part3 + password_part4)
                random.shuffle(s)
                password = ''.join(s)
                print("Your generated password with {} characters ({} uppercase, {} lowercase, {} digits, {} special characters, {} random characters) is {}".format(passlen, ul, ll, di, sc, remain, password))
                break

        # If NO: Random format
        elif con.upper() in ["N", "NO"]:
            s.extend(list(alls))
            random.shuffle(s)
            password = ''.join(s[:passlen])
            print("Your generated password with {} characters is {}".format(passlen, password))
            break

        # Invalid input
        else:
            print("Invalid choice. Please enter Y or N.")

# Run the password generator
gen()
