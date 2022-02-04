from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda:self.callhw("11"))
        self.ui.pushButton_2.clicked.connect(lambda:self.callhw("12"))
        self.ui.pushButton_3.clicked.connect(lambda:self.callhw("13"))
        self.ui.pushButton_4.clicked.connect(lambda:self.callhw("14"))
        self.ui.pushButton_5.clicked.connect(lambda:self.callhw("21"))
        self.ui.pushButton_6.clicked.connect(lambda:self.callhw("22"))
        self.ui.pushButton_7.clicked.connect(lambda:self.callhw("23"))
        self.ui.pushButton_8.clicked.connect(lambda:self.callhw("31"))
        self.ui.pushButton_9.clicked.connect(lambda:self.callhw("32"))
        self.ui.pushButton_10.clicked.connect(lambda:self.callhw("33"))
        self.ui.pushButton_11.clicked.connect(lambda:self.callhw("34"))
        self.ui.pushButton_12.clicked.connect(lambda:self.callhw("41"))
        self.ui.pushButton_13.clicked.connect(lambda:self.callhw("42"))
        self.ui.pushButton_14.clicked.connect(lambda:self.callhw("43"))
        self.ui.pushButton_15.clicked.connect(lambda:self.callhw("44"))
    
    def callhw(self,str): 
        exec(open("hwpy/"+ str +".py").read())
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())


