from os.path import join
from PyQt4 import QtCore, QtGui

class DlgShowDrawing(QtGui.QDialog):
    """Show the numbers in a dialog box"""
    def __init__(self, draw_number, highest_number):
        QtGui.QDialog.__init__(self)
        
        self.setWindowIcon(QtGui.QIcon(join("misc", "icon.ico")))
        self.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)

        self.boxLayout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom, self)
                
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(0)
               
        self.Btn_Numerary_1to49 = []
        for button in xrange(highest_number):
            self.Btn_Numerary_1to49.append(QtGui.QPushButton(self))
        for button in xrange(highest_number):
            self.Btn_Numerary_1to49[button].setMaximumSize(QtCore.QSize(58, 58))
            self.gridLayout.addWidget(self.Btn_Numerary_1to49[button], int(button / 7),  int(button % 7), 1, 1)
            self.Btn_Numerary_1to49[button].setAutoFillBackground(True)
            self.Btn_Numerary_1to49[button].setText(QtGui.QApplication.translate("MainWindow", str(button + 1), 
             None, QtGui.QApplication.UnicodeUTF8))                                               
        
        for button in xrange(highest_number):
            if button + 1 in draw_number:
                self.Btn_Numerary_1to49[button].setFlat(False)
            else:
                self.Btn_Numerary_1to49[button].setFlat(True)
       
        self.setWindowTitle("Show Drawing")

        self.boxLayout.addLayout(self.gridLayout)
        self.boxLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)


