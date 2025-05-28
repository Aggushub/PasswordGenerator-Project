# 🔐 Basic Password Generator

This is a **very basic password generator** written in Python. It generates a random password based on the length input by the user. The password includes a mix of uppercase letters, lowercase letters, digits, and punctuation characters.

## 🚀 Features

- Takes user input for desired password length
- Generates a random password using:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special characters (punctuation)

## 🧠 How It Works

The script does the following:
1. Prompts the user to enter the desired password length.
2. Combines uppercase letters, lowercase letters, digits, and special characters into a single list.
3. Shuffles the list and selects characters up to the requested length.
4. Prints the generated password.

## 📝 Usage

Run the script using Python:

```bash
python Password_gen_basic.py
````

Then enter the length of the password you want when prompted.

---

## 🖼️ Example Output

Below is a screenshot of the script in action:

![Password Generator Example](./Screenshot%20\(72\).png)

---

## ⚠️ Note

* This is a **very basic implementation** intended for learning purposes.
* No validation is performed on the input. Negative or non-integer inputs may raise errors.
* Does not guarantee the inclusion of at least one character from each character set.

## 📂 File Structure

```
PasswordGenerator_Project/
│
├── Password_gen_basic.py       # Main password generator script
├── Screenshot (72).png         # Screenshot of the output
└── README.md                   # This file
```

## 🛠 Requirements

* Python 3.x

## 📬 Contributing

Feel free to fork the repo and submit a pull request if you’d like to enhance the functionality or add features!

---
