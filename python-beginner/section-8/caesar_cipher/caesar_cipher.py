from caesar_data import logo
from caesar_functions import encrypt_decrypt


def main():
    print(logo)

    user_choice = str(
        input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    )

    if user_choice == "encode" or user_choice == "decode":
        user_text = str(input(f"Type your message to be {user_choice}d: ").lower())
        shift_number = int(input("Type the shift number: "))
        print(encrypt_decrypt(user_choice, user_text, shift_number))
    else:
        print("Option not found.")


main()
