from cryptography.fernet import Fernet

# ---------- KEY HANDLING ----------
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

# Generate key if not exists
import os
if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)

# ---------- FUNCTIONS ----------
def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("|")
            decrypted_pass = fer.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_pass)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        encrypted_pass = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_pass + "\n")

# ---------- MAIN LOOP ----------
while True:
    mode = input("Would you like to add a new password or view existing ones (view/add) or press q to quit? ").strip().lower()
    
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Not a valid option!")
