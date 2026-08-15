import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_nums=True, use_syms=True):
    chars = ""
    pwd = []

    if use_upper:
        chars += string.ascii_uppercase
        pwd.append(random.choice(string.ascii_uppercase))
    if use_lower:
        chars += string.ascii_lowercase
        pwd.append(random.choice(string.ascii_lowercase))
    if use_nums:
        chars += string.digits
        pwd.append(random.choice(string.digits))
    if use_syms:
        chars += string.punctuation
        pwd.append(random.choice(string.punctuation))

    if not chars:
        print("Error: You must select at least one character type.")
        return None


    for _ in range(length - len(pwd)):
        pwd.append(random.choice(chars))

    random.shuffle(pwd)
    return "".join(pwd)

def main():
    print("--- Password Generator ---")

    user_input = input("Enter password length (default 12): ").strip()
    if user_input.isdigit():
        length = max(6, int(user_input)) 
    else:
        length = 12

    print("\nInclude character types? (y/n)")
    use_upper = input("Uppercase? (Y/n): ").strip().lower() != 'n'
    use_lower = input("Lowercase? (Y/n): ").strip().lower() != 'n'
    use_nums = input("Numbers? (Y/n): ").strip().lower() != 'n'
    use_syms = input("Symbols? (Y/n): ").strip().lower() != 'n'

    pwd = generate_password(length, use_upper, use_lower, use_nums, use_syms)

    if pwd:
        print(f"\nGenerated Password: {pwd}")

if __name__ == "__main__":
    main()