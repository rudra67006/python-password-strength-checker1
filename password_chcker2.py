
password = input("Enter your password: ")

# Initialize all checks
has_length = len(password) >= 8
has_uppercase = False
has_lowercase = False
has_number = False
has_special = False

special_characters = "!@#$%^&*()-_+=<>?/[]{}"

# Check each character
for character in password:
    if character.isupper():
        has_uppercase = True

    if character.islower():
        has_lowercase = True

    if character.isdigit():
        has_number = True

    if character in special_characters:
        has_special = True

# Display overall password strength
if (has_length and has_uppercase and has_lowercase
        and has_number and has_special):
    print("\nPassword Strength: STRONG")
else:
    print("\nPassword Strength: WEAK")
    print("\nSuggestions to improve your password:")

    if not has_length:
        print("- Use at least 8 characters.")

    if not has_uppercase:
        print("- Add an uppercase letter (A-Z).")

    if not has_lowercase:
        print("- Add a lowercase letter (a-z).")

    if not has_number:
        print("- Add a number (0-9).")

    if not has_special:
        print("- Add a special character such as @, #, or !.")
