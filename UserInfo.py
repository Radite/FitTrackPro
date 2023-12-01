from DatabaseConnection import connect_to_database, execute_query, close_connection

class UserInfo(object):
    def __init__(self, UserID=1):
        self.UserID = UserID
        self.user_data = None  # Initialize an instance variable to store user data

        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'fittrackpro'
        }

        conn = connect_to_database(**db_config)
        if conn:
            try:
                query = "SELECT * FROM User WHERE UserID = %s"
                user_id = (self.UserID,)  # user_id needs to be a tuple
                cursor = execute_query(conn, query, user_id)
                if cursor:
                    
                    self.user_data = cursor.fetchone()  # Fetch one record
                    print(self.user_data)
                    cursor.close()
            finally:
                close_connection(conn)

    def get_email(self):
        if self.user_data:
            return self.user_data[2]  # Assuming email is at index 2
        else:
            return None

    def get_fullname(self):
        if self.user_data:
            FName = str(self.user_data[4])
            LName = str(self.user_data[5])
            FullName = FName+' '+LName
            return FullName
        else:
            return None