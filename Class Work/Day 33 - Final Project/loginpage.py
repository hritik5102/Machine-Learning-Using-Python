
from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
from email.message import EmailMessage
import cv2
import imghdr, sys,csv
import datetime 
import keyboard
import os,socket

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


class Ui_MainWindow(object):


    def precheck(self):
        try:
            socket.create_connection(("www.google.com",80))
            print("Internet working sending emails")
            
            src = config['PHOTOPATH']
            des = config['ARCHIVEPATH']
            allphotos = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src,f))]
            
            print(allphotos)
            text = "Intruder Detected!"
            
            for single in allphotos:
                if self.sendEmail(text,single):
                    print("Email sent for {} file".format(single))
                else:
                    print("Email nahi hui bhai ...")
                    break
            print("All Photos has been sent ...")

            
            #if not os.path.isdir(des):
            #    os.mkdir(os.path.join(dir))




        except:
             print("Intenet not working")    





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1364, 896)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(499, 230, 351, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(524, 170, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1364, 26))
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
        self.pushButton_2.setText(_translate("MainWindow", "LOGIN"))
        self.label_2.setText(_translate("MainWindow", "USERID"))
        self.label_3.setText(_translate("MainWindow", "PASSWORD"))
        self.pushButton_3.setText(_translate("MainWindow", "CLEAR"))
        
        self.pushButton.setText(_translate("MainWindow", "FORGET"))
        self.pushButton_2.setVisible(False)
        
        self.label.setText(_translate("MainWindow", "     LOGIN PAGE      "))
        self.pushButton_2.clicked.connect(self.loginFun)
        self.pushButton.clicked.connect(self.forgetfun)

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
        try:

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(config["EMAIL_ADDRESS"], config["EMAIL_PASSWORD"])
                smtp.send_message(msg)
                src = config['PHOTOPATH']
                des = config['ARCHIVEPATH']
                try:
                    os.rename(os.path.join(src,photo),os.path.join(des,photo))
                except:
                    print("Error occured while moving the file")    
                return True
        except:
            return False

        return False      


    def checkFace(self):
        
        cap = cv2.VideoCapture(0)
        det = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        while cap.isOpened():

            ret, photo = cap.read()
            count = 0

            if ret:
                faces = det.detectMultiScale(photo,1.2,5,minSize = (100,100),flags = cv2.CASCADE_SCALE_IMAGE)

                for (x,y,w,h) in faces:
                    count = 1
                    break
                
                if count == 1:
                    date_string = datetime.datetime.now().strftime("%Y%m%d%H%M")
                    cv2.imwrite(config["PHOTOPATH"]+date_string+".jpg",photo)
                    self.pushButton_2.setVisible(True)
                    return True




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
    
    #login function
    def loginFun(self):
        
        u = self.lineEdit.text()
        p = self.lineEdit_2.text()
        if u == config["USERNAME"] and p == config["PASSWORD"]:
            print("Login Successful!!")
            exit()
        else:
            photo = self.capturePhoto()
            self.sendEmail("Koi pange le raha hai apke laptop ke saath", photo)
            print("Wrong User! Email Sent")

    def forgetfun(self):
        photo=self.capturePhoto()
        self.sendEmail("username:{}   password:{}".format(config["USERNAME"] ,config["PASSWORD"]),photo)
        print("forget sucessfull")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    MainWindow.
    MainWindow.showMaximized()
    keyboard.block_key('Shift')
    keyboard.block_key('win')
    keyboard.block_key('alt')
    MainWindow.show()
    ui.checkFace()
    ui.precheck()
    sys.exit(app.exec_())
