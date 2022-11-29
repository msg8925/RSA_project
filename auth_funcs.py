from file_context_manager import file_context_manager
from pickleEmployee import pickle_object, unpickle_string


####################################################
#
#   Desc: Places the pickled 'employee' object into
#         a file named 'auth_vars.pkl'. This file is
#         is used to show the currently logged in user       
#
####################################################
def set_current_logged_in_employee(employee):

    # Open the "auth_vars.pkl" file with a context manager 
    with file_context_manager("auth_vars.pkl", "wb") as f:
        
        # Pickle the 'employee' object
        employee = pickle_object(employee)
        
        # Write it to the 'auth_vars.pkl' file    
        f.write(employee)

    return 0    


####################################################
#
#   Desc: Retrieves the currently logged in user by
#         getting the serialized 'employee' object 
#         from the auth_vars.pkl file and unpickling
#         and returning it.
#
####################################################
def get_current_logged_in_employee():

    # Open the "auth_vars.pkl" file with a context manager
    with file_context_manager("auth_vars.pkl", "rb") as f:
        
        # Read the file and retrieve the pickled string
        employee = f.read()

        # Unpickle the string and store it in the 'employee' object
        employee = unpickle_string(employee)
        
    return employee        


