from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
os.system("cls")
import sys
class window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMaximumSize(1080,720)
        self.setMinimumSize(1080,720)
        self.txtedit=QLineEdit(self)
        self.txtedit.setFont(QFont("Calibri",14))
        self.txtedit.setGeometry(30,100,1000,400)
        self.menu=self.menuBar()
        self.menu.setFont(QFont("Consolas",20))
        self.file=self.menu.addMenu("&File")
        self.edit=self.menu.addMenu("&Edit")


        self.ochish=QAction(QIcon("C:\\Users\\User\\Downloads\\13.png"),"Faylni ochish",self) 
        self.ochish.setShortcut("Ctrl+O")
        self.font=QAction(QIcon("C:\\Users\\User\\Downloads\\14.png"),"Fontni o'zgartirish",self) 
        self.font.setShortcut("Ctrl+F")
        self.rang=QAction(QIcon("C:\\Users\\User\\Downloads\\15.png"),"Rangni o'zgartirish",self) 
        self.rang.setShortcut("Ctrl+R")
        self.yopish=QAction(QIcon("C\\Users\\User\\Downloads\\16.png"),"Dasturni yopish",self) 
        self.yopish.setShortcut("Ctrl+Q")
        self.file.setFont(QFont("Consolas",18)) 
        self.file.addAction(self.ochish)
        self.file.addAction(self.yopish)
        
        self.edit.setFont(QFont("Consolas",18))
        self.menyu1=self.edit.addMenu("Color and Font")
        
        self.menyu1.addActions([self.font,self.rang])
        
        self.edit.addMenu(self.menyu1)
        
        self.qbar=QToolBox(self)
        self.qbar.setGeometry(860,50,200,50)
        self.qbar.addAction(self.ochish)
        self.qbar.addAction(self.yopish)
        self.qbar.addAction(self.font)
        self.qbar.addAction(self.rang)
        
        self.ochish.triggered.connect(self.faylni_och)
        self.yopish.triggered.connect(self.quit)
        self.font.triggered.connect(self.font_change)
        self.rang.triggered.connect(self.color_change)

    def faylni_och(self):
        filename=QFileDialog.getOpenFileName(self,"Faylddan ma'lumot o'qish uchun ","D:")[0]
        
        f=open(filename,"rt")
        malumot=f.read()
        self.txtedit.setText(malumot)
        f.close()

    def quit(self):
        self.close()
    
    def font_change(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.txtedit.setFont(font)
        else:
            print("siz fontni tanlamdiz")

    def color_change(self):
        color=QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet("QMainWindow: {background-color: "+color.name()+";}")
            print(("QMainWindow: {background-color: "+color.name()+";}"))
            self.txtedit.setStyleSheet(f"color: {color.name()}")
            

app=QApplication(sys.argv)
oyna=window()
oyna.show()
sys.exit(app.exec_())
