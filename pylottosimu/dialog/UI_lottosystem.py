# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lottosystem.ui'
#
# Created: Tue Oct 27 04:58:13 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 298))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 351, 211))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_max_draw = QtGui.QLabel(self.gridLayoutWidget)
        self.label_max_draw.setObjectName(_fromUtf8("label_max_draw"))
        self.gridLayout.addWidget(self.label_max_draw, 2, 0, 1, 1)
        self.spinBox_max_addit = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBox_max_addit.setObjectName(_fromUtf8("spinBox_max_addit"))
        self.gridLayout.addWidget(self.spinBox_max_addit, 7, 1, 1, 1)
        self.spinBox_addit_numbers = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBox_addit_numbers.setObjectName(_fromUtf8("spinBox_addit_numbers"))
        self.gridLayout.addWidget(self.spinBox_addit_numbers, 5, 1, 1, 1)
        self.label_max_addit = QtGui.QLabel(self.gridLayoutWidget)
        self.label_max_addit.setObjectName(_fromUtf8("label_max_addit"))
        self.gridLayout.addWidget(self.label_max_addit, 7, 0, 1, 1)
        self.spinBox_max_draw = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBox_max_draw.setObjectName(_fromUtf8("spinBox_max_draw"))
        self.gridLayout.addWidget(self.spinBox_max_draw, 2, 1, 1, 1)
        self.label_addit_numbers = QtGui.QLabel(self.gridLayoutWidget)
        self.label_addit_numbers.setObjectName(_fromUtf8("label_addit_numbers"))
        self.gridLayout.addWidget(self.label_addit_numbers, 5, 0, 1, 1)
        self.label_draw_numbers = QtGui.QLabel(self.gridLayoutWidget)
        self.label_draw_numbers.setObjectName(_fromUtf8("label_draw_numbers"))
        self.gridLayout.addWidget(self.label_draw_numbers, 3, 0, 1, 1)
        self.label_with_addit = QtGui.QLabel(self.gridLayoutWidget)
        self.label_with_addit.setObjectName(_fromUtf8("label_with_addit"))
        self.gridLayout.addWidget(self.label_with_addit, 4, 0, 1, 1)
        self.spinBox_draw_numbers = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBox_draw_numbers.setObjectName(_fromUtf8("spinBox_draw_numbers"))
        self.gridLayout.addWidget(self.spinBox_draw_numbers, 3, 1, 1, 1)
        self.check_with_addit = QtGui.QCheckBox(self.gridLayoutWidget)
        self.check_with_addit.setText(_fromUtf8(""))
        self.check_with_addit.setObjectName(_fromUtf8("check_with_addit"))
        self.gridLayout.addWidget(self.check_with_addit, 4, 1, 1, 1)
        self.label_name = QtGui.QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.gridLayout.addWidget(self.label_name, 1, 0, 1, 1)
        self.label_sep_addit_numbers = QtGui.QLabel(self.gridLayoutWidget)
        self.label_sep_addit_numbers.setObjectName(_fromUtf8("label_sep_addit_numbers"))
        self.gridLayout.addWidget(self.label_sep_addit_numbers, 6, 0, 1, 1)
        self.check_sep_addit_numbers = QtGui.QCheckBox(self.gridLayoutWidget)
        self.check_sep_addit_numbers.setText(_fromUtf8(""))
        self.check_sep_addit_numbers.setObjectName(_fromUtf8("check_sep_addit_numbers"))
        self.gridLayout.addWidget(self.check_sep_addit_numbers, 6, 1, 1, 1)
        self.combo_name = QtGui.QComboBox(self.gridLayoutWidget)
        self.combo_name.setEditable(True)
        self.combo_name.setObjectName(_fromUtf8("combo_name"))
        self.gridLayout.addWidget(self.combo_name, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(215, 250, 166, 22))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "System", None))
        self.label_max_draw.setText(_translate("Dialog", "Maximum number of draw", None))
        self.label_max_addit.setText(_translate("Dialog", "Maximum number of additional ", None))
        self.label_addit_numbers.setText(_translate("Dialog", "Additional numbers", None))
        self.label_draw_numbers.setText(_translate("Dialog", "Draw numbers", None))
        self.label_with_addit.setText(_translate("Dialog", "With additional number", None))
        self.label_name.setText(_translate("Dialog", "Name of the lotto system", None))
        self.label_sep_addit_numbers.setText(_translate("Dialog", "Separete numbers area", None))

