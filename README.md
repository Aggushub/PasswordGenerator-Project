# 🔐 PasswordGenerator_Project

This repository contains a **progressive series of password generators** written in Python, increasing in complexity and customization:

1. **L1 Basic Generator**
2. **L2 Advanced Generator**
3. **L3 Ultimate Generator**

Each level adds features and flexibility, allowing you to choose the right tool based on your password generation needs.

---

## 📁 Directory Structure

```

PasswordGenerator\_Project/
│
├── L1\_Basic\_generator/
│   ├── Password\_gen\_basic.py
│   └── Screenshot (72).png
│
├── L2\_Advanced\_generator/
│   ├── Password\_gen\_advanced.py
│   └── Screenshot (75).png
│
├── L3\_Ultimate\_Generator/
│   ├── Password\_gen\_ult.py
│   └── Screenshot (76).png
│
└── README.md  # This file

````

---

## 📊 Comparison Overview

| Feature                              | Basic (L1) | Advanced (L2) | Ultimate (L3) |
|--------------------------------------|------------|---------------|----------------|
| Generate password by length only     | ✅         | ✅            | ✅             |
| Uses uppercase, lowercase, digits, symbols | ✅    | ✅            | ✅             |
| Specify number of each character type | ❌         | ✅            | ✅             |
| Prevents over-allocation of characters | ❌        | ⚠️ Partial     | ✅ Robust       |
| Handles invalid input gracefully     | ❌         | ⚠️ Partial     | ✅             |
| Fills remaining characters randomly  | ❌         | ✅            | ✅             |
| Clean formatted output               | ❌         | ✅            | ✅ Enhanced    |

---

## 🧩 L1: Basic Password Generator

A beginner-friendly script that generates a random password using all types of characters, based solely on user-defined length.

### ✅ Features

- Simple and fast
- Uses uppercase, lowercase, digits, and punctuation
- No input validation

### ▶️ Run

```bash
cd L1_Basic_generator
python Password_gen_basic.py
````

### 💡 Example Output

![L1 Screenshot](./Screenshot%20\(72\).png)
---

## 🛠 L2: Advanced Password Generator

Adds the ability to specify how many characters of each type should be included in the password.

### ✅ Features

* Control over character counts (uppercase, lowercase, digits, symbols)
* Automatically fills leftover characters randomly
* Warns if specified characters exceed total length

### ▶️ Run

```bash
cd L2_Advanced_generator
python Password_gen_advanced.py
```

### 💡 Example Output

![L2 Screenshot](./Screenshot%20\(75\).png)

---

## 💼 L3: Ultimate Password Generator

A full-fledged, interactive password builder with precise control and validation. Prevents all user errors like character overflow and ensures robust password construction.

### ✅ Features

* Strict input validation with retry prompts
* Dynamic handling of each step
* Option to include only selected types
* Clear breakdown of generated password components

### ▶️ Run

```bash
cd L3_Ultimate_Generator
python Password_gen_ult.py
```

### 💡 Example Output

![L3 Screenshot](./Screenshot%20\(76\).png)

---

## 🧪 Requirements

* Python 3.x

No external libraries are required.

---

## 🤝 Contributing

Have an idea to improve the generators? Feel free to fork, enhance, and submit a pull request!

---

## 🚀 Final Thoughts

This project demonstrates how to progressively enhance a Python script from a basic tool to a powerful, user-friendly utility. Whether you're a beginner or looking to refine your Python skills with user input and randomization, this repo is a great starting point.

---
