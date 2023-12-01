from PyQt5.QtWidgets import QLineEdit

def addTraining(gridLayout):
    row = gridLayout.rowCount()
    for col in range(5):  # Assuming 5 QLineEdit widgets need to be added
        timeEdit = QLineEdit()
        gridLayout.addWidget(timeEdit, row, col)

def addRace(gridLayout):
    row = gridLayout.rowCount()
    for col in range(2):  # Assuming 2 QLineEdit widgets need to be added
        timeEdit = QLineEdit()
        gridLayout.addWidget(timeEdit, row, col)

def addGym(gridLayout):
    row = gridLayout.rowCount()
    for col in range(4):  # Assuming 4 QLineEdit widgets need to be added
        timeEdit = QLineEdit()
        gridLayout.addWidget(timeEdit, row, col)