#Frederick Herzog
#HashCalc
from PyQt5 import QtCore, QtGui, QtWidgets
import hashes
import hashlib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 521)
        MainWindow.setWindowOpacity(0.9)
        MainWindow.setWindowIcon(QtGui.QIcon('icons/alg.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Vivaldi")
        font.setPointSize(60)
        font.setItalic(True)
        self.MainLabel.setFont(font)
        self.MainLabel.setObjectName("MainLabel")
        self.gridLayout.addWidget(self.MainLabel, 0, 0, 1, 2)
        self.mainIcon = QtWidgets.QLabel(self.centralwidget)
        self.mainIcon.setMaximumSize(QtCore.QSize(60, 50))
        self.mainIcon.setText("")
        self.mainIcon.setPixmap(QtGui.QPixmap("icons/alg.png"))
        self.mainIcon.setScaledContents(True)
        self.mainIcon.setObjectName("mainIcon")
        self.gridLayout.addWidget(self.mainIcon, 0, 2, 1, 1)
        self.encButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Nueva Std")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.encButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encButton.setIcon(icon)
        self.encButton.setObjectName("encButton")
        self.encButton.clicked.connect(self.popup2)
        self.gridLayout.addWidget(self.encButton, 1, 2, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 2, 2, 1, 1)
        self.exitButton.clicked.connect(self.quit)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 3)
        self.loadFileLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setItalic(False)
        self.loadFileLabel.setFont(font)
        self.loadFileLabel.setObjectName("loadFileLabel")
        self.gridLayout.addWidget(self.loadFileLabel, 4, 0, 1, 1)
        self.CalculateButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.CalculateButton.setFont(font)
        self.CalculateButton.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.CalculateButton.setObjectName("CalculateButton")
        self.CalculateButton.clicked.connect(self.populate)
        self.gridLayout.addWidget(self.CalculateButton, 4, 2, 1, 1)
        self.fileLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.gridLayout.addWidget(self.fileLineEdit, 5, 0, 1, 2)
        self.fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileButton.setObjectName("fileButton")
        self.fileButton.clicked.connect(self.file_dialogue)
        self.gridLayout.addWidget(self.fileButton, 6, 0, 1, 1)
        self.EnterStringLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setItalic(False)
        self.EnterStringLabel.setFont(font)
        self.EnterStringLabel.setObjectName("EnterStringLabel")
        self.gridLayout.addWidget(self.EnterStringLabel, 7, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 7, 1, 1, 2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 431, 408))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.md5Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.md5Label.setFont(font)
        self.md5Label.setObjectName("md5Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.md5Label)
        self.md5entry = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.md5entry.setObjectName("md5entry")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.md5entry)
        self.sha1Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sha1Label.setFont(font)
        self.sha1Label.setObjectName("sha1Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sha1Label)
        self.sha1entry = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sha1entry.setObjectName("sha1entry")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sha1entry)
        self.sha224Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sha224Label.setObjectName("sha224Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sha224Label)
        self.sha224entry = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sha224entry.setObjectName("sha224entry")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sha224entry)
        self.Sha256Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Sha256Label.setFont(font)
        self.Sha256Label.setObjectName("Sha256Label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Sha256Label)
        self.sha256entry = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sha256entry.setObjectName("sha256entry")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sha256entry)
        self.sha384Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sha384Label.setFont(font)
        self.sha384Label.setObjectName("sha384Label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sha384Label)
        self.sha384entry = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sha384entry.setObjectName("sha384entry")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sha384entry)
        self.sha512Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sha512Label.setFont(font)
        self.sha512Label.setObjectName("sha512Label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.sha512Label)
        self.sha512entry = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sha512entry.setObjectName("sha512entry")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sha512entry)
        font = QtGui.QFont()
        font.setPointSize(9)
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(14, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 8, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HashCalc"))
        self.MainLabel.setText(_translate("MainWindow", "HashCalc"))
        self.encButton.setText(_translate("MainWindow", "Encryption Tool"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.loadFileLabel.setText(_translate("MainWindow", "Load File:"))
        self.CalculateButton.setText(_translate("MainWindow", "Calculate"))
        self.fileButton.setText(_translate("MainWindow", "Browse..."))
        self.EnterStringLabel.setText(_translate("MainWindow", "Enter String:"))
        self.md5Label.setText(_translate("MainWindow", "md5"))
        self.sha1Label.setText(_translate("MainWindow", "sha1"))
        self.sha224Label.setText(_translate("MainWindow", "sha224"))
        self.Sha256Label.setText(_translate("MainWindow", "sha256"))
        self.sha384Label.setText(_translate("MainWindow", "sha384"))
        self.sha512Label.setText(_translate("MainWindow", "sha512"))

    def populate(self):
        try:
            textEntry = self.textEdit.toPlainText()
            if textEntry.isalnum():
                self.hash2Text(textEntry)
                self.clearEntries()
            else:
                myfile = self.filename[0]
                self.hashFile(myfile)
                self.clearEntries()
        except:
            self.popup()
            self.clearEntries()
       
    def hash2Text(self, tohash):
        self.md5entry.setText(hashes.md5(tohash).upper())
        self.sha1entry.setText(hashes.sha1(tohash).upper())
        self.sha224entry.setText(hashes.sha224(tohash).upper())
        self.sha256entry.setText(hashes.sha256(tohash).upper())
        self.sha384entry.setText(hashes.sha384(tohash).upper())
        self.sha512entry.setText(hashes.sha512(tohash).upper())

    def clearEntries(self):
        self.textEdit.setText('')
        self.fileLineEdit.setText('')
        self.filename = '' 

    def hashFile(self, file):
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha224 = hashlib.sha224()
        sha256 = hashlib.sha256()
        sha384 = hashlib.sha384()
        sha512 = hashlib.sha512()
        with open (file, 'rb') as f:
            chunk = 0
            while chunk != b'':
                chunk = f.read(1024)
                md5.update(chunk)
                sha1.update(chunk)
                sha224.update(chunk)
                sha256.update(chunk)
                sha384.update(chunk)
                sha512.update(chunk)
        self.md5entry.setText(md5.hexdigest().upper())
        self.sha1entry.setText(sha1.hexdigest().upper())
        self.sha224entry.setText(sha224.hexdigest().upper())
        self.sha256entry.setText(sha256.hexdigest().upper())
        self.sha384entry.setText(sha384.hexdigest().upper())
        self.sha512entry.setText(sha512.hexdigest().upper())

    def file_dialogue(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName()
        self.fileLineEdit.setText(self.filename[0])

    def quit(self):
        MainWindow.destroy()

    def popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setWindowIcon(QtGui.QIcon('icons/alg.png'))
        msg.setText("You must first enter a string or a file.")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x = msg.exec_()

    def popup2(self):
        msg = QtWidgets.QMessageBox()
       	msg.setWindowTitle("Crypto-Tools")
       	msg.setWindowIcon(QtGui.QIcon('icons/alg.png'))
        msg.setText("Be Patient. Cryptography tools are coming soon!")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

