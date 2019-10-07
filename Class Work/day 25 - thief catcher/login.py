
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
import smtplib
from email.message import EmailMessage
import config
import cv2
Email = config.EMAIL_ADDRESS
password = config.EMAIL_PASSWORD


import datetime



class Ui_MainWindow(object,):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(100%, 100%)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 110, 421, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.loginButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.loginButton.setObjectName("loginButton")
        self.gridLayout.addWidget(self.loginButton, 2, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.u_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.u_label.setObjectName("u_label")
        self.gridLayout.addWidget(self.u_label, 0, 0, 1, 1)
        self.p_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.p_label.setObjectName("p_label")
        self.gridLayout.addWidget(self.p_label, 1, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 60, 161, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Log in"))
        self.u_label.setText(_translate("MainWindow", "Username"))
        self.p_label.setText(_translate("MainWindow", "Password"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.label_3.setText(_translate("MainWindow", "Login Form"))
        self.loginButton.clicked.connect(self.loginFun)

    def sendEmail(self, text,photo):

        msg = EmailMessage()
        msg['Subject'] = 'Check out Bronx as a puppy!'
        msg['From'] = config.EMAIL_ADDRESS
        msg['To'] = 'gargtushar72@gmail.com'

        msg.set_content('This is a plain text email')
        msg.add_alternative(f"""\
        <!DOCTYPE html>
        <html>
            <body>
                <h1 style="color:SlateGray;">{text}</h1>
                <img src=''>

            </body>
        </html>
        """, subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
            smtp.send_message(msg)

    #Capturing Thief
    def capturePhoto(self):
        date_string = datetime.datetime.now().strftime("%Y%m%d%H%M")
        print(date_string)
        cap = cv2.VideoCapture(0)
        ret, photo = cap.read()
        #cv2.imwrite(config.PHOTOPATH+date_string+".jpg",photo)
        #cv2.imwrite("thiefphoto/"+date_string+".jpg",photo)
        cap.release()
        print("Captured...")
        return date_string+".jpg"

    def loginFun(self):
        u = self.username.text()
        p = self.password.text()

        if u == "Admin" and p == "123":
            print("Login Successful!!")
        else:
            photo = self.capturePhoto()
            self.sendEmail("Koi pange le raha hai apke laptop ke saath",photo)
            print("Wrong User")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
