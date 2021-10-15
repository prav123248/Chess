# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chess test.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 800, 800))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(0)
        all_position_labels = []
        
        colour = False
        for x in range(8):
            row = []
            
            for y in range(8):
                self.position = QtWidgets.QLabel(self.gridLayoutWidget)
                self.position.setText("Place " + str(x) + " " + str(y))
                if colour == True:
                    self.position.setStyleSheet("border: 1px solid black; background: gray;")
                    colour = False
                else:
                    self.position.setStyleSheet("border: 1px solid black;")
                    colour = True
                self.gridLayout.addWidget(self.position, x, y, 1, 1)
                

                row.append(self.position)
            all_position_labels.append(row)   

            if colour == True:
                colour = False
            else:
                colour = True
        del row
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def resizeEvent(self, event):
        print("trigger")
        super().resizeEvent(event)

        l = min(self.width(), self.height())
        center = self.rect().center()

        rect = QtCore.QRect(0, 0, l, l)
        rect.moveCenter(center)
        self.my_frame.setGeometry(rect)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
 
    
    MainWindow.show()

    sys.exit(app.exec_())

"""
        for x in range(8):
            for y in range(8):
                self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
                self.label_2.setObjectName("label_2")
                self.gridLayout.addWidget(self.label_2, x, y, 1, 1)

 def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        #self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))



"""