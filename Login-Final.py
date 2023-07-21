import hashlib

users = {}

def login():
    username = input("Enter Your Username:- ")
    if username not in users:
        print("---User Does Not Exist---")
    else:

        password = hashlib.sha256(input("Enter Your Password:- ").encode()).hexdigest()

        if username in users and password == users[username]['password']:
            print("-----Login Successfull-----")
    
        else:
            print("-----Invalid Username or Password-----")
            return None
    
def deluser():
    username = input("Enter Your Username:- ")
    password = hashlib.sha256(input("Enter Your Password:- ").encode()).hexdigest()

    if username in users and password == users[username]['password']:
        del users[username]
        print("-----Delete User Successfully-----")
    else:
        print("-----User Not Found-----")

def show1():
    if len(users) == 0:
        print("-----Dictionary is Empty-----")
    else:
        print("Dictionary is:- ",users)

def sign_up():
    username = input("Choose a username:- ")

    if username in users:
        print("-----Username already exists-----")
        return False
    
    password = hashlib.sha256(
        input("Choose a password:- ").encode()).hexdigest()

    users[username] = {
        "password":password
    }

    print("-----Sign-up Successfully-----")
    return True

def main():
    while True:
        print("1. Sign-up")
        print("2. Login")
        print("3. Show All Users")
        print("4. Delete")
        print("5. Quit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            role = login()
            if role == "admin":
                print("---Welcome---")
            elif role == "user":
                print("---Welcome---")
        elif choice == "3":
            show1()
        elif choice == "4":
            deluser()
        elif choice == "5":
            break
        else:
            print("-----Invalid Choice. Please Try Again-----")

if __name__ == "__main__":
    main()


        
