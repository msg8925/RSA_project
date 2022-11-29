from file_context_manager import Open_file
from pickle_it import pickle_object, unpickle_string

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