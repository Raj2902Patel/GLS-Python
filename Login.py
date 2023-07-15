import hashlib

# hashlib.sha256 is the function of hashlib
# database of users
users = {
    "raj": {
        "password": hashlib.sha256("raj123".encode()).hexdigest(),
        "role": "admin"
    },
    "parth": {
        "password": hashlib.sha256("parth123".encode()).hexdigest(),
        "role": "user"
    }
}

# Login function


def login():
    username = input("Username: ")
    password = hashlib.sha256(input("Password: ").encode()).hexdigest()

    if username in users and password == users[username]["password"]:
        print("Login successful!")
        return users[username]["role"]
    else:
        print("Invalid username or password.")
        return None

# Sign-up function


def sign_up():
    username = input("Choose a username: ")

    if username in users:
        print("Username already exists.")
        return False

    password = hashlib.sha256(
        input("Choose a password: ").encode()).hexdigest()

    users[username] = {
        "password": password,
        "role": "user"
    }

    print("Sign-up successful!")
    return True

# Main program


def main():
    while True:
        print("1. Login")
        print("2. Sign up")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            role = login()
            if role == "admin":
                print("Welcome, admin!")
            elif role == "user":
                print("Welcome, user!")
        elif choice == "2":
            sign_up()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()