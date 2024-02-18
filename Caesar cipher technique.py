def caesar_cipher(message, shift, encrypt=True):
    result = ""

    for char in message:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Apply the shift to the character based on the alphabet
            char_code = ord(char) - ord('A' if is_upper else 'a')
            shifted_code = (char_code + shift) % 26 if encrypt else (char_code - shift) % 26
            new_char = chr(shifted_code + ord('A' if is_upper else 'a'))

            result += new_char
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Encryption/Decryption Application")

    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value for encryption: "))
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value for decryption: "))
            decrypted_message = caesar_cipher(message, shift, encrypt=False)
            print("Decrypted message:", decrypted_message)
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
