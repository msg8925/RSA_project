####################################################
#
#   Desc: 
#
#
####################################################
class Open_file():

    # init method runs when object is created
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        

    # enter method runs when an operation such as a write is performed
    def __enter__(self):
        self.f = open(self.filename, self.mode)
        
        return self.f


    # exit method runs when an operation has finshed
    def __exit__(self, exc_type, exc_cal, traceback):
        self.f.close()