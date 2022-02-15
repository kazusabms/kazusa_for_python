# coding:utf-8
# 作者:冬马kazusa

import maya.cmds as mc
import pymel.core as pmc
import sys
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
try:
    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets
except ImportError:
    from PyQt5 import QtGui
    from PyQt5 import QtCore
    from PyQt5 import QtWidgets

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr),QtWidgets.QWidget)



class TestDialog(QtWidgets.QDialog):
    def __init__(self,parent =maya_main_window()):
        super(TestDialog, self).__init__(parent)

        self.setWindowTitle("")
        self.resize(300,400)
        self.setWindowFlags(self.windowFlags()^QtCore.Qt.WindowContextHelpButtonHint)

        self.create_wigets()
        self.create_layouts()
        self.create_connections()



    def create_wigets(self):
        self.sel_view = QtWidgets.QListView()
        self.copy_skin_view = QtWidgets.QListView()
        self.slm = QtGui.QStringListModel()
        self.copy_sl_mesh = QtGui.QStringListModel()

        self.btn = QtWidgets.QPushButton("加载模型")
        self.btn2 = QtWidgets.QPushButton("加载copy skin模型")
        self.btn3 = QtWidgets.QPushButton("copy")
    def create_layouts(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.sel_view)


        left_layout = QtWidgets.QVBoxLayout()
        left_layout.addWidget(self.btn2)
        left_layout.addWidget(self.copy_skin_view)



        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(left_layout)

        m_layout = QtWidgets.QVBoxLayout(self)
        m_layout.addLayout(main_layout)
        m_layout.addWidget(self.btn3)



    def sl_mesh(self):
        self.ls_list = mc.ls(sl=1)
        self.slm.setStringList(self.ls_list)
        self.sel_view.setModel(self.slm)
        print(self.ls_list)
        return  self.ls_list
    def sl_copy_mesh(self):
        self.slCopyMeshList = mc.ls(sl=1)
        self.copy_sl_mesh.setStringList(self.slCopyMeshList)
        self.copy_skin_view.setModel(self.copy_sl_mesh)
        return self.slCopyMeshList
    def connect_mesh(self): #copy skin的功能暂时没写,先用关联替代
        for i1,i2 in zip(self.ls_list,self.slCopyMeshList):
            mc.connectAttr(i1+".translateX",i2+".translateX")


    def create_connections(self):
        self.btn.clicked.connect(self.sl_mesh)
        self.btn2.clicked.connect(self.sl_copy_mesh)
        self.btn3.clicked.connect(self.connect_mesh)


if __name__ == "__main__":
    try:
        d.close()
        d.deleteLater()           #判断窗口已经打开，如果打开了就删掉
    except:
        pass
    d = TestDialog()
    d.show()

