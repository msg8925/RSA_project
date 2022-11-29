####################################################
#
#   Desc: 
#
#
####################################################
class Employee:

    def __init__(self, firstname, lastname, username, password, salary):
        self.id = None
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.salary = salary 


    def set_employee_id(self, id):
        self.id = id


    def get_employee_id(self):
        return self.id


    def __repr__(self):
        return f"Employee({self.firstname}, {self.lastname}, {self.username}, {self.salary})"  