import sys, res
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UneditedDashboard4.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from AddWorkoutV2 import ui_AddWorkout



class Ui_MainWindow(object):
    def setupUi(self, MainWindow, UserID):
        self.UserID = UserID
        self.uiAddWorkout = ui_AddWorkout()
        self.main_window = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 545)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MainWindowWidget = QtWidgets.QWidget(MainWindow)
        self.MainWindowWidget.setStyleSheet("layoutLeftMargin")
        self.MainWindowWidget.setObjectName("MainWindowWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MainWindowWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.MainWindowWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.LeftMenuWidget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftMenuWidget.sizePolicy().hasHeightForWidth())
        self.LeftMenuWidget.setSizePolicy(sizePolicy)
        self.LeftMenuWidget.setMaximumSize(QtCore.QSize(310, 16777215))
        self.LeftMenuWidget.setStyleSheet("QWidget {\n"
"    background-color: #272727; \n"
"}")
        self.LeftMenuWidget.setObjectName("LeftMenuWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.LeftMenuWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.NameWidget = QtWidgets.QWidget(self.LeftMenuWidget)
        self.NameWidget.setMaximumSize(QtCore.QSize(16777215, 75))
        self.NameWidget.setObjectName("NameWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.NameWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NameLabel = QtWidgets.QLabel(self.NameWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameLabel.sizePolicy().hasHeightForWidth())
        self.NameLabel.setSizePolicy(sizePolicy)
        self.NameLabel.setMaximumSize(QtCore.QSize(16777215, 75))
        self.NameLabel.setObjectName("NameLabel")
        self.verticalLayout.addWidget(self.NameLabel)
        self.verticalLayout_9.addWidget(self.NameWidget)
        self.SearchWidget = QtWidgets.QWidget(self.LeftMenuWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchWidget.sizePolicy().hasHeightForWidth())
        self.SearchWidget.setSizePolicy(sizePolicy)
        self.SearchWidget.setMaximumSize(QtCore.QSize(16777215, 75))
        self.SearchWidget.setObjectName("SearchWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.SearchWidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.SearchBar = QtWidgets.QLineEdit(self.SearchWidget)
        self.SearchBar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.SearchBar.setStyleSheet("QLineEdit {\n"
"\n"
"    padding-right: 20px; /* Adjust padding so text does not overlap the icon */\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    border-top: 1px solid rgba(105, 118, 132, 255);\n"
"    border-right: 1px solid rgba(105, 118, 132, 255);\n"
"    border-left: 1px solid rgba(105, 118, 132, 255);\n"
"    border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
"    color: rgba(255, 255, 255, 230);\n"
"    padding-top: 2px;\n"
"    padding-bottom: 7px;\n"
"    padding-left: 2px;\n"
"    border-radius: 3px; /* Adjust this value to change the roundness */\n"
"}\n"
"")
        self.SearchBar.setText("")
        self.SearchBar.setObjectName("SearchBar")
        self.verticalLayout_7.addWidget(self.SearchBar)
        self.verticalLayout_9.addWidget(self.SearchWidget)
        self.UpperListWidget = QtWidgets.QWidget(self.LeftMenuWidget)
        self.UpperListWidget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.UpperListWidget.setObjectName("UpperListWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.UpperListWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.GoalsButton = QtWidgets.QPushButton(self.UpperListWidget)
        self.GoalsButton.setStyleSheet("color: white; \n"
"border: none;\n"
"background: transparent;\n"
"text-align: left; /* Align the text inside the QPushButton to the left */\n"
"padding-left: 10px;\n"
"")
        self.GoalsButton.setObjectName("GoalsButton")
        self.verticalLayout_3.addWidget(self.GoalsButton)
        self.EventsButton = QtWidgets.QPushButton(self.UpperListWidget)
        self.EventsButton.setStyleSheet("color: white; \n"
"border: none;\n"
"background: transparent;\n"
"text-align: left; /* Align the text inside the QPushButton to the left */\n"
"padding-left: 10px;\n"
"")
        self.EventsButton.setObjectName("EventsButton")
        self.verticalLayout_3.addWidget(self.EventsButton)
        self.WorkoutsButton = QtWidgets.QPushButton(self.UpperListWidget)
        self.WorkoutsButton.setStyleSheet("color: white; \n"
"border: none;\n"
"background: transparent;\n"
"text-align: left; /* Align the text inside the QPushButton to the left */\n"
"padding-left: 10px;\n"
"")
        self.WorkoutsButton.setObjectName("WorkoutsButton")
        self.verticalLayout_3.addWidget(self.WorkoutsButton)
        self.StatsButton = QtWidgets.QPushButton(self.UpperListWidget)
        self.StatsButton.setStyleSheet("color: white; \n"
"border: none;\n"
"background: transparent;\n"
"text-align: left; /* Align the text inside the QPushButton to the left */\n"
"padding-left: 10px;\n"
"")
        self.StatsButton.setObjectName("StatsButton")
        self.verticalLayout_3.addWidget(self.StatsButton)
        self.ProgressButton = QtWidgets.QPushButton(self.UpperListWidget)
        self.ProgressButton.setStyleSheet("color: white; \n"
"border: none;\n"
"background: transparent;\n"
"text-align: left; /* Align the text inside the QPushButton to the left */\n"
"padding-left: 10px;\n"
"")
        self.ProgressButton.setObjectName("ProgressButton")
        self.verticalLayout_3.addWidget(self.ProgressButton)
        self.line = QtWidgets.QFrame(self.UpperListWidget)
        self.line.setStyleSheet("color: white; \n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout_9.addWidget(self.UpperListWidget)
        self.LowerListWidget = QtWidgets.QWidget(self.LeftMenuWidget)
        self.LowerListWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.LowerListWidget.setStyleSheet("")
        self.LowerListWidget.setObjectName("LowerListWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.LowerListWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.SettingsButton = QtWidgets.QPushButton(self.LowerListWidget)
        self.SettingsButton.setStyleSheet("color: white; \n"
"border: none;\n"
"background: transparent;\n"
"text-align: left; /* Align the text inside the QPushButton to the left */\n"
"padding-left: 10px;\n"
"")
        self.SettingsButton.setObjectName("SettingsButton")
        self.verticalLayout_8.addWidget(self.SettingsButton)
        self.HelpButton = QtWidgets.QPushButton(self.LowerListWidget)
        self.HelpButton.setStyleSheet("color: white; \n"
"border: none;\n"
"background: transparent;\n"
"text-align: left; /* Align the text inside the QPushButton to the left */\n"
"padding-left: 10px;\n"
"")
        self.HelpButton.setObjectName("HelpButton")
        self.verticalLayout_8.addWidget(self.HelpButton)
        self.LogOutButton = QtWidgets.QPushButton(self.LowerListWidget)
        self.LogOutButton.setStyleSheet("color: white; \n"
"border: none;\n"
"background: transparent;\n"
"text-align: left; /* Align the text inside the QPushButton to the left */\n"
"padding-left: 10px;\n"
"")
        self.LogOutButton.setObjectName("LogOutButton")
        self.verticalLayout_8.addWidget(self.LogOutButton)
        self.verticalLayout_9.addWidget(self.LowerListWidget)
        self.MainStackedWidget = QtWidgets.QStackedWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainStackedWidget.sizePolicy().hasHeightForWidth())
        self.MainStackedWidget.setSizePolicy(sizePolicy)
        self.MainStackedWidget.setStyleSheet("QWidget {\n"
"    background-color: #1C1C1C; \n"
"}")
        self.MainStackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MainStackedWidget.setLineWidth(0)
        self.MainStackedWidget.setObjectName("MainStackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.DashboardWidget = QtWidgets.QWidget(self.page1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DashboardWidget.sizePolicy().hasHeightForWidth())
        self.DashboardWidget.setSizePolicy(sizePolicy)
        self.DashboardWidget.setObjectName("DashboardWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.DashboardWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.AddWorkoutButtonTop_5 = QtWidgets.QPushButton(self.DashboardWidget)
        self.AddWorkoutButtonTop_5.setStyleSheet("color: white; \n"
"border: none;\n"
"background: transparent;\n"
"text-align: left; /* Align the text inside the QPushButton to the left */\n"
"")
        self.AddWorkoutButtonTop_5.setObjectName("AddWorkoutButtonTop_5")
        self.gridLayout.addWidget(self.AddWorkoutButtonTop_5, 0, 11, 1, 1)
        self.DistanceLabel_5 = QtWidgets.QLabel(self.DashboardWidget)
        self.DistanceLabel_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DistanceLabel_5.setFont(font)
        self.DistanceLabel_5.setStyleSheet("color: white; \n"
"")
        self.DistanceLabel_5.setObjectName("DistanceLabel_5")
        self.gridLayout.addWidget(self.DistanceLabel_5, 5, 0, 1, 2)
        self.ActivityLabel_5 = QtWidgets.QLabel(self.DashboardWidget)
        self.ActivityLabel_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.ActivityLabel_5.setFont(font)
        self.ActivityLabel_5.setStyleSheet("color: white; \n"
"")
        self.ActivityLabel_5.setObjectName("ActivityLabel_5")
        self.gridLayout.addWidget(self.ActivityLabel_5, 2, 0, 1, 1)
        self.DateLabel_5 = QtWidgets.QLabel(self.DashboardWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DateLabel_5.sizePolicy().hasHeightForWidth())
        self.DateLabel_5.setSizePolicy(sizePolicy)
        self.DateLabel_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.DateLabel_5.setFont(font)
        self.DateLabel_5.setStyleSheet("color: white; \n"
"")
        self.DateLabel_5.setObjectName("DateLabel_5")
        self.gridLayout.addWidget(self.DateLabel_5, 0, 0, 1, 9)
        self.AllFilterButton_5 = QtWidgets.QPushButton(self.DashboardWidget)
        self.AllFilterButton_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.AllFilterButton_5.setStyleSheet("color: white; \n"
"\n"
"background: transparent;\n"
"text-align: center; /* Align the text inside the QPushButton to the left */\n"
"border-radius: 3px; /* Adjust this value to change the roundness */\n"
"border: 1px solid rgba(105, 118, 132, 255);\n"
"\n"
"\n"
"")
        self.AllFilterButton_5.setObjectName("AllFilterButton_5")
        self.gridLayout.addWidget(self.AllFilterButton_5, 3, 0, 1, 1)
        self.DistanceAmount_5 = QtWidgets.QLabel(self.DashboardWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DistanceAmount_5.setFont(font)
        self.DistanceAmount_5.setStyleSheet("color: white; \n"
"")
        self.DistanceAmount_5.setObjectName("DistanceAmount_5")
        self.gridLayout.addWidget(self.DistanceAmount_5, 4, 0, 1, 1)
        self.TrainingFilterButton_5 = QtWidgets.QPushButton(self.DashboardWidget)
        self.TrainingFilterButton_5.setMaximumSize(QtCore.QSize(70, 16777215))
        self.TrainingFilterButton_5.setStyleSheet("color: white; \n"
"\n"
"background: transparent;\n"
"text-align: center; /* Align the text inside the QPushButton to the left */\n"
"border-radius: 3px; /* Adjust this value to change the roundness */\n"
"border: 1px solid rgba(105, 118, 132, 255);\n"
"\n"
"\n"
"")
        self.TrainingFilterButton_5.setObjectName("TrainingFilterButton_5")
        self.gridLayout.addWidget(self.TrainingFilterButton_5, 3, 1, 1, 1)
        self.GymFilterButton_5 = QtWidgets.QPushButton(self.DashboardWidget)
        self.GymFilterButton_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.GymFilterButton_5.setStyleSheet("color: white; \n"
"\n"
"background: transparent;\n"
"text-align: center; /* Align the text inside the QPushButton to the left */\n"
"border-radius: 3px; /* Adjust this value to change the roundness */\n"
"border: 1px solid rgba(105, 118, 132, 255);\n"
"\n"
"\n"
"")
        self.GymFilterButton_5.setObjectName("GymFilterButton_5")
        self.gridLayout.addWidget(self.GymFilterButton_5, 3, 2, 1, 1)
        self.RaceFilterButton_5 = QtWidgets.QPushButton(self.DashboardWidget)
        self.RaceFilterButton_5.setStyleSheet("color: white; \n"
"\n"
"background: transparent;\n"
"text-align: center; /* Align the text inside the QPushButton to the left */\n"
"border-radius: 3px; /* Adjust this value to change the roundness */\n"
"border: 1px solid rgba(105, 118, 132, 255);\n"
"\n"
"\n"
"")
        self.RaceFilterButton_5.setObjectName("RaceFilterButton_5")
        self.gridLayout.addWidget(self.RaceFilterButton_5, 3, 3, 1, 1)
        self.DurationAmount_5 = QtWidgets.QLabel(self.DashboardWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DurationAmount_5.setFont(font)
        self.DurationAmount_5.setStyleSheet("color: white; \n"
"")
        self.DurationAmount_5.setObjectName("DurationAmount_5")
        self.gridLayout.addWidget(self.DurationAmount_5, 4, 2, 1, 2)
        self.DurationLabel_5 = QtWidgets.QLabel(self.DashboardWidget)
        self.DurationLabel_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DurationLabel_5.setFont(font)
        self.DurationLabel_5.setStyleSheet("color: white; \n"
"")
        self.DurationLabel_5.setObjectName("DurationLabel_5")
        self.gridLayout.addWidget(self.DurationLabel_5, 5, 2, 1, 1)
        self.TWorkoutsAmount_5 = QtWidgets.QLabel(self.DashboardWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TWorkoutsAmount_5.setFont(font)
        self.TWorkoutsAmount_5.setStyleSheet("color: white; \n"
"")
        self.TWorkoutsAmount_5.setObjectName("TWorkoutsAmount_5")
        self.gridLayout.addWidget(self.TWorkoutsAmount_5, 4, 4, 1, 1)
        self.GWorkoutsLabel_5 = QtWidgets.QLabel(self.DashboardWidget)
        self.GWorkoutsLabel_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GWorkoutsLabel_5.setFont(font)
        self.GWorkoutsLabel_5.setStyleSheet("color: white; \n"
"")
        self.GWorkoutsLabel_5.setObjectName("GWorkoutsLabel_5")
        self.gridLayout.addWidget(self.GWorkoutsLabel_5, 5, 6, 1, 1)
        self.RacesAmount_5 = QtWidgets.QLabel(self.DashboardWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.RacesAmount_5.setFont(font)
        self.RacesAmount_5.setStyleSheet("color: white; \n"
"")
        self.RacesAmount_5.setObjectName("RacesAmount_5")
        self.gridLayout.addWidget(self.RacesAmount_5, 4, 6, 1, 1)
        self.RacesLabel_5 = QtWidgets.QLabel(self.DashboardWidget)
        self.RacesLabel_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.RacesLabel_5.setFont(font)
        self.RacesLabel_5.setStyleSheet("color: white; \n"
"")
        self.RacesLabel_5.setObjectName("RacesLabel_5")
        self.gridLayout.addWidget(self.RacesLabel_5, 5, 8, 1, 1)
        self.GWorkoutsAmount_5 = QtWidgets.QLabel(self.DashboardWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.GWorkoutsAmount_5.setFont(font)
        self.GWorkoutsAmount_5.setStyleSheet("color: white; \n"
"")
        self.GWorkoutsAmount_5.setObjectName("GWorkoutsAmount_5")
        self.gridLayout.addWidget(self.GWorkoutsAmount_5, 4, 8, 1, 1)
        self.TWorkoutsLabel_5 = QtWidgets.QLabel(self.DashboardWidget)
        self.TWorkoutsLabel_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.TWorkoutsLabel_5.setFont(font)
        self.TWorkoutsLabel_5.setStyleSheet("color: white; \n"
"")
        self.TWorkoutsLabel_5.setObjectName("TWorkoutsLabel_5")
        self.gridLayout.addWidget(self.TWorkoutsLabel_5, 5, 4, 1, 2)
        self.verticalLayout_10.addWidget(self.DashboardWidget)
        self.WorkoutLogWidget = QtWidgets.QWidget(self.page1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WorkoutLogWidget.sizePolicy().hasHeightForWidth())
        self.WorkoutLogWidget.setSizePolicy(sizePolicy)
        self.WorkoutLogWidget.setStyleSheet("QWidget {\n"
"border-radius: 400px;\n"
"    background-color: #272727; \n"
"}")
        self.WorkoutLogWidget.setObjectName("WorkoutLogWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.WorkoutLogWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.DateLabelDash_5 = QtWidgets.QLabel(self.WorkoutLogWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DateLabelDash_5.setFont(font)
        self.DateLabelDash_5.setStyleSheet("color: white; \n"
"")
        self.DateLabelDash_5.setObjectName("DateLabelDash_5")
        self.gridLayout_2.addWidget(self.DateLabelDash_5, 0, 0, 1, 1)
        self.ActivityLabelDash_5 = QtWidgets.QLabel(self.WorkoutLogWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ActivityLabelDash_5.setFont(font)
        self.ActivityLabelDash_5.setStyleSheet("color: white; \n"
"")
        self.ActivityLabelDash_5.setObjectName("ActivityLabelDash_5")
        self.gridLayout_2.addWidget(self.ActivityLabelDash_5, 0, 1, 1, 1)
        self.DistancesLabelDash_5 = QtWidgets.QLabel(self.WorkoutLogWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DistancesLabelDash_5.setFont(font)
        self.DistancesLabelDash_5.setStyleSheet("color: white; \n"
"")
        self.DistancesLabelDash_5.setObjectName("DistancesLabelDash_5")
        self.gridLayout_2.addWidget(self.DistancesLabelDash_5, 0, 2, 1, 1)
        self.FocusLabelDash_5 = QtWidgets.QLabel(self.WorkoutLogWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.FocusLabelDash_5.setFont(font)
        self.FocusLabelDash_5.setStyleSheet("color: white; \n"
"")
        self.FocusLabelDash_5.setObjectName("FocusLabelDash_5")
        self.gridLayout_2.addWidget(self.FocusLabelDash_5, 0, 3, 1, 1)
        self.stackedWidget_6 = QtWidgets.QStackedWidget(self.WorkoutLogWidget)
        self.stackedWidget_6.setStyleSheet("QWidget {\n"
"border-radius: 400px;\n"
"    background-color: #ffffff; \n"
"}")
        self.stackedWidget_6.setObjectName("stackedWidget_6")
        self.page_26 = QtWidgets.QWidget()
        self.page_26.setObjectName("page_26")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_26)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.AddWorkoutButtonWidget_5 = QtWidgets.QPushButton(self.page_26)
        self.AddWorkoutButtonWidget_5.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(32)
        self.AddWorkoutButtonWidget_5.setFont(font)
        self.AddWorkoutButtonWidget_5.setStyleSheet("color: white; \n"
"")
        self.AddWorkoutButtonWidget_5.setObjectName("AddWorkoutButtonWidget_5")
        self.verticalLayout_11.addWidget(self.AddWorkoutButtonWidget_5)
        self.WorkoutsAmountDefaultLabel_5 = QtWidgets.QLabel(self.page_26)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WorkoutsAmountDefaultLabel_5.setFont(font)
        self.WorkoutsAmountDefaultLabel_5.setStyleSheet("color: white; \n"
"")
        self.WorkoutsAmountDefaultLabel_5.setObjectName("WorkoutsAmountDefaultLabel_5")
        self.verticalLayout_11.addWidget(self.WorkoutsAmountDefaultLabel_5)
        self.stackedWidget_6.addWidget(self.page_26)
        self.page_27 = QtWidgets.QWidget()
        self.page_27.setObjectName("page_27")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_27)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.stackedWidget_6.addWidget(self.page_27)
        self.gridLayout_2.addWidget(self.stackedWidget_6, 1, 0, 1, 4)
        self.verticalLayout_10.addWidget(self.WorkoutLogWidget)
        self.MainStackedWidget.addWidget(self.page1)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.MainWindowWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.MainStackedWidget.setCurrentIndex(0)
        self.stackedWidget_6.setCurrentIndex(0)
        self.showWorkouts()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        def showWorkouts(self):
                # Fetch workout data
                workout_data = self.uiAddWorkout.fetchWorkouts(self.UserID)

                # Check if there are workouts, if not, show default page
                if not any(workout_data.values()):
                        self.stackedWidget_6.setCurrentIndex(0)  # Showing default page with no workouts
                        return

                # If workouts exist, show them on page 27
                self.stackedWidget_6.setCurrentIndex(1)

                # Create a new widget with grid layout for workouts
                workout_widget = QtWidgets.QWidget()
                workout_layout = QtWidgets.QGridLayout(workout_widget)

                row = 0
                for category, workouts in workout_data.items():
                        for workout in workouts:
                                date, activity, distances, focus = workout
                                date_label = QtWidgets.QLabel(str(date))
                                activity_label = QtWidgets.QLabel(activity)
                                distances_label = QtWidgets.QLabel(distances)
                                focus_label = QtWidgets.QLabel(focus)

                                workout_layout.addWidget(date_label, row, 0)
                                workout_layout.addWidget(activity_label, row, 1)
                                workout_layout.addWidget(distances_label, row, 2)
                                workout_layout.addWidget(focus_label, row, 3)
                                row += 1

                        # Add the workout widget to page_27
                self.page_27.layout().addWidget(workout_widget)



        def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NameLabel.setText(_translate("MainWindow", "TextLabel"))
        self.SearchBar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.GoalsButton.setText(_translate("MainWindow", "Goals"))
        self.EventsButton.setText(_translate("MainWindow", "Upcoming Events"))
        self.WorkoutsButton.setText(_translate("MainWindow", "Workouts"))
        self.StatsButton.setText(_translate("MainWindow", "Stats"))
        self.ProgressButton.setText(_translate("MainWindow", "Progress"))
        self.SettingsButton.setText(_translate("MainWindow", "Settings"))
        self.HelpButton.setText(_translate("MainWindow", "Help"))
        self.LogOutButton.setText(_translate("MainWindow", "Log Out"))
        self.AddWorkoutButtonTop_5.setText(_translate("MainWindow", "+ Add Workout"))
        self.DistanceLabel_5.setText(_translate("MainWindow", "Distance (km)"))
        self.ActivityLabel_5.setText(_translate("MainWindow", "Activity"))
        self.DateLabel_5.setText(_translate("MainWindow", "NOVEMBER 13, 2023"))
        self.AllFilterButton_5.setText(_translate("MainWindow", "All"))
        self.DistanceAmount_5.setText(_translate("MainWindow", "0.00"))
        self.TrainingFilterButton_5.setText(_translate("MainWindow", "Training"))
        self.GymFilterButton_5.setText(_translate("MainWindow", "Gym"))
        self.RaceFilterButton_5.setText(_translate("MainWindow", "Race"))
        self.DurationAmount_5.setText(_translate("MainWindow", "0:00.00"))
        self.DurationLabel_5.setText(_translate("MainWindow", "Duration"))
        self.TWorkoutsAmount_5.setText(_translate("MainWindow", "0"))
        self.GWorkoutsLabel_5.setText(_translate("MainWindow", "Gym Workouts"))
        self.RacesAmount_5.setText(_translate("MainWindow", "0"))
        self.RacesLabel_5.setText(_translate("MainWindow", "Races"))
        self.GWorkoutsAmount_5.setText(_translate("MainWindow", "0"))
        self.TWorkoutsLabel_5.setText(_translate("MainWindow", "Track Workouts"))
        self.DateLabelDash_5.setText(_translate("MainWindow", "Date"))
        self.ActivityLabelDash_5.setText(_translate("MainWindow", "Activity"))
        self.DistancesLabelDash_5.setText(_translate("MainWindow", "Distances"))
        self.FocusLabelDash_5.setText(_translate("MainWindow", "Focus"))
        self.AddWorkoutButtonWidget_5.setText(_translate("MainWindow", "+"))
        self.WorkoutsAmountDefaultLabel_5.setText(_translate("MainWindow", "             You have no workouts for this month."))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))



        
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow, UserID=1)
        MainWindow.show()
        sys.exit(app.exec_())

