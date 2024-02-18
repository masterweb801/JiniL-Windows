import ctypes
import time
import threading
from sys import argv
from PyQt5 import QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://jinil.rf.gd/"))
        
        self.pmap = QtGui.QPixmap("./sps.png")
        self.splash_label = QLabel()
        self.splash_label.setPixmap(self.pmap)
        self.splash_label.setScaledContents(True)
        
        self.setCentralWidget(self.splash_label)
        t = threading.Thread(target=self.label_close)
        t.start()

        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon("./icon.jpg"))

    def label_close(self):
        time.sleep(2)
        self.splash_label.close()
        self.setCentralWidget(self.browser)


app = QApplication(argv)
QApplication.setApplicationName("JiniL")
QApplication.setWindowIcon(QtGui.QIcon("./icon.jpg"))

my_appid = 'logic_realm.jinil.1.2' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_appid)

window = MainWindow()
app.exec_()
