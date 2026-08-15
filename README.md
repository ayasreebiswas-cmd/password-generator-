# Customizable Python Password Generator

A lightweight, interactive Python tool designed to generate strong, customizable, and secure passwords. 

## Features

- **Custom Length**: Specify your desired password length (minimum length of 6 characters enforced).
- **Character Selection**: Choose whether to include:
  - Uppercase letters (`A-Z`)
  - Lowercase letters (`a-z`)
  - Numeric digits (`0-9`)
  - Special characters/symbols (`!@#$%^&*()`, etc.)
- **Guaranteed Coverage**: Ensures at least one character from each selected category is included in the generated password.
- **Randomized Order**: Shuffles the final list of characters to prevent predictable pattern placement.

---

## Requirements

- **Python 3.x**: Uses standard built-in modules (`random`, `string`). No external dependencies or `pip install` required.

---

## Usage

### 1. Run the Interactive CLI Tool

Execute the script directly from your terminal:

```bash
python password_generator.py
