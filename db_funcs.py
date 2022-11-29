from classes import DB_context_manager
#from key_classes import Keys

####################################################
#
#   Desc: Create tables  
#
#
####################################################
def open_db(DB_NAME):

    with DB_context_manager(DB_NAME) as c:
        
        c.execute("""

            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FIRSTNAME TEXT,
                LASTNAME TEXT,
                USERNAME TEXT,
                PASSWORD TEXT,
                SALARY INT
            );
            
        """)

        c.execute("""

            CREATE TABLE IF NOT EXISTS session (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                EMPLOYEE_ID INTEGER,
                FOREIGN KEY (EMPLOYEE_ID) REFERENCES employee (id)            
            );
            
        """)

        c.execute("""

            CREATE TABLE IF NOT EXISTS keys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                PUBLIC_KEY TEXT,
                PRIVATE_KEY TEXT,
                EMPLOYEE_ID INTEGER,
                FOREIGN KEY (EMPLOYEE_ID) REFERENCES employee (id) 
            );
            
        """)


    return 0


####################################################
#
#   Desc: Insert employee into DB
#
#
####################################################
def insert_into_db(DB_NAME, employee):
    
    with DB_context_manager(DB_NAME) as c:
        c.execute("INSERT INTO employee (id, FIRSTNAME, LASTNAME, USERNAME, PASSWORD, SALARY) VALUES (:id, :firstname, :lastname, :username, :password, :salary)", {'id': None, 'firstname': employee.firstname, 'lastname': employee.lastname, 'username': employee.username, 'password': employee.password, 'salary': employee.salary})
        
    return 0


####################################################
#
#   Desc: select employee from DB
#
#
####################################################
def select_from_db(DB_NAME, username):
    
    with DB_context_manager(DB_NAME) as c:
        c.execute("SELECT * FROM employee WHERE USERNAME=:username", {'username': username})
        employee = c.fetchone()

    return employee


####################################################
#
#   Desc: Select a session from DB
#
#
####################################################
def select_session_from_db(DB_NAME, employee_id):
    
    with DB_context_manager(DB_NAME) as c:
        c.execute("SELECT * FROM session WHERE EMPLOYEE_ID=:employee_id", {'employee_id': employee_id})
        session = c.fetchone()

    return session


####################################################
#
#   Desc: Insert session into DB
#
#
####################################################
def insert_session_into_db(DB_NAME, employee_id):
    
    with DB_context_manager(DB_NAME) as c:
        c.execute("INSERT INTO session (id, EMPLOYEE_ID) VALUES (:id, :employee_id)", {'id': None, 'employee_id': employee_id})
        
    return 0    


####################################################
#
#   Desc: Delete a session from DB
#
#
####################################################
def delete_session_from_db(DB_NAME, employee_id):

    with DB_context_manager(DB_NAME) as c:
        c.execute("DELETE FROM session WHERE EMPLOYEE_ID=:employee_id", {'id': None, 'employee_id': employee_id})

    return 0   


####################################################
#
#   Desc: Add public and private keys to 'keys' 
#         table in DB
#
####################################################
def insert_key_into_db(DB_NAME, keys):

    with DB_context_manager(DB_NAME) as c:
        c.execute("INSERT INTO keys (id, PUBLIC_KEY, PRIVATE_KEY, USER_ID) VALUES (:id, :public_key, :private_key, :user_id)", {'id': None, 'public_key': keys.PUBLIC_KEY, 'private_key':  keys.PRIVATE_KEY, 'user_id': keys.user_id}) 

    return 0