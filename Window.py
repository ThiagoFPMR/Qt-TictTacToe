# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class TicTacToe (object):
    turn = False # False means O's turn and True means X's turn
    match = True # Stores if the match is still going or if it's over
    board = []
    def __init__(self, x, y): # player should also be a boolean that behaves in the same way as turn
        self.x = x
        self.y = y
        self.player = self.turn
        self.board.append(self)

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def check(cls, x, y, player):
        for _ in cls.board:
            if _.x == x and _.y == y and _.player == player:
                return True
        return False
    
    @classmethod
    def update (cls):
        for square in cls.board:
            if square.x == 1:
                if cls.check(2, square.y, square.player) and cls.check(3, square.y, square.player):
                    cls.match = False
                    if square.player == False:
                        return "O Wins!"
                    elif square.player == True:
                        return "X Wins!"
                elif square.y == 1:
                    if cls.check(2, 2, square.player) and cls.check(3, 3, square.player):
                        cls.match = False
                        if square.player == False:
                            return "O Wins!"
                        elif square.player == True:
                            return "X Wins!"
                elif square.y == 3:
                    if cls.check(2, 2, square.player) and cls.check(3, 1, square.player):
                        cls.match = False
                        if square.player == False:
                            return "O Wins!"
                        elif square.player == True:
                            return "X Wins!"
            if square.y == 1:
                if cls.check(square.x, 2, square.player) and cls.check(square.x, 3, square.player):
                    cls.match = False
                    if square.player == False:
                        return "O Wins!"
                    elif square.player == True:
                        return "X Wins!"
        if len(cls.board) >= 9:
            cls.match = False
            return "Draw!"
        cls.turn = (cls.turn - 1) * (-1)

    @classmethod
    def clear (cls):
        cls.match = True
        cls.board = []
        # cls.turn = False   # If this line is left commented, the winner goes first in the next match



