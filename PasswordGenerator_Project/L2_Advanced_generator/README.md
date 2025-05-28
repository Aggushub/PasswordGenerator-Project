# 🔐 Advanced Password Generator

This is a more **advanced password generator** written in Python that lets you customize the password structure to meet specific security requirements. You can specify the number of uppercase letters, lowercase letters, digits, and special characters in the password.

---

## 🧠 How It Works

- Prompts the user to enter the desired password length.
- Asks if you want to follow a specific format (e.g., number of uppercase, lowercase, digits, and symbols).
- Ensures that the sum of specified character types does not exceed the total length.
- If no format is chosen, it generates a fully random password.

---

## 🚀 Features

✅ Customizable password structure  
✅ Guarantees inclusion of specific character types  
✅ Fallback to default random generation if no format is selected  
✅ Good for learning input validation and character control in Python

---

## ▶️ How to Use

Run the script using Python 3:

```bash
python Password_gen_advanced.py
````

You’ll be prompted to:

1. Enter the total length of the password.
2. Choose whether to specify a format.
3. If yes, provide counts for:

   * Uppercase letters
   * Lowercase letters
   * Digits
   * Special characters

The program will build a password accordingly and display it.

---

## 💡 Example Output

Here’s how the script looks in action:

![Advanced Generator Screenshot](./Screenshot%20\(75\).png)

---

## 📂 Files

```
L2 Advanced_generator/
│
├── Password_gen_advanced.py     # Advanced generator script
└── Screenshot (75).png          # Example output screenshot
```

---

## 🛠 Requirements

* Python 3.x

---

## ⚠️ Notes

* If the specified counts exceed the total length, a warning is shown.
* No character type is guaranteed unless format mode is used.
* Meant for educational use and basic personal needs.

---

## 🤝 Contributing

Want to improve this tool? Fork the repo, add features (like saving to file or GUI support), and send a pull request!

---

Upgrade your password generation game with precision control! 🔐✨

```
