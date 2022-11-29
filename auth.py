from db_funcs import insert_into_db, select_from_db, insert_session_into_db, select_session_from_db, delete_session_from_db
from auth_funcs import set_current_logged_in_employee, get_current_logged_in_employee 
from models import Employee
import bcrypt
from getpass import getpass
import os


#DB_NAME=os.getenv("DB_NAME")
DB_NAME="company.db"


####################################################
#
#   Desc: Allows a user to login. Upon successful  
#         authentication a session is created.  
#
####################################################
def login():
    
    # Check if user is already logged in
    current_logged_in_employee = get_current_logged_in_employee()
    if current_logged_in_employee:
        print("You are currently logged in.")
        return 0

    
    # Obtain user's credentials 
    username = input("Please enter your username: ")
    password = getpass("Please enter your password: ")
    

    # Check if the user has an account 
    user = select_from_db(DB_NAME, username)
    if user == None:
        print("No account with username provided.")
        return 1
    
    # If the username is found in the DB   
    else:
        # Check the password supplied by the user matches the password in the DB
        if bcrypt.checkpw(password.encode(), user[4]):

            ###### Need to change the 'user_id'     
            #employee = Employee(id)

            # Check if a session already exists
            session = select_session_from_db(DB_NAME, user[0])
            if session:
                print("Employee already logged in.")
                return 3
            
            # If no session exists
            else:     
                # Add user to session
                insert_session_into_db(DB_NAME, user[0])
                
                # Create an 'Employee' object and fill it with the newly logged in user's data 
                current_logged_in_employee = Employee(firstname=user[1], lastname=user[2], username=user[3], password=user[4], salary=user[5])
                current_logged_in_employee.set_employee_id(user[0])

                # TODO - add this to the log file 
                # print(f"Session created for user: {current_logged_in_employee.username}.")     

                # Set the currently logged in user value by storing it in the pickle file
                set_current_logged_in_employee(current_logged_in_employee)    

                # Let the user know the login was successful.
                print("Successfully logged in.")
                
                return 0
        
        # If the password supplied by the user does not match the password in the DB
        else:
            print("Incorrect login credentials.")
            return 2


####################################################
#
#   Desc: Register a new user. 
#
#
####################################################
def register():

    # Check if a user is currently logged in 
    current_logged_in_employee = get_current_logged_in_employee()
    if current_logged_in_employee:
        print("You are currently logged in. Please log out to register.")
        return 0

    # if a user is not currently logged in
    else:
        # Get registration information
        firstname = input("Please enter your firstname: ")
        lastname = input("Please enter your lastname: ")
        username = input("Please enter your username: ")
        password_1 = getpass("Please enter your password: ")
        password_2 = getpass("Please enter your password again: ")

        # Check if this username already exists
        user = select_from_db(DB_NAME, username)
        if user:
            print("This username already exists.")
            return 1

        # Check if the two passwords match
        else: 
            if password_1 != password_2:
                print("Passwords do not match.")
                return 2

            # If the two passwords match
            else:
                # Hash the password that was supplied by the user
                hashed_password = bcrypt.hashpw(password_1.encode(), bcrypt.gensalt())
        
                # Create an 'Employee' object and fill it with the info provided by the user 
                employee = Employee(firstname, lastname, username, hashed_password, 20000)     
                
                # Insert the employee into the DB
                insert_into_db(DB_NAME, employee)
        
                # Obtain the user's id from the DB and update 'employee' object
                employee_with_id = select_from_db(DB_NAME, employee.username)
                employee.set_employee_id(employee_with_id[0])

                # TODO - insert this into a log file 
                # print(f"Employee id: {employee.get_employee_id()}")

                print("Registration successful. You can now log in.")

                return 0


####################################################
#
#   Desc: Log out a user
#
#
####################################################
def logout():
    
    # Check if the user is logged in 
    current_logged_in_employee = get_current_logged_in_employee()

    # If the user is not logged in
    if current_logged_in_employee == None:
        print("No user is logged in.")
        return 0
    
    # If the user is logged in
    else:      
        # Get the currently logged in employee's id
        current_logged_in_employee_id = current_logged_in_employee.get_employee_id()

        # Remove the employee's session from the session table  
        delete_session_from_db(DB_NAME, current_logged_in_employee_id)
        
        # Inform the user that the logout has been successful
        print("Employee successfully logged out.")

        # Remove the user from the .pkl file 
        current_logged_in_employee = set_current_logged_in_employee(None)

        return 0
    