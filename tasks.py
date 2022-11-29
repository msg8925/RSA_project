from decorators import login_required


####################################################
#
#   Desc: 
#
#
####################################################
@login_required
def some_secure_function():
    print("This function will run and shows results after the decorator has run.")

