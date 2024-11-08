import random
import string

def generate_pass(length):
    # Define the character sets to use for password generation
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters
    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    # Join the list into a string and return
    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4 characters.")
            else:
                password = generate_pass(length)
                print(f"Generated Password: {password}")

        except ValueError:
            print("Invalid input! Please enter a numeric value.")

        while True:
            continue_prompt = input("Enter either 1 to continue or 0 to exit: ")
            if continue_prompt == "0":
                print("                                             THANK YOU!")
                return  
            elif continue_prompt == "1":
                break  # Valid input, break out of the loop
            else:
                print("Please enter a valid number (1 to continue, 0 to exit).")

if __name__ == "__main__":
    main()