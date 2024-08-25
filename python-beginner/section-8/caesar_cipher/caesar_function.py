from caesar_data import alphabet


def encrypt_decrypt(user_choice: str, text: str, shift: int) -> str:
    text_list: list[str] = text.split()
    new_text: list[str] = []

    for word in text_list:
        new_word: str = ""
        for letter in word:
            if letter in alphabet:
                if user_choice == "encode":
                    # get the index number of the equivalent letter + shifts needed to make
                    new_letter: str = alphabet[
                        (alphabet.index(letter) + shift) % len(alphabet)
                    ]
                    new_word += new_letter
                elif user_choice == "decode":
                    new_letter = alphabet[
                        (alphabet.index(letter) - shift) % len(alphabet)
                    ]
                    new_word += new_letter
            else:
                new_word += letter
        new_text.append(new_word)

    final_text = " ".join(new_text)  # turn back into string
    if user_choice == "encode":
        return f"Encrypted message: {final_text}"
    elif user_choice == "decode":
        return f"Decrypted message: {final_text}"