class Ui_MainWIndow(object):
    claimed = []
    def setupUi(self, MainWIndow):
        MainWIndow.setObjectName("MainWIndow")
        MainWIndow.resize(1280, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWIndow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWIndow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(606, 74, 81, 131))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("imgs/logo.png"))
        self.Logo.setObjectName("Logo")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(470, 242, 100, 100))
        self.Button_1.setText("")
        self.Button_1.setIconSize(QtCore.QSize(100, 100))
        self.Button_1.setObjectName("Button_1")
        self.Button_1.clicked.connect(partial(self.clicked, self.Button_1, TicTacToe))
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(590, 242, 100, 100))
        self.Button_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_2.setText("")
        self.Button_2.setIconSize(QtCore.QSize(100, 100))
        self.Button_2.setObjectName("Button_2")
        self.Button_2.clicked.connect(partial(self.clicked, self.Button_2, TicTacToe))
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(710, 242, 100, 100))
        self.Button_3.setText("")
        self.Button_3.setIconSize(QtCore.QSize(100, 100))
        self.Button_3.setObjectName("Button_3")
        self.Button_3.clicked.connect(partial(self.clicked, self.Button_3, TicTacToe))
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(470, 362, 100, 100))
        self.Button_4.setText("")
        self.Button_4.setIconSize(QtCore.QSize(100, 100))
        self.Button_4.setObjectName("Button_4")
        self.Button_4.clicked.connect(partial(self.clicked, self.Button_4, TicTacToe))
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(590, 362, 100, 100))
        self.Button_5.setText("")
        self.Button_5.setIconSize(QtCore.QSize(100, 100))
        self.Button_5.setObjectName("Button_5")
        self.Button_5.clicked.connect(partial(self.clicked, self.Button_5, TicTacToe))
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(710, 362, 100, 100))
        self.Button_6.setText("")
        self.Button_6.setIconSize(QtCore.QSize(100, 100))
        self.Button_6.setObjectName("Button_6")
        self.Button_6.clicked.connect(partial(self.clicked, self.Button_6, TicTacToe))
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(470, 482, 100, 100))
        self.Button_7.setText("")
        self.Button_7.setIconSize(QtCore.QSize(100, 100))
        self.Button_7.setObjectName("Button_7")
        self.Button_7.clicked.connect(partial(self.clicked, self.Button_7, TicTacToe))
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(590, 482, 100, 100))
        self.Button_8.setText("")
        self.Button_8.setIconSize(QtCore.QSize(100, 100))
        self.Button_8.setObjectName("Button_8")
        self.Button_8.clicked.connect(partial(self.clicked, self.Button_8, TicTacToe))
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(710, 482, 100, 100))
        self.Button_9.setText("")
        self.Button_9.setIconSize(QtCore.QSize(100, 100))
        self.Button_9.setObjectName("Button_9")
        self.Button_9.clicked.connect(partial(self.clicked, self.Button_9, TicTacToe))
        self.RestartButton = QtWidgets.QPushButton(self.centralwidget)
        self.RestartButton.setGeometry(QtCore.QRect(541, 686, 214, 41))
        self.RestartButton.setObjectName("RestartButton")
        self.RestartButton.clicked.connect(partial(self.restart, TicTacToe))
        self.Player = QtWidgets.QLabel(self.centralwidget)
        self.Player.setGeometry(QtCore.QRect(590, 618, 41, 41))
        self.Player.setText("")
        self.Player.setPixmap(QtGui.QPixmap("imgs/o.png"))
        self.Player.setObjectName("Player")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(636, 629, 91, 31))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWIndow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWIndow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWIndow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWIndow)
        self.statusbar.setObjectName("statusbar")
        MainWIndow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWIndow)
        QtCore.QMetaObject.connectSlotsByName(MainWIndow)

    def retranslateUi(self, MainWIndow):
        _translate = QtCore.QCoreApplication.translate
        MainWIndow.setWindowTitle(_translate("MainWIndow", "Tic Tac Toe"))
        self.RestartButton.setText(_translate("MainWIndow", "Restart"))
        self.label_3.setText(_translate("MainWIndow", "\'s turn"))
    
    def clicked(self, button, TicTacToe):
        if not button in self.claimed and TicTacToe.match:
            if button == self.Button_1:
                move = TicTacToe(1, 1)
            if button == self.Button_2:
                move = TicTacToe(2, 1)
            if button == self.Button_3:
                move = TicTacToe(3, 1)
            if button == self.Button_4:
                move = TicTacToe(1, 2)
            if button == self.Button_5:
                move = TicTacToe(2, 2)
            if button == self.Button_6:
                move = TicTacToe(3, 2)
            if button == self.Button_7:
                move = TicTacToe(1, 3)
            if button == self.Button_8:
                move = TicTacToe(2, 3)
            if button == self.Button_9:
                move = TicTacToe(3, 3)

            self.claimed.append(button)

            if TicTacToe.turn == False:
                button.setIcon(QtGui.QIcon("imgs/o.png"))
            else:
                button.setIcon(QtGui.QIcon("imgs/x.png"))

            # TicTacToe.turn = (TicTacToe.turn - 1) * (-1)
            result = TicTacToe.update() 

            if not TicTacToe.match:
                    msg = QMessageBox()
                    msg.setWindowTitle("Game Over")
                    msg.setText(result)
                    msg.setStandardButtons(QMessageBox.Retry)
                    msg.setInformativeText('Click "Retry" to restart the game.')
                    msg.buttonClicked.connect(partial(self.restart, TicTacToe))
                    x = msg.exec_()             

            if TicTacToe.turn == False:
                self.Player.setPixmap(QtGui.QPixmap("imgs/o.png"))
                self.Player.setGeometry(QtCore.QRect(590, 618, 41, 41))
                self.Player.adjustSize()
            else:
                self.Player.setPixmap(QtGui.QPixmap("imgs/x.png"))
                self.Player.setGeometry(QtCore.QRect(575, 608, 41, 41))
                self.Player.adjustSize()
            
    # How to clear an Icon in QT -> button.setIcon(QIcon())
    
    def restart (self, TicTacToe):
        self.claimed = []
        self.Button_1.setIcon(QtGui.QIcon())
        self.Button_2.setIcon(QtGui.QIcon())
        self.Button_3.setIcon(QtGui.QIcon())
        self.Button_4.setIcon(QtGui.QIcon())
        self.Button_5.setIcon(QtGui.QIcon())
        self.Button_6.setIcon(QtGui.QIcon())
        self.Button_7.setIcon(QtGui.QIcon())
        self.Button_8.setIcon(QtGui.QIcon())
        self.Button_9.setIcon(QtGui.QIcon())
        TicTacToe.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWIndow = QtWidgets.QMainWindow()
    ui = Ui_MainWIndow()
    ui.setupUi(MainWIndow)
    MainWIndow.show()
    sys.exit(app.exec_())
