# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# Edited by Nir Pikan - knows what he's doing

from PyQt5 import QtCore, QtGui, QtWidgets
from Classes.Calculator import Calculator, ErrorMsg, Course


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, calculator):
        self.calculator = calculator

        # create main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create My-GPA-Calculator
        self.myGPAcalcLabel = QtWidgets.QLabel(self.centralwidget)
        self.myGPAcalcLabel.setGeometry(QtCore.QRect(350, 5, 300, 32))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.myGPAcalcLabel.setFont(font)
        self.myGPAcalcLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.myGPAcalcLabel.setObjectName("myGPAcalcLabel")

        # create messageLabel
        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        self.messageLabel.setGeometry(QtCore.QRect(10, 790, 980, 50))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.messageLabel.setStyleSheet("background-color: yellow")
        self.messageLabel.setFont(font)
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setObjectName("messageLabel")

        # create myCoursesLabel
        self.myCoursesLabel = QtWidgets.QLabel(self.centralwidget)
        self.myCoursesLabel.setGeometry(QtCore.QRect(20, 40, 122, 24))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.myCoursesLabel.setFont(font)
        self.myCoursesLabel.setObjectName("myCoursesLabel")

        # create totalPointsLabel
        self.totalPointsLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalPointsLabel.setGeometry(QtCore.QRect(770, 100, 250, 24))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.totalPointsLabel.setFont(font)
        self.totalPointsLabel.setObjectName("totalPointsLabel")

        # create gpaLabel
        self.gpaLabel = QtWidgets.QLabel(self.centralwidget)
        self.gpaLabel.setGeometry(QtCore.QRect(770, 140, 200, 24))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.gpaLabel.setFont(font)
        self.gpaLabel.setObjectName("gpaLabel")

        # create nameLabel
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(115, 80, 81, 20))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")

        # create pointsLabel
        self.pointsLabel = QtWidgets.QLabel(self.centralwidget)
        self.pointsLabel.setGeometry(QtCore.QRect(325, 80, 81, 20))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pointsLabel.setFont(font)
        self.pointsLabel.setObjectName("pointsLabel")

        # create gradeLabel
        self.gradeLabel = QtWidgets.QLabel(self.centralwidget)
        self.gradeLabel.setGeometry(QtCore.QRect(535, 80, 81, 20))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.gradeLabel.setFont(font)
        self.gradeLabel.setObjectName("gradeLabel")

        # create frame-grid-scroll area for courses
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 90, 761, 281))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")

        self.coursesScrollArea = QtWidgets.QScrollArea(self.frame)
        self.coursesScrollArea.setWidgetResizable(True)
        self.coursesScrollArea.setObjectName("coursesScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(5, 5, 5, -1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.coursesScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.coursesScrollArea, 0, 1, 1, 1)

        # create Add-course base
        self.addCourseHorizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.addCourseHorizontalLayoutWidget.setGeometry(QtCore.QRect(20, 370, 741, 51))
        self.addCourseHorizontalLayoutWidget.setObjectName("addCourseHorizontalLayoutWidget")
        self.addCourseHorizontalLayout = QtWidgets.QHBoxLayout(self.addCourseHorizontalLayoutWidget)
        self.addCourseHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.addCourseHorizontalLayout.setObjectName("addCourseHorizontalLayout")

        # add-course name
        self.nameAddLineEdit = QtWidgets.QLineEdit(self.addCourseHorizontalLayoutWidget)
        self.nameAddLineEdit.setObjectName("nameAddLineEdit")
        self.addCourseHorizontalLayout.addWidget(self.nameAddLineEdit)

        # add-course pointsSpinBox
        self.pointsSpinBox = QtWidgets.QDoubleSpinBox(self.addCourseHorizontalLayoutWidget)
        self.pointsSpinBox.setWrapping(False)
        self.pointsSpinBox.setFrame(True)
        self.pointsSpinBox.setReadOnly(False)
        self.pointsSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.pointsSpinBox.setPrefix("")
        self.pointsSpinBox.setSuffix("")
        self.pointsSpinBox.setMinimum(1.0)
        self.pointsSpinBox.setMaximum(10.0)
        self.pointsSpinBox.setSingleStep(0.5)
        self.pointsSpinBox.setObjectName("pointsSpinBox")
        self.addCourseHorizontalLayout.addWidget(self.pointsSpinBox)
        self.pointsSpinBox.valueChanged.connect(self.set_course_points)

        # add-course gradeSpinBox
        self.gradeSpinBox = QtWidgets.QSpinBox(self.addCourseHorizontalLayoutWidget)
        self.gradeSpinBox.setMaximum(100)
        self.gradeSpinBox.setObjectName("gradeSpinBox")
        self.addCourseHorizontalLayout.addWidget(self.gradeSpinBox)

        # add-course button
        self.addCourseButton = QtWidgets.QPushButton(self.addCourseHorizontalLayoutWidget)
        self.addCourseButton.setObjectName("addCourseButton")
        self.addCourseHorizontalLayout.addWidget(self.addCourseButton)
        self.addCourseButton.clicked.connect(self.add_course_clicked)

        # create features label
        self.featuresLabel = QtWidgets.QLabel(self.centralwidget)
        self.featuresLabel.setGeometry(QtCore.QRect(20, 450, 122, 24))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.featuresLabel.setFont(font)
        self.featuresLabel.setObjectName("featuresLabel")

        # create Top3 results
        self.top3VerticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.top3VerticalLayoutWidget.setGeometry(QtCore.QRect(270, 480, 300, 81))
        self.top3VerticalLayoutWidget.setObjectName("top3VerticalLayoutWidget")
        self.top3VerticalLayout = QtWidgets.QVBoxLayout(self.top3VerticalLayoutWidget)
        self.top3VerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top3VerticalLayout.setObjectName("top3VerticalLayout")

        # 1st result
        self.top3Label = QtWidgets.QLabel(self.top3VerticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        self.top3Label.setFont(font)
        self.top3Label.setObjectName("top3Label")
        self.top3VerticalLayout.addWidget(self.top3Label)

        # 2nd result
        self.top3Label_2 = QtWidgets.QLabel(self.top3VerticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        self.top3Label_2.setFont(font)
        self.top3Label_2.setObjectName("top3Label_2")
        self.top3VerticalLayout.addWidget(self.top3Label_2)

        # 3rd result
        self.top3Label_3 = QtWidgets.QLabel(self.top3VerticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        self.top3Label_3.setFont(font)
        self.top3Label_3.setObjectName("top3Label_3")
        self.top3VerticalLayout.addWidget(self.top3Label_3)

        # create top3Button
        self.top3Button = QtWidgets.QPushButton(self.centralwidget)
        self.top3Button.setGeometry(QtCore.QRect(20, 480, 241, 81))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        self.top3Button.setFont(font)
        self.top3Button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.top3Button.setObjectName("top3Button")
        self.top3Button.clicked.connect(self.top_3_clicked)

        # create maxGPA results
        self.maxGPAVerticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.maxGPAVerticalLayoutWidget.setGeometry(QtCore.QRect(270, 570, 351, 81))
        self.maxGPAVerticalLayoutWidget.setObjectName("maxGPAVerticalLayoutWidget")
        self.maxGPAVerticalLayout = QtWidgets.QVBoxLayout(self.maxGPAVerticalLayoutWidget)
        self.maxGPAVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.maxGPAVerticalLayout.setObjectName("maxGPAVerticalLayout")

        # create 120 points result
        self.maxGPA120Label = QtWidgets.QLabel(self.maxGPAVerticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        self.maxGPA120Label.setFont(font)
        self.maxGPA120Label.setObjectName("maxGPA120Label")
        self.maxGPAVerticalLayout.addWidget(self.maxGPA120Label)

        # create 160 points result
        self.maxGPA160Label = QtWidgets.QLabel(self.maxGPAVerticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        self.maxGPA160Label.setFont(font)
        self.maxGPA160Label.setObjectName("maxGPA160Label")
        self.maxGPAVerticalLayout.addWidget(self.maxGPA160Label)

        # create maxGPAButton
        self.maxGPAButton = QtWidgets.QPushButton(self.centralwidget)
        self.maxGPAButton.setGeometry(QtCore.QRect(20, 570, 241, 81))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        self.maxGPAButton.setFont(font)
        self.maxGPAButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.maxGPAButton.setObjectName("maxGPAButton")
        self.maxGPAButton.clicked.connect(self.max_gpa_clicked)

        # create targetGPA results
        # create top horizontal input
        self.targetGPAMainHorizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.targetGPAMainHorizontalLayoutWidget.setGeometry(QtCore.QRect(270, 660, 160, 31))
        self.targetGPAMainHorizontalLayoutWidget.setObjectName("targetGPAMainHorizontalLayoutWidget")
        self.targetGPAHorizontalLayoutWidget = QtWidgets.QHBoxLayout(self.targetGPAMainHorizontalLayoutWidget)
        self.targetGPAHorizontalLayoutWidget.setContentsMargins(0, 0, 0, 0)
        self.targetGPAHorizontalLayoutWidget.setObjectName("targetGPAHorizontalLayoutWidget")

        # create targetGPALabel for input
        self.targetGPALabel = QtWidgets.QLabel(self.targetGPAMainHorizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        self.targetGPALabel.setFont(font)
        self.targetGPALabel.setObjectName("targetGPALabel")
        self.targetGPAHorizontalLayoutWidget.addWidget(self.targetGPALabel)

        # create targetGPADoubleSpinBox
        self.targetGPADoubleSpinBox = QtWidgets.QDoubleSpinBox(self.targetGPAMainHorizontalLayoutWidget)
        self.targetGPADoubleSpinBox.setWrapping(False)
        self.targetGPADoubleSpinBox.setFrame(True)
        self.targetGPADoubleSpinBox.setReadOnly(False)
        self.targetGPADoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.targetGPADoubleSpinBox.setPrefix("")
        self.targetGPADoubleSpinBox.setSuffix("")
        self.targetGPADoubleSpinBox.setMinimum(0.0)
        self.targetGPADoubleSpinBox.setMaximum(100.0)
        self.targetGPADoubleSpinBox.setSingleStep(1)
        self.targetGPADoubleSpinBox.setObjectName("targetGPADoubleSpinBox")
        self.targetGPAHorizontalLayoutWidget.addWidget(self.targetGPADoubleSpinBox)

        # create bottom vertical output
        self.targetGPAMainVerticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.targetGPAMainVerticalLayoutWidget.setGeometry(QtCore.QRect(270, 690, 380, 41))
        self.targetGPAMainVerticalLayoutWidget.setObjectName("targetGPAMainVerticalLayoutWidget")
        self.targetGPAVerticalLayoutWidget = QtWidgets.QVBoxLayout(self.targetGPAMainVerticalLayoutWidget)
        self.targetGPAVerticalLayoutWidget.setContentsMargins(0, 0, 0, 0)
        self.targetGPAVerticalLayoutWidget.setObjectName("targetGPAVerticalLayoutWidget")

        # create avg120Label
        self.avg120Label = QtWidgets.QLabel(self.targetGPAMainVerticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(12)
        self.avg120Label.setFont(font)
        self.avg120Label.setObjectName("avg120Label")
        self.targetGPAVerticalLayoutWidget.addWidget(self.avg120Label)

        # create avg160Label
        self.avg160Label = QtWidgets.QLabel(self.targetGPAMainVerticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(12)
        self.avg160Label.setFont(font)
        self.avg160Label.setObjectName("avg160Label")
        self.targetGPAVerticalLayoutWidget.addWidget(self.avg160Label)

        # create targetGPAButton
        self.targetGPAButton = QtWidgets.QPushButton(self.centralwidget)
        self.targetGPAButton.setGeometry(QtCore.QRect(20, 660, 241, 81))
        font = QtGui.QFont()
        font.setFamily("David")
        font.setPointSize(14)
        self.targetGPAButton.setFont(font)
        self.targetGPAButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.targetGPAButton.setObjectName("targetGPAButton")
        self.targetGPAButton.clicked.connect(
            lambda: self.target_gpa_button_clicked(self.targetGPADoubleSpinBox.value()))

        # create menubar and statusbar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuOpen.addAction(self.actionOpen)
        self.menuOpen.addAction(self.actionSave)
        self.menubar.addAction(self.menuOpen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.myGPAcalcLabel.setText(_translate("MainWindow", "My-GPA-Calculator"))
        self.myCoursesLabel.setText(_translate("MainWindow", "My Courses"))
        self.totalPointsLabel.setText(_translate("MainWindow", "Total Points: 0"))
        self.gpaLabel.setText(_translate("MainWindow", "GPA: 0"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.pointsLabel.setText(_translate("MainWindow", "Points"))
        self.gradeLabel.setText(_translate("MainWindow", "Grade"))
        self.addCourseButton.setText(_translate("MainWindow", "Add"))
        self.addCourseButton.setStatusTip(_translate(
            "MainWindow", "Adds a course to the calculator"))
        self.featuresLabel.setText(_translate("MainWindow", "Features"))
        self.top3Label.setText(_translate("MainWindow", "1."))
        self.top3Label_2.setText(_translate("MainWindow", "2."))
        self.top3Label_3.setText(_translate("MainWindow", "3."))
        self.top3Button.setText(_translate("MainWindow", "Top 3 courses to improve"))
        self.top3Button.setStatusTip(_translate(
            "MainWindow", "Calculates the top 3 courses you should improve to improve your GPA"))
        self.maxGPA120Label.setText(_translate("MainWindow", "Max GPA for 120 points: "))
        self.maxGPA160Label.setText(_translate("MainWindow", "Max GPA for 160 points: "))
        self.maxGPAButton.setText(_translate("MainWindow", "Max GPA possible"))
        self.maxGPAButton.setStatusTip(_translate(
            "MainWindow", "Calculates maximum GPA you can possibly achieve without "
                          "improving any course"))
        self.targetGPAButton.setText(_translate("MainWindow", "Average for target GPA"))
        self.targetGPAButton.setStatusTip(_translate(
            "MainWindow", "Calculates the average grade you will need in the rest "
                          "of your courses to get to your target GPA"))
        self.targetGPALabel.setText(_translate("MainWindow", "Target GPA:"))
        self.avg120Label.setText(_translate("MainWindow", "Average grade needed for 120 points:"))
        self.avg160Label.setText(_translate("MainWindow", "Average grade needed for 160 points:"))
        self.nameAddLineEdit.setStatusTip(_translate("MainWindow", "Add course name input"))
        self.pointsSpinBox.setStatusTip(_translate("MainWindow", "Add course points input"))
        self.gradeSpinBox.setStatusTip(_translate("MainWindow", "Add course grade input"))
        self.targetGPADoubleSpinBox.setStatusTip(_translate("MainWindow", "Target GPA input"))
        self.menuOpen.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open a file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Saves a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    # when the addCourseButton is clicked
    def add_course_clicked(self, calculator):
        created_course = self.calculator.add_course(
            self.nameAddLineEdit.text(), self.pointsSpinBox.value(), self.gradeSpinBox.value())

        # in case of an error
        if type(created_course) is ErrorMsg:
            self.messageLabel.setText(created_course.msg)
            return

        # update text
        self.messageLabel.setText("Course ''%s'' was added!" % created_course.name)
        self.totalPointsLabel.setText("Total Points: %.1f" % self.calculator.total_points)
        self.gpaLabel.setText("GPA: %.2f" % self.calculator.gpa)

        # add course to UI
        # add check_box
        check_box = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        check_box.setText("")
        check_box.setChecked(True)
        check_box.setTristate(False)
        check_box.stateChanged.connect(
            lambda: self.set_checkbox_to_course(created_course, check_box.checkState()))
        self.gridLayout_2.addWidget(check_box, self.calculator.courses_count, 0, 1, 1)

        # add nameLineEdit
        name_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        name_line_edit.setText(created_course.name)
        name_line_edit.setReadOnly(True)
        name_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(name_line_edit, self.calculator.courses_count, 1, 1, 1)

        # add pointsLineEdit
        points_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        points_line_edit.setText(str(created_course.points))
        points_line_edit.setReadOnly(True)
        points_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(points_line_edit, self.calculator.courses_count, 2, 1, 1)

        # Add gradeLineEdit
        grade_line_edit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        grade_line_edit.setText(str(created_course.grade))
        grade_line_edit.setReadOnly(True)
        grade_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(grade_line_edit, self.calculator.courses_count, 3, 1, 1)

        # add deleteButton
        delete_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        delete_button.setText("Delete")
        delete_button.clicked.connect(lambda: self.remove_row(delete_button, created_course))
        self.gridLayout_2.addWidget(delete_button, self.calculator.courses_count, 4, 1, 1)

    # makes sure that the pointsSpinBox will have logical values
    def set_course_points(self, value):
        x = float(value)
        if not (x * 2).is_integer():
            self.pointsSpinBox.setValue(int(x))

    # connects a course to his checkbox
    def set_checkbox_to_course(self, course, value):
        course.enabled = value
        if course.enabled:
            text = "enabled!"
        else:
            text = "disabled!"
        self.messageLabel.setText("Course ''" + course.name + "'' is " + text)
        self.calculator.enable_disable_update(course)
        self.update_gpa_and_total_points_text()

    # when the deleteCourseButton is clicked
    def remove_row(self, sender, course):
        self.calculator.remove_course(course)

        index = self.gridLayout_2.indexOf(sender)
        row = self.gridLayout_2.getItemPosition(index)[0]
        for column in range(self.gridLayout_2.columnCount()):
            layout = self.gridLayout_2.itemAtPosition(row, column)
            if layout is not None:
                layout.widget().deleteLater()
                self.gridLayout_2.removeItem(layout)

        # update text
        self.messageLabel.setText("Course ''%s'' was deleted!" % course.name)
        self.update_gpa_and_total_points_text()

    # updates the GPA and Total Points text
    def update_gpa_and_total_points_text(self):
        self.totalPointsLabel.setText("Total Points: %.1f" % self.calculator.total_points)
        self.gpaLabel.setText("GPA: %.2f" % self.calculator.gpa)

    # when the maxGPAButton is clicked
    def max_gpa_clicked(self):
        self.calculator.calculate_max_gpa()
        if self.calculator.total_points <= 120:
            self.maxGPA120Label.setText("Max GPA for 120 points: %.2f" % self.calculator.max_gpa_120)
        else:
            self.maxGPA120Label.setText("Max GPA for 120 points: Total points over 120!")

        if self.calculator.total_points <= 160:
            self.maxGPA160Label.setText("Max GPA for 160 points: %.2f" % self.calculator.max_gpa_160)
        else:
            self.maxGPA160Label.setText("Max GPA for 160 points: Total points over 160!")

        self.messageLabel.setText("Max GPA possible was calculated!")

    # when the top3Button is clicked
    def top_3_clicked(self):
        results = self.calculator.top_3_to_improve()
        length = len(results)
        if not length:
            self.top3Label.setText("1.")
            self.top3Label_2.setText("2.")
            self.top3Label_3.setText("3.")

        elif length == 1:
            self.top3Label.setText("1.%s" % results[0].name)
            self.top3Label_2.setText("2.")
            self.top3Label_3.setText("3.")

        elif length == 2:
            self.top3Label.setText("1.%s" % results[0].name)
            self.top3Label_2.setText("2.%s" % results[1].name)
            self.top3Label_3.setText("3.")

        else:
            self.top3Label.setText("1.%s" % results[0].name)
            self.top3Label_2.setText("2.%s" % results[1].name)
            self.top3Label_3.setText("3.%s" % results[2].name)

        self.messageLabel.setText("Top 3 courses to improve calculated!")

    # when the targetGPAButton is clicked
    def target_gpa_button_clicked(self, target_gpa):
        output = self.calculator.target_gpa(target_gpa)
        if type(output[0]) == float:
            self.avg120Label.setText("Average grade needed for 120 points: %.2f" % output[0])
        else:
            self.avg120Label.setText("Average grade needed for 120 points: " + output[0])

        if type(output[1]) == float:
            self.avg160Label.setText("Average grade needed for 160 points: %.2f" % output[1])
        else:
            self.avg160Label.setText("Average grade needed for 120 points: " + output[1])

        self.messageLabel.setText("Average for target GPA was calculated!")
