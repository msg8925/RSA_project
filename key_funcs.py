from file_context_manager import Open_file
from pickle_it import pickle_object, unpickle_string
import os
from models import Employee

####################################################
#
#   Desc: Create the inital file when program begins
#
#
####################################################
def create_file():

    filename = "auth_vars.pkl"
    mode = "wb"

    # Set the inital logged in user data to None
    initial_data = Employee(firstname=None, lastname=None, username=None, password=None, salary=None) 
    initial_data.set_employee_id = None

    # Check if the file already exists
    isExists = os.path.exists(filename)

    # If the file already exits
    if isExists:
        # return without creating new file
        return 0

    # If no file exists 
    else:
        # Create file
        f = open(filename, mode)

        # Pickle the list object
        pickled_data = pickle_object(initial_data)
        
        # Write data to the file
        f.write(pickled_data)

        # Close the file
        f.close()

        return 0


####################################################
#
#   Desc: # Read a key from a file
#
#
####################################################
def read_from_file(filename):
    
     # Read in binary form
    mode = "rb"

    with Open_file(filename, mode) as f:
        key = f.read()
        key = unpickle_string(key)

    return key


####################################################
#
#   Desc: # Write a key to a file
#
#
####################################################
def write_to_file(filename, key):
    
    # Write in binary form
    mode = "wb" 

    with Open_file(filename, mode) as f:
        key = pickle_object(key)
        result = f.write(key)
        
    return 0