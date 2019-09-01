#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time

import resources_rc

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QLabel, QGridLayout, QPushButton, QWidget,
                             QApplication, QSplashScreen)

from Game import Game


class MainWindow(QWidget):
    game = Game()

    def __init__(self):
        super().__init__()
        self.first = 0
        self.second = 0
        self.win = False

        self.initUI()

    def initUI(self):
        self.screen = QSplashScreen(QPixmap(':images/wp.png'))
        self.screen.show()

        grid = QGridLayout()
        self.setLayout(grid)

        self.restart = QPushButton('restart')
        self.gamer1 = QLabel('0')
        self.gamer2 = QLabel('0')

        self.field1 = QPushButton()
        self.field1.setIcon(QIcon(':images/field.png'))
        self.field1.setStyleSheet("background-color: black")
        self.field1.setIconSize(QSize(50, 50))
        grid.addWidget(self.field1, 0, 0)

        self.field2 = QPushButton()
        self.field2.setIcon(QIcon(':images/field.png'))
        self.field2.setStyleSheet("background-color: black")
        self.field2.setIconSize(QSize(50, 50))
        grid.addWidget(self.field2, 0, 1)

        self.field3 = QPushButton()
        self.field3.setIcon(QIcon(':images/field.png'))
        self.field3.setStyleSheet("background-color: black")
        self.field3.setIconSize(QSize(50, 50))
        grid.addWidget(self.field3, 0, 2)
        grid.addWidget(QLabel('first gamer:'), 0, 3)
        grid.addWidget(self.gamer1, 0, 4)

        self.field4 = QPushButton()
        self.field4.setIcon(QIcon(':images/field.png'))
        self.field4.setStyleSheet("background-color: black")
        self.field4.setIconSize(QSize(50, 50))
        grid.addWidget(self.field4, 1, 0)

        self.field5 = QPushButton()
        self.field5.setIcon(QIcon(':images/field.png'))
        self.field5.setStyleSheet("background-color: black")
        self.field5.setIconSize(QSize(50, 50))
        grid.addWidget(self.field5, 1, 1)

        self.field6 = QPushButton()
        self.field6.setIcon(QIcon(':images/field.png'))
        self.field6.setStyleSheet("background-color: black")
        self.field6.setIconSize(QSize(50, 50))
        grid.addWidget(self.field6, 1, 2)
        grid.addWidget(QLabel('second gamer:'), 1, 3)
        grid.addWidget(self.gamer2, 1, 4)

        self.field7 = QPushButton()
        self.field7.setIcon(QIcon(':images/field.png'))
        self.field7.setStyleSheet("background-color: black")
        self.field7.setIconSize(QSize(50, 50))
        grid.addWidget(self.field7, 2, 0)

        self.field8 = QPushButton()
        self.field8.setIcon(QIcon(':images/field.png'))
        self.field8.setStyleSheet("background-color: black")
        self.field8.setIconSize(QSize(50, 50))
        grid.addWidget(self.field8, 2, 1)

        self.game_next = QPushButton('next')

        self.field9 = QPushButton()
        self.field9.setIcon(QIcon(':images/field.png'))
        self.field9.setStyleSheet("background-color: black")
        self.field9.setIconSize(QSize(50, 50))
        grid.addWidget(self.field9, 2, 2)
        grid.addWidget(self.restart, 2, 3)
        grid.addWidget(self.game_next, 2, 4)

        self.field1.clicked.connect(self.field1Cliced)
        self.field2.clicked.connect(self.field2Cliced)
        self.field3.clicked.connect(self.field3Cliced)
        self.field4.clicked.connect(self.field4Cliced)
        self.field5.clicked.connect(self.field5Cliced)
        self.field6.clicked.connect(self.field6Cliced)
        self.field7.clicked.connect(self.field7Cliced)
        self.field8.clicked.connect(self.field8Cliced)
        self.field9.clicked.connect(self.field9Cliced)

        self.restart.clicked.connect(self.restartGame)
        self.game_next.clicked.connect(self.clearFields)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Tic Tac Toe')
        time.sleep(17)
        self.show()
        self.screen.finish(self)

    def restartGame(self):
        self.clearFields()
        self.first = 0
        self.second = 0
        self.gamer1.setText(str(self.first))
        self.gamer2.setText(str(self.second))

    def clearFields(self):
        self.game.next_game()
        self.win = False
        self.field1.setIcon(QIcon(':images/field.png'))
        self.field2.setIcon(QIcon(':images/field.png'))
        self.field3.setIcon(QIcon(':images/field.png'))
        self.field4.setIcon(QIcon(':images/field.png'))
        self.field5.setIcon(QIcon(':images/field.png'))
        self.field6.setIcon(QIcon(':images/field.png'))
        self.field7.setIcon(QIcon(':images/field.png'))
        self.field8.setIcon(QIcon(':images/field.png'))
        self.field9.setIcon(QIcon(':images/field.png'))

    def checkWin(self):
        if self.game.getOrder() > 4:
            if self.game.check_win() == 1:
                print("first win!!")
                self.win = True
                self.first += 1
                self.gamer1.setText(str(self.first))
            elif self.game.check_win() == 2:
                print("second win!!")
                self.win = True
                self.second += 1
                self.gamer2.setText(str(self.second))
            elif self.game.getOrder() == 9 and self.game.check_win() == 0:
                print("no winners")
                self.win = True

    def setField(self):
        if self.game.getOrder() % 2 != 0:
            return QIcon(':images/X.png')
        else:
            return QIcon(':images/O.png')

    def field1Cliced(self):
        if self.win:
            return
        self.game.set_input(0, 0)
        self.field1.setIcon(self.setField())
        self.checkWin()

    def field2Cliced(self):
        if self.win:
            return
        self.game.set_input(0, 1)
        self.field2.setIcon(self.setField())
        self.checkWin()

    def field3Cliced(self):
        if self.win:
            return
        self.game.set_input(0, 2)
        self.field3.setIcon(self.setField())
        self.checkWin()

    def field4Cliced(self):
        if self.win:
            return
        self.game.set_input(1, 0)
        self.field4.setIcon(self.setField())
        self.checkWin()

    def field5Cliced(self):
        if self.win:
            return
        self.game.set_input(1, 1)
        self.field5.setIcon(self.setField())
        self.checkWin()

    def field6Cliced(self):
        if self.win:
            return
        self.game.set_input(1, 2)
        self.field6.setIcon(self.setField())
        self.checkWin()

    def field7Cliced(self):
        if self.win:
            return
        self.game.set_input(2, 0)
        self.field7.setIcon(self.setField())
        self.checkWin()

    def field8Cliced(self):
        if self.win:
            return
        self.game.set_input(2, 1)
        self.field8.setIcon(self.setField())
        self.checkWin()

    def field9Cliced(self):
        if self.win:
            return
        self.game.set_input(2, 2)
        self.field9.setIcon(self.setField())
        self.checkWin()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())