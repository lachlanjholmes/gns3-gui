# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/qemu/ui/qemu_vm_configuration_page.ui'
#
# Created: Fri Oct  3 14:51:40 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_QemuVMConfigPageWidget(object):
    def setupUi(self, QemuVMConfigPageWidget):
        QemuVMConfigPageWidget.setObjectName(_fromUtf8("QemuVMConfigPageWidget"))
        QemuVMConfigPageWidget.resize(492, 399)
        self.verticalLayout = QtGui.QVBoxLayout(QemuVMConfigPageWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.uiQemutabWidget = QtGui.QTabWidget(QemuVMConfigPageWidget)
        self.uiQemutabWidget.setObjectName(_fromUtf8("uiQemutabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.uiQemuListLabel = QtGui.QLabel(self.tab)
        self.uiQemuListLabel.setObjectName(_fromUtf8("uiQemuListLabel"))
        self.gridLayout_4.addWidget(self.uiQemuListLabel, 2, 0, 1, 2)
        self.uiNameLineEdit = QtGui.QLineEdit(self.tab)
        self.uiNameLineEdit.setObjectName(_fromUtf8("uiNameLineEdit"))
        self.gridLayout_4.addWidget(self.uiNameLineEdit, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(263, 94, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 4, 1, 1, 2)
        self.uiQemuListComboBox = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiQemuListComboBox.sizePolicy().hasHeightForWidth())
        self.uiQemuListComboBox.setSizePolicy(sizePolicy)
        self.uiQemuListComboBox.setObjectName(_fromUtf8("uiQemuListComboBox"))
        self.gridLayout_4.addWidget(self.uiQemuListComboBox, 2, 2, 1, 1)
        self.uiConsolePortSpinBox = QtGui.QSpinBox(self.tab)
        self.uiConsolePortSpinBox.setMaximum(65535)
        self.uiConsolePortSpinBox.setObjectName(_fromUtf8("uiConsolePortSpinBox"))
        self.gridLayout_4.addWidget(self.uiConsolePortSpinBox, 3, 2, 1, 1)
        self.uiConsolePortLabel = QtGui.QLabel(self.tab)
        self.uiConsolePortLabel.setObjectName(_fromUtf8("uiConsolePortLabel"))
        self.gridLayout_4.addWidget(self.uiConsolePortLabel, 3, 0, 1, 2)
        self.uiNameLabel = QtGui.QLabel(self.tab)
        self.uiNameLabel.setObjectName(_fromUtf8("uiNameLabel"))
        self.gridLayout_4.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiRamLabel = QtGui.QLabel(self.tab)
        self.uiRamLabel.setObjectName(_fromUtf8("uiRamLabel"))
        self.gridLayout_4.addWidget(self.uiRamLabel, 1, 0, 1, 1)
        self.uiRamSpinBox = QtGui.QSpinBox(self.tab)
        self.uiRamSpinBox.setMinimum(32)
        self.uiRamSpinBox.setMaximum(65535)
        self.uiRamSpinBox.setProperty("value", 256)
        self.uiRamSpinBox.setObjectName(_fromUtf8("uiRamSpinBox"))
        self.gridLayout_4.addWidget(self.uiRamSpinBox, 1, 2, 1, 1)
        self.uiQemutabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.uiHdaDiskImageLabel = QtGui.QLabel(self.tab_3)
        self.uiHdaDiskImageLabel.setObjectName(_fromUtf8("uiHdaDiskImageLabel"))
        self.gridLayout_7.addWidget(self.uiHdaDiskImageLabel, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.uiHdaDiskImageLineEdit = QtGui.QLineEdit(self.tab_3)
        self.uiHdaDiskImageLineEdit.setObjectName(_fromUtf8("uiHdaDiskImageLineEdit"))
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageLineEdit)
        self.uiHdaDiskImageToolButton = QtGui.QToolButton(self.tab_3)
        self.uiHdaDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHdaDiskImageToolButton.setObjectName(_fromUtf8("uiHdaDiskImageToolButton"))
        self.horizontalLayout_8.addWidget(self.uiHdaDiskImageToolButton)
        self.gridLayout_7.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.uiHdbDiskImageLabel = QtGui.QLabel(self.tab_3)
        self.uiHdbDiskImageLabel.setObjectName(_fromUtf8("uiHdbDiskImageLabel"))
        self.gridLayout_7.addWidget(self.uiHdbDiskImageLabel, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.uiHdbDiskImageLineEdit = QtGui.QLineEdit(self.tab_3)
        self.uiHdbDiskImageLineEdit.setObjectName(_fromUtf8("uiHdbDiskImageLineEdit"))
        self.horizontalLayout_4.addWidget(self.uiHdbDiskImageLineEdit)
        self.uiHdbDiskImageToolButton = QtGui.QToolButton(self.tab_3)
        self.uiHdbDiskImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiHdbDiskImageToolButton.setObjectName(_fromUtf8("uiHdbDiskImageToolButton"))
        self.horizontalLayout_4.addWidget(self.uiHdbDiskImageToolButton)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(438, 257, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem1, 2, 0, 1, 2)
        self.uiQemutabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_7)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.uiAdaptersLabel = QtGui.QLabel(self.tab_7)
        self.uiAdaptersLabel.setObjectName(_fromUtf8("uiAdaptersLabel"))
        self.gridLayout_8.addWidget(self.uiAdaptersLabel, 0, 0, 1, 1)
        self.uiAdaptersSpinBox = QtGui.QSpinBox(self.tab_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdaptersSpinBox.sizePolicy().hasHeightForWidth())
        self.uiAdaptersSpinBox.setSizePolicy(sizePolicy)
        self.uiAdaptersSpinBox.setMinimum(1)
        self.uiAdaptersSpinBox.setMaximum(8)
        self.uiAdaptersSpinBox.setObjectName(_fromUtf8("uiAdaptersSpinBox"))
        self.gridLayout_8.addWidget(self.uiAdaptersSpinBox, 0, 1, 1, 1)
        self.uiAdapterTypesLabel = QtGui.QLabel(self.tab_7)
        self.uiAdapterTypesLabel.setObjectName(_fromUtf8("uiAdapterTypesLabel"))
        self.gridLayout_8.addWidget(self.uiAdapterTypesLabel, 1, 0, 1, 1)
        self.uiAdapterTypesComboBox = QtGui.QComboBox(self.tab_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdapterTypesComboBox.sizePolicy().hasHeightForWidth())
        self.uiAdapterTypesComboBox.setSizePolicy(sizePolicy)
        self.uiAdapterTypesComboBox.setObjectName(_fromUtf8("uiAdapterTypesComboBox"))
        self.gridLayout_8.addWidget(self.uiAdapterTypesComboBox, 1, 1, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(20, 261, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem2, 2, 1, 1, 1)
        self.uiQemutabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout = QtGui.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.uiLinuxBootGroupBox = QtGui.QGroupBox(self.tab_2)
        self.uiLinuxBootGroupBox.setObjectName(_fromUtf8("uiLinuxBootGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.uiLinuxBootGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.uiKernelImageLineEdit = QtGui.QLineEdit(self.uiLinuxBootGroupBox)
        self.uiKernelImageLineEdit.setObjectName(_fromUtf8("uiKernelImageLineEdit"))
        self.gridLayout_2.addWidget(self.uiKernelImageLineEdit, 1, 1, 1, 1)
        self.uiKernelCommandLineLabel = QtGui.QLabel(self.uiLinuxBootGroupBox)
        self.uiKernelCommandLineLabel.setObjectName(_fromUtf8("uiKernelCommandLineLabel"))
        self.gridLayout_2.addWidget(self.uiKernelCommandLineLabel, 2, 0, 1, 1)
        self.uiInitrdLabel = QtGui.QLabel(self.uiLinuxBootGroupBox)
        self.uiInitrdLabel.setObjectName(_fromUtf8("uiInitrdLabel"))
        self.gridLayout_2.addWidget(self.uiInitrdLabel, 0, 0, 1, 1)
        self.uiKernelImageLabel = QtGui.QLabel(self.uiLinuxBootGroupBox)
        self.uiKernelImageLabel.setObjectName(_fromUtf8("uiKernelImageLabel"))
        self.gridLayout_2.addWidget(self.uiKernelImageLabel, 1, 0, 1, 1)
        self.uiInitrdLineEdit = QtGui.QLineEdit(self.uiLinuxBootGroupBox)
        self.uiInitrdLineEdit.setObjectName(_fromUtf8("uiInitrdLineEdit"))
        self.gridLayout_2.addWidget(self.uiInitrdLineEdit, 0, 1, 1, 1)
        self.uiInitrdToolButton = QtGui.QToolButton(self.uiLinuxBootGroupBox)
        self.uiInitrdToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiInitrdToolButton.setObjectName(_fromUtf8("uiInitrdToolButton"))
        self.gridLayout_2.addWidget(self.uiInitrdToolButton, 0, 2, 1, 1)
        self.uiKernelImageToolButton = QtGui.QToolButton(self.uiLinuxBootGroupBox)
        self.uiKernelImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiKernelImageToolButton.setObjectName(_fromUtf8("uiKernelImageToolButton"))
        self.gridLayout_2.addWidget(self.uiKernelImageToolButton, 1, 2, 1, 1)
        self.uiKernelCommandLineEdit = QtGui.QLineEdit(self.uiLinuxBootGroupBox)
        self.uiKernelCommandLineEdit.setObjectName(_fromUtf8("uiKernelCommandLineEdit"))
        self.gridLayout_2.addWidget(self.uiKernelCommandLineEdit, 2, 1, 1, 2)
        self.gridLayout.addWidget(self.uiLinuxBootGroupBox, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.uiQemuOptionsLabel = QtGui.QLabel(self.groupBox)
        self.uiQemuOptionsLabel.setObjectName(_fromUtf8("uiQemuOptionsLabel"))
        self.gridLayout_3.addWidget(self.uiQemuOptionsLabel, 0, 0, 1, 1)
        self.uiQemuOptionsLineEdit = QtGui.QLineEdit(self.groupBox)
        self.uiQemuOptionsLineEdit.setObjectName(_fromUtf8("uiQemuOptionsLineEdit"))
        self.gridLayout_3.addWidget(self.uiQemuOptionsLineEdit, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 90, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.uiQemutabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.uiQemutabWidget)

        self.retranslateUi(QemuVMConfigPageWidget)
        self.uiQemutabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QemuVMConfigPageWidget)

    def retranslateUi(self, QemuVMConfigPageWidget):
        QemuVMConfigPageWidget.setWindowTitle(_translate("QemuVMConfigPageWidget", "QEMU VM configuration", None))
        self.uiQemuListLabel.setText(_translate("QemuVMConfigPageWidget", "Qemu binary:", None))
        self.uiConsolePortLabel.setText(_translate("QemuVMConfigPageWidget", "Console port:", None))
        self.uiNameLabel.setText(_translate("QemuVMConfigPageWidget", "VM name:", None))
        self.uiRamLabel.setText(_translate("QemuVMConfigPageWidget", "RAM:", None))
        self.uiRamSpinBox.setSuffix(_translate("QemuVMConfigPageWidget", " MB", None))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.tab), _translate("QemuVMConfigPageWidget", "General settings", None))
        self.uiHdaDiskImageLabel.setText(_translate("QemuVMConfigPageWidget", "Disk image (hda):", None))
        self.uiHdaDiskImageToolButton.setText(_translate("QemuVMConfigPageWidget", "Browse...", None))
        self.uiHdbDiskImageLabel.setText(_translate("QemuVMConfigPageWidget", "Disk image (hdb):", None))
        self.uiHdbDiskImageToolButton.setText(_translate("QemuVMConfigPageWidget", "Browse...", None))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.tab_3), _translate("QemuVMConfigPageWidget", "HDD", None))
        self.uiAdaptersLabel.setText(_translate("QemuVMConfigPageWidget", "Adapters:", None))
        self.uiAdapterTypesLabel.setText(_translate("QemuVMConfigPageWidget", "Type:", None))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.tab_7), _translate("QemuVMConfigPageWidget", "Network", None))
        self.uiLinuxBootGroupBox.setTitle(_translate("QemuVMConfigPageWidget", "Linux boot specific settings", None))
        self.uiKernelCommandLineLabel.setText(_translate("QemuVMConfigPageWidget", "Kernel command line:", None))
        self.uiInitrdLabel.setText(_translate("QemuVMConfigPageWidget", "Initial RAM disk (initrd):", None))
        self.uiKernelImageLabel.setText(_translate("QemuVMConfigPageWidget", "Kernel image:", None))
        self.uiInitrdToolButton.setText(_translate("QemuVMConfigPageWidget", "Browse...", None))
        self.uiKernelImageToolButton.setText(_translate("QemuVMConfigPageWidget", "Browse...", None))
        self.groupBox.setTitle(_translate("QemuVMConfigPageWidget", "Aditional settings", None))
        self.uiQemuOptionsLabel.setText(_translate("QemuVMConfigPageWidget", "Options:", None))
        self.uiQemutabWidget.setTabText(self.uiQemutabWidget.indexOf(self.tab_2), _translate("QemuVMConfigPageWidget", "Advanced settings", None))
