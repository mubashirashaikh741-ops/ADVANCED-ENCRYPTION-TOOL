from cryptography.fernet import Fernet
import os

# ==============================
# GENERATE & SAVE ENCRYPTION KEY
# ==============================
def generate_key():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("\n[+] Encryption key generated and saved as secret.key")


# ==============================
# LOAD EXISTING KEY
# ==============================
def load_key():
    return open("secret.key", "rb").read()


# ==============================
# ENCRYPT FILE
# ==============================
def encrypt_file(filename, key):
    fernet = Fernet(key)

    try:
        with open(filename, "rb") as file:
            original_data = file.read()

        encrypted_data = fernet.encrypt(original_data)

        encrypted_filename = filename + ".encrypted"

        with open(encrypted_filename, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        print(f"\n[+] File encrypted successfully: {encrypted_filename}")

    except:
        print("\n[-] Error encrypting file")


# ==============================
# DECRYPT FILE
# ==============================
def decrypt_file(filename, key):
    fernet = Fernet(key)

    try:
        with open(filename, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        decrypted_filename = filename.replace(".encrypted", ".decrypted")

        with open(decrypted_filename, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)

        print(f"\n[+] File decrypted successfully: {decrypted_filename}")

    except:
        print("\n[-] Error decrypting file or invalid key")


# ==============================
# MAIN MENU
# ==============================
while True:

    print("\n===== ADVANCED ENCRYPTION TOOL =====")
    print("1. Generate Encryption Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    # Generate key
    if choice == "1":
        generate_key()

    # Encrypt file
    elif choice == "2":

        if not os.path.exists("secret.key"):
            print("\n[-] Generate key first!")
            continue

        key = load_key()

        filename = input("Enter file name to encrypt: ")

        if os.path.exists(filename):
            encrypt_file(filename, key)
        else:
            print("\n[-] File not found")

    # Decrypt file
    elif choice == "3":

        if not os.path.exists("secret.key"):
            print("\n[-] Generate key first!")
            continue

        key = load_key()

        filename = input("Enter encrypted file name: ")

        if os.path.exists(filename):
            decrypt_file(filename, key)
        else:
            print("\n[-] File not found")

    # Exit
    elif choice == "4":
        print("\nExiting Program...")
        break

    else:
        print("\n[-] Invalid Choice")