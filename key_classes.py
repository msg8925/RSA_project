class Keys:

    def __init__(self, PUBLIC_KEY, PRIVATE_KEY, user_id):
        self.PUBLIC_KEY = PUBLIC_KEY
        self.PRIVATE_KEY = PRIVATE_KEY
        self.user_id = user_id


    def __repr__(self):
        return f"keys('Public_key: '{self.PUBLIC_KEY}, 'Private_key: {self.PRIVATE_KEY}', 'User id: '{self.user_id})" 

    def __str__(self):
        return f"keys('Public_key: '{self.PUBLIC_KEY}, 'Private_key: {self.PRIVATE_KEY}', 'User id: '{self.user_id})" 