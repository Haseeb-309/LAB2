# login.py
import db.database as database

def login():
    print("=== Login ===")
    username = input("Username: ")
    password = input("Password: ")

    if database.validate_user(username, password):
        print("Login successful!")
        return username
    else:
        print("Invalid credentials.")
        return None

def register():
    print("=== Register ===")
    username = input("Username: ")
    password = input("Password: ")

    if database.add_user(username, password):
        print("User registered successfully!")
    else:
        print("Username already exists.")
