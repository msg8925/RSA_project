from db_funcs import open_db, insert_key_into_db
from auth import login, register, logout 
from tasks import some_secure_function 
import os
from rsa import rsa_generate_key
from key_classes import Keys
from key_funcs import write_to_file 
from auth_funcs import get_current_logged_in_employee


NUMBER_OF_BITS = 8

if __name__=="__main__":

    # Get DB info from dotenv file 
    #DB_NAME=os.getenv("DB_NAME")
    DB_NAME="company.db"
    print(DB_NAME)
    
    # Setup DB
    open_db(DB_NAME)

    while True:

        # Clear terminal
        os.system("cls")

        print("""

            1. Login
            2. Logout
            3. Register
            4. Execute task
            5. Generate keys
            9. Exit

        Please enter your option:

        """)
        user_input = input(">>: ")

        if user_input == '1':
            login()
            user_input = input("Press any key to continue... ")

        elif user_input == '2':
            logout()
            user_input = input("Press any key to continue... ")

        elif user_input == '3':
            register()
            user_input = input("Press any key to continue... ")

        elif user_input == '4': 
            # This function will prompt user for login information before running
            some_secure_function()
            user_input = input("Press any key to continue... ")


        # Generate keys
        elif user_input == '5': 

            # Generate the public and private keys            
            keys = rsa_generate_key(NUMBER_OF_BITS)

            print(f"Keys={keys}")

            public_key = [keys[0], keys[2]]
            private_key = [keys[1], keys[2]]

            # Get currently logged in employee to extract id 
            current_logged_in_employee = get_current_logged_in_employee()

            # Create a 'keys' object and fill it with public and private key data 
            keys = Keys(public_key=str(public_key), private_key=str(private_key), employee_id=current_logged_in_employee.id)

            # Store the keys in the DB
            insert_key_into_db(DB_NAME, keys)  

            # Export the public key
            write_to_file("public_key.txt", public_key)

            # Export the private key
            write_to_file("private_key.txt", private_key)

            user_input = input("Press any key to continue... ")


        elif user_input == '9':
            print("Exiting...")
            exit()

        else:
            print("Invalid option selected.")
            user_input = input("Press any key to continue... ")
