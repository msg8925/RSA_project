from db_funcs import open_db, insert_key_into_db, select_key_from_db
from auth import login, register, logout 
from tasks import some_secure_function 
import os
from rsa import rsa_generate_key, rsa_encrypt, rsa_decrypt
from key_classes import Keys
from key_funcs import write_to_file, create_file 
from auth_funcs import get_current_logged_in_employee 
from pickle_it import pickle_object, unpickle_string

NUMBER_OF_BITS = 8

string_encrypted_message = []
ampersand_embedded_message = []
original_msg = []

if __name__=="__main__":

    # Get DB info from dotenv file 
    #DB_NAME=os.getenv("DB_NAME")
    DB_NAME="company.db"
    print(DB_NAME)
    
    # Setup DB
    open_db(DB_NAME)

    # Create login file
    create_file()

    while True:

        # Clear terminal
        os.system("cls")

        print("""

            1. Login
            2. Logout
            3. Register
            4. Execute task
            5. Generate keys
            6. Encrypt message
            7. Decrypt message
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
            keys = Keys(public_key=pickle_object(public_key), private_key=pickle_object(private_key), employee_id=current_logged_in_employee.id)

            # Store the keys in the DB
            insert_key_into_db(DB_NAME, keys)  

            # Export the public key
            write_to_file("public_key.txt", public_key)

            # Export the private key
            write_to_file("private_key.txt", private_key)

            user_input = input("Press any key to continue... ")


        # Encrypt a message
        elif user_input == '6':
            
            # Get currently logged in user      
            current_logged_in_employee = get_current_logged_in_employee()

            # Retrieve key from DB
            keys = select_key_from_db(DB_NAME, current_logged_in_employee.id)

            print(f"key: {keys}")
            #print(f"public key: {}")

            public_key = unpickle_string(keys[1])
            print(f"Public key: {public_key}")

            e = public_key[0]
            n = public_key[1]

            print(f"e = {e}")
            print(f"n = {n}")


            ################################################################

            c = []

            # Convert char to ascii value
            #user_char = input("Please enter a char: ")
            user_string = input("Please enter the string you want to encrypt: ")
            user_string.split() 
            #print(f"user_string = {user_string}")

            for msg in user_string: 
                msg = ord(msg)
                #print(f"msg = {msg}")
                
                c.append(rsa_encrypt(msg, e, n))


            index = 0
            for msg_element in c:
                string_encrypted_message.append(str(c[index])) 
                index = index + 1

            #print(f"string_encrypted_message = {string_encrypted_message}") 

            # Insert symbol '&' to allow dectection of word boundaries    
            
            for msg_item in string_encrypted_message:
                ampersand_embedded_message.append(msg_item + '&')
    

            #print(f"ampersand embedded message = {ampersand_embedded_message}")

            #  # Join the string version
            ampersand_embedded_message = "".join(ampersand_embedded_message)
            # joined_encrypted_message = "".join(string_encrypted_message)

            print(f"""Encrypted message: 
            
                {ampersand_embedded_message}
                        
            """)
        
          
            ################################################################

            print("\n")
            user_input = input("Press any key to continue... ")


        # Decrypt a message
        elif user_input == '7':
            
            # Get currently logged in user      
            current_logged_in_employee = get_current_logged_in_employee()

            # Retrieve key from DB
            keys = select_key_from_db(DB_NAME, current_logged_in_employee.id)

            print(f"key: {keys}")
            #print(f"public key: {}")

            # Unpickle the private key
            private_key = unpickle_string(keys[2])
            print(f"Private key: {private_key}")

            # Extract the 'd' and 'n' values from the private key
            d = private_key[0]
            n = private_key[1]

            print(f"d = {d}")
            print(f"n = {n}")


            #################################################################
             
            c = []

            c = input("Please enter the message you want to decrypt: ")

            # Separate the message into a list 
            c = c.split('&')

            # Remove the final empty index     
            c.pop()

            #print(f"c.split('&') = {c}")  

            # d = private_key[0]
        
            for original_char in c:
                original_msg.append(chr(rsa_decrypt(int(original_char), d, n)))


            original_text = "".join(original_msg)    
            print(f"original message = {original_text}")   

             
            #################################################################     


            print("\n")
            input("Press any key to continue...")


        elif user_input == '9':
            print("Exiting...")
            exit()

        else:
            print("Invalid option selected.")
            user_input = input("Press any key to continue... ")
