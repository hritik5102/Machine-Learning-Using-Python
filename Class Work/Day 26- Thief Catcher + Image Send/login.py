#Basic Imports
from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
from email.message import EmailMessage
import cv2
import imghdr, sys,csv
import datetime
#Imports End


# Reading CSV File
config ={}
config_file_path = sys.argv[1]
try:
    data = csv.DictReader(open(config_file_path))
except:
    print("Config File Not found.... ")
    exit()

#Converting csv to dict obj
for one in data:
    for key in one.keys():
        config[key] = one[key]
    break

#print(config)

# End - Reading CSV File

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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

    def sendEmail(self, text, photo):

        msg = EmailMessage()

        msg['Subject'] = 'Intruder Alert!'
        msg['From'] = config["EMAIL_ADDRESS"]
        msg['To'] = config["RECEIVEREMAIL"]

        msg.set_content(text)

        print(config["PHOTOPATH"]+photo)

        with open(config["PHOTOPATH"]+photo,'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
            #print(file_type)

        msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

        #msg.add_alternative()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(config["EMAIL_ADDRESS"], config["EMAIL_PASSWORD"])
            smtp.send_message(msg)


    #Capturing Thief
    def capturePhoto(self):
        date_string = datetime.datetime.now().strftime("%Y%m%d%H%M")
        print(date_string)
        cap = cv2.VideoCapture(0)
        ret, photo = cap.read()
        cv2.imwrite(config["PHOTOPATH"]+date_string+".jpg",photo)
        cap.release()
        print("Captured...")
        return date_string+".jpg"

    def loginFun(self):
        u = self.username.text()
        p = self.password.text()

        if u == config["USERNAME"] and p == config["PASSWORD"]:
            print("Login Successful!!")
        else:
            photo = self.capturePhoto()
            self.sendEmail("Koi pange le raha hai apke laptop ke saath", photo)
            print("Wrong User! Email Sent")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
