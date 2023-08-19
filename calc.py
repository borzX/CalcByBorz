import sys
import math
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QWidget,  QTableWidget,
    QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox




class MainWindow(QMainWindow):
    def __init__(self):
            super(MainWindow, self).__init__()
            self.setFixedSize(425, 555)
            self.setWindowTitle('Калькулятор')
            uic.loadUi('main_form.ui', self)
            
            #этот файл в одной папке с ui
            self.lineEdit.setPlaceholderText("0")
            self.pushButton_3.clicked.connect(self.exx)
            self.pushButton.clicked.connect(self.input_value)
            self.one.clicked.connect(lambda: self.Num_bat(1))
            self.two.clicked.connect(lambda: self.Num_bat(2))
            self.three.clicked.connect(lambda: self.Num_bat(3))
            self.sum_but.clicked.connect(self.deystvie_sum)
            self.result.clicked.connect(self.resultat)
            self.erase.clicked.connect(self.eraser)
            self.cleare.clicked.connect(self.clearer)

    

    def temp(self):
        self.lineEdit.setText("0")
        tmp = int(input(self.lineEdit()))



    def exx(self):
        sys.exit()

    def eraser(self):
        a = self.lineEdit.text()
        a = a[:-1]
        self.lineEdit.setText(a)

    def clearer(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        

    def resultat(self):
        self.lineEdit.setText(self.lineEdit_2.text())
        #self.lineEdit_2.setText(self.lineEdit.text())
        #self.lineEdit.clear()
         

    def input_value(self):
        self.lineEdit.setText("Привет")
    
    
    def Num_bat(self, num):
        value = str(num)
        self.lineEdit.setText(self.lineEdit.text()+value)
        

    def deystvie_sum(self):
        
        tmp = self.lineEdit.text()
        if tmp.isdigit()==False:
            tmp = 0
        
        tmp_2 = self.lineEdit_2.text()
        if tmp_2.isdigit()==False:
            tmp_2 = 0
       
        self.lineEdit.clear()
        sum_res = int(tmp)+int(tmp_2)

        return self.lineEdit_2.setText(str(sum_res))

        
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
