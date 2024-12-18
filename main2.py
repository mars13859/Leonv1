from password_generator import generate_password

from password_utils import check_password_strength, generate_multiple_passwords, save_passwords_to_file


def main():
    print("Welcome to the Enhanced Password Generator!")

    length = int(input("Enter the desired password length (minimum 1): "))

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

    use_digits = input("Include digits? (y/n): ").lower() == 'y'

    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    exclude_chars = input("Enter characters to exclude (leave blank for none): ")

    count = int(input("How many passwords would you like to generate? "))

    try:

        passwords = generate_multiple_passwords(count, length, use_uppercase, use_lowercase, use_digits, use_special,
                                                exclude_chars)

        for password in passwords:
            strength = check_password_strength(password)

            print(f"Generated Password: {password} (Strength: {strength})")

        save_to_file = input("Would you like to save these passwords to a file? (y/n): ").lower() == 'y'

        if save_to_file:
            save_passwords_to_file(passwords)



    except ValueError as e:

        print(e)


if __name__ == "__main__":
    main()