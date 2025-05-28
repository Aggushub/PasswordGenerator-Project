# 🔐 Ultimate Password Generator (L3)

This is the most **advanced and flexible password generator** in the series, written in Python. It allows full control over the structure of the generated password, including strict customization of character types and robust input validation.

---

## 🌟 Key Features

- Set password length with input validation
  - If password length is found to be 0 or negative, it asks again for the length
- Now you can type yes instead of 'y' and No instead of 'n'
- Choose to customize the structure:
  - Number of **uppercase**, **lowercase**, **digits**, and **special characters**
- Automatically fills remaining characters with random mix if needed
- Prevents over-allocation of characters
- Friendly prompts and error messages
- Terminal output with clear formatting

---

## 🧠 How It Works

1. Prompts user to enter the total password length (must be > 0).
2. Asks if you want to customize the format.
3. If **Yes**, lets you:
   - Allocate specific number of character types.
   - Prevents character count overflow.
4. If **No**, it generates a random password using all character types.

---

## ▶️ How to Run

```bash
python Password_gen_ult.py
````

You’ll be prompted interactively in the terminal.

---

## 💡 Example Output

Here’s a screenshot of the generator in action:

![Ultimate Password Generator Screenshot](./Screenshot%20\(76\).png)

---

## 📂 Project Files

```
L3 Ultimate_Generator/
│
├── Password_gen_ult.py           # The ultimate password generator script
└── Screenshot (76).png           # Example output screenshot
```

---

## 🛠 Requirements

* Python 3.x

---

## ⚠️ Notes

* Ensure total password length covers all character specifications.
* Random characters are added if there’s space left after custom allocation.
* Fully interactive; no external libraries required.

---

## 🤝 Contributing

Want to improve this tool? Add CLI flags, file-saving, or GUI support — then submit a pull request!

---

Make your passwords smarter, stronger, and fully under your control 🔐🚀

```