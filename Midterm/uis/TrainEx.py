import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from datetime import datetime
from Midterm.uis.StatisticMainWindow import Ui_MainWindow

class StatisticMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.showWindow()

    def showWindow(self):
        self.MainWindow.show()