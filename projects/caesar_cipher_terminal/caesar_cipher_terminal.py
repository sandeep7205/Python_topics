def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(cipher_text, key):
    return encrypt(cipher_text, -key)

def menu():
    while True:
        print("\n===== Caesar Cipher Tool =====")
        print("1. Encrypt a Message")
        print("2. Decrypt a Message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            text = input("Enter text to encrypt: ")
            key = int(input("Enter shift key (number): "))
            encrypted = encrypt(text, key)
            print(f"\n🔐 Encrypted Text: {encrypted}")

        elif choice == "2":
            cipher_text = input("Enter text to decrypt: ")
            key = int(input("Enter shift key (number): "))
            decrypted = decrypt(cipher_text, key)
            print(f"\n🔓 Decrypted Text: {decrypted}")

        elif choice == "3":
            print("👋 Exiting the program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

# Run the tool
menu()
