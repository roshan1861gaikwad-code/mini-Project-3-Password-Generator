import string
import secrets

print("=== Password Generator ===")

try:
    length = int(input("Enter password length (minimum 4): "))

    if length < 4:
        print("Error: Password length must be at least 4.")

    else:
        # Generate at least one character from each category
        password_chars = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.digits),
            secrets.choice(string.punctuation)
        ]

        # All available character types
        all_chars = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        # Generate the remaining characters
        for i in range(length - 4):
            password_chars.append(secrets.choice(all_chars))

        # Shuffle the characters into a random order
        secrets.SystemRandom().shuffle(password_chars)

        # Convert the list into a single string
        password = "".join(password_chars)

        print("Generated Password:", password)

except ValueError:
    print("Error: Please enter a valid whole number.")

    print("THANKYOU FOR GENERATING PASSWORD")
