import random
import string #Import the pre-define module

class PasswordGenerator: #Define the class name
    def __init__(self):
        self.length = None

    def get_password_length(self): #This function define the length of password
        try:
            self.length = int(input("Enter the length of password:"))

            if self.length <= 0:
                print("Invalid input! Please enter a valid positive integer.")
                return False
            return True
        except ValueError:
            print("Invalid input! Please enter a valid positive integer.")
            return False
    
    def generate_password(self): #This function generate the random password
        if self.length is None:
            print("Password length not set. Please set the length first!")
            return
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(self.length))

        return password

def main():
    password_gen = PasswordGenerator() #Create a object of the function

    while True:
        if password_gen.get_password_length():
            password = password_gen.generate_password()
            print(f"Generated password: {password}")
            break

if __name__ == "__main__":
    main()