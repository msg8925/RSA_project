import pickle


####################################################
#
#   Desc: 
#
#
####################################################
def pickle_object(my_object):
    pickled_object = pickle.dumps(my_object)
    return pickled_object


####################################################
#
#   Desc: 
#
#
####################################################
def unpickle_string(my_string):
    unpickled_string = pickle.loads(my_string)
    return unpickled_string   
