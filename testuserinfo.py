# Assuming UserInfo class is in a file named user_info.py
from UserInfo import UserInfo

def test_user_info(user_id):
    try:
        user_info = UserInfo(user_id)
        # The UserInfo constructor should print the user data
    except Exception as e:
        print(f"An error occurred: {e}")

# Test with a specific user ID, replace 1 with a valid UserID from your database
test_user_info(1)
