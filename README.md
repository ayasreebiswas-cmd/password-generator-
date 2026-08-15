# Custom Password Generator

A secure, configurable, and lightweight Python application designed to generate cryptographically random, customizable passwords based on user-defined length and character set preferences.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Usage Instructions](#-usage-instructions)
- [How It Works](#-how-it-works)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📖 Project Overview
Security and password complexity are fundamental aspects of digital identity protection. The **Custom Password Generator** is an interactive command-line tool written in Python that allows users to quickly create robust, highly secure passwords tailored to specific criteria (length, inclusion of uppercase letters, lowercase letters, numbers, and special symbols).

It ensures that at least one character from each selected category is included in the output before shuffling, avoiding weak or unpredictable generation patterns.

---

## ✨ Key Features
- **Customizable Length**: Users can specify the exact length of the password (minimum recommended length enforced: 6 characters).
- **Flexible Character Sets**: Toggle inclusion for:
  - Uppercase letters (`A-Z`)
  - Lowercase letters (`a-z`)
  - Numeric digits (`0-9`)
  - Special punctuation symbols (`!@#$%^&*...`)
- **Guaranteed Coverage**: Ensures at least one character from every selected category is explicitly included before final shuffling.
- **Randomization Security**: Uses Python's `random.shuffle()` to randomize character positions thoroughly.
- **Interactive CLI Interface**: Simple, user-friendly prompt system with default fallback values.

---

## 🛠️ Technologies Used
- **Language**: Python 3.x
- **Standard Libraries**:
  - `random`: For selection and shuffling.
  - `string`: For predefined character constants (`ascii_uppercase`, `ascii_lowercase`, `digits`, `punctuation`).

---

## 📂 Project Structure
