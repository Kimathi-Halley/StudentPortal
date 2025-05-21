def welcome():
    print("Welcome to the Student Portal!")

def login():
    username = input("Enter your name: ")
    print(f"Welcome, {username}!")

def about():
    print("About: This is a basic student portal system used for demonstrating software development and version control with Git.")

if __name__ == "__main__":
    welcome()
    login()
    about()
