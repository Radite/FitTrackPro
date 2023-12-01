import sys
from PyQt5.QtWidgets import QApplication
import loginUI

def logout(current_window):
    """
    Closes the current window and opens the login window.
    """
    login_window = loginUI.LoginForm()
    login_window.show()
