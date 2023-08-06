import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from client_dist.client.add_contact_window import AddContWindow


class Communicate(QObject):
    closeApp = pyqtSignal()


class ClientWindow(QMainWindow):
    '''
        Класс - основное окно пользователя.
        Содержит всю основную логику работы клиентского модуля.
        Конфигурация окна создана в QTDesigner и загружается из
        конвертированого файла main_window_conv.py
        '''
    def __init__(self, connector, username, cln_db=None):
        super().__init__()
        uic.loadUi('client/client.ui', self)
        # self.btnQuit.clicked.connect(qApp.quit)
        # self.actionExit.triggered.connect(qApp.quit)
        self.setWindowTitle(f'client {username}')
        self.actionAdd_Contact.triggered.connect(self.add_contact_window)
        self.btnAddCont.clicked.connect(self.add_contact_window)

        # self.actionDelete_Contact.triggered.connect(self.del_contact_window)
        # self.btnDelCont.clicked.connect(self.del_contact_window)

        self.btnClean.clicked.connect(self.clean_func)
        # self.listWidget.itemDoubleClicked.connect(self.add_hist)
        self.c = Communicate()
        self.connector = connector
        self.cln_db = cln_db
        self.username = username
        self.current_chat_key = None
        self.encryptor = None
        self.messages = QMessageBox()
        self.show()

    # def add_hist(self):
    # self.textEdit_2.append(self.listWidget.currentItem().text())
    def clean_func(self):
        self.textEdit_3.clear()

    def closeEvent(self, event):
        self.c.closeApp.emit()
        event.accept()

    def add_contact_window(self):
        global cont_window
        cont_window = AddContWindow(self.connector, self.username, self.cln_db, self)


'''
    def del_contact_window(self):
        global del_cont_window
        del_cont_window = DelContWindow(self.connector, self.username, self.cln_db, self)
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client_main_window = ClientWindow()
    client_main_window.listWidget.addItems(['user2', 'user3', 'user4'])

    app.exec_()
