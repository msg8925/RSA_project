class Keys:

    def __init__(self, public_key, private_key, employee_id):
        self.public_key = public_key
        self.private_key = private_key
        self.employee_id = employee_id


    def __repr__(self):
        return f"keys('Public_key: '{self.public_key}, 'Private_key: {self.private_key}', 'employee id: '{self.employee_id})" 

    def __str__(self):
        return f"keys('Public_key: '{self.public_key}, 'Private_key: {self.private_key}', 'employee id: '{self.employee_id})" 