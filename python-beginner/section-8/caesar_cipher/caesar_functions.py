from caesar_data import alphabet


def encrypt_decrypt(user_choice: str, text: str, shift: int) -> str:
    text_list = text.split()
    new_text = []

    # print(f"innitial text: {text}")  # output "text"
    # print(f"innitial text list: {text_list}")  # output [text, ]

    for word in text_list:
        new_word = ""
        for letter in word:
            if letter in alphabet:
                if user_choice == "encode":
                    # get the index number of the equivalent letter + shifts needed to make
                    new_letter = alphabet[(alphabet).index(letter) + shift]
                    new_word += new_letter
                elif user_choice == "decode":
                    new_letter = alphabet[(alphabet).index(letter) - shift]
                    new_word += new_letter
            else:
                new_word += letter
        new_text.append(new_word)
        # print(f"encrypted: {new_word}")
        # print(f"new text: {new_text}")

    final_text = " ".join(new_text)  # turn back into string
    if user_choice == "encode":
        return f"Encrypted message: {final_text}"
    elif user_choice == "decode":
        return f"Decrypted message: {final_text}"
