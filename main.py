from db_funcs import open_db, insert_key_into_db, select_key_from_db
from auth import login, register, logout 
from tasks import some_secure_function 
import os
from rsa import rsa_generate_key, rsa_encrypt, rsa_decrypt
from key_classes import Keys
from key_funcs import write_to_file, create_file 
from auth_funcs import get_current_logged_in_employee 
from pickle_it import pickle_object, unpickle_string
import random
import re

NUMBER_OF_BITS = 8

string_encrypted_message = []
ampersand_embedded_message = []
original_msg = []
separators = ["!", "@", "#", "^"] 

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
            
            c = []

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

       
            # Convert char to ascii value
            #user_char = input("Please enter a char: ")
            user_string = input("Please enter the string you want to encrypt: ")
            user_string.split() 
            #print(f"user_string = {user_string}")

            # Encryption process 
            for msg in user_string: 
                # Convert each ASCII character into its equivalent number 
                msg = ord(msg)
                
                # Append each value in encrypted form into an empty list called 'c' 
                c.append(rsa_encrypt(msg, e, n))


            # Convert each value into a string type 
            index = 0
            for msg_element in c:
                string_encrypted_message.append(str(c[index])) 
                index = index + 1

            
            # Insert symbol '&' to allow dectection of word boundaries     
            for msg_item in string_encrypted_message:

                random_value = random.randint(0, (len(separators) - 1))
                ampersand_embedded_message.append(msg_item + separators[random_value])
    
   
            # Make the encryted list into a single continuous string   
            ampersand_embedded_message = "".join(ampersand_embedded_message)
            
            # Print the encrypted message for the user to see
            print(f"""Encrypted message: 
            
                {ampersand_embedded_message}
                        
            """)


            print("\n")
            user_input = input("Press any key to continue... ")


        # Decrypt a message
        elif user_input == '7':
            
            c = []    

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
            

            c = input("Please enter the message you want to decrypt: ")

            # Separate the message into a list 
            # n = 0
            # for index in c:
            #     c = c.split(separators[n])
            #     n = n + 1

            c = re.split('\!|@|#|\^', c)
            # c = c.split('@')
            # c = c.split('#')
            # c = c.split('$')

            print(f"c = {c}")

            # Remove the final empty index     
            c.pop()
            c.pop()
            
            # Decryption process        
            for original_char in c:
                # Decrypt the message and place it in a list called 'original message'
                original_msg.append(chr(rsa_decrypt(int(original_char), d, n)))


            # Join the list into a sinle string
            original_text = "".join(original_msg)

            # Print the unencrypted message    
            print(f"original message = {original_text}")   


            print("\n")
            input("Press any key to continue...")


        elif user_input == '9':
            print("Exiting...")
            exit()

        else:
            print("Invalid option selected.")
            user_input = input("Press any key to continue... ")
