from file_context_manager import Open_file

####################################################
#
#   Desc: # Read a key from a file
#
#
####################################################
def read_from_file(filename, mode):
    
    with Open_file(filename, mode) as f:
        key = f.read()
        
    return key


####################################################
#
#   Desc: # Write a key to a file
#
#
####################################################
def write_to_file(filename, mode, key):
    
    with Open_file(filename, mode) as f:
        result = f.write(key)
        
    return 0