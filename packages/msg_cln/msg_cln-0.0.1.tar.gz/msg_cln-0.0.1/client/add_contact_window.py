import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, qApp, QApplication, QMainWindow, QDialog
from client_dist.common.constant import ADD_CONTACT, USERS_REQUEST
from client_dist.common.messanger import srv_database_request


class AddContWindow(QDialog):
    def __init__(self, connector, username, cln_db, main_wind):
        super().__init__()
        uic.loadUi('client/add_contact.ui', self)
        self.btnCancel.clicked.connect(self.close)
        #self.actionExit.triggered.connect(qApp.quit)
        self.btnAdd.clicked.connect(self.add_cont_func)
        self.connector = connector
        self.cln_db = cln_db
        self.username = username
        self.main_wind = main_wind
        self.show()
        known_user_list = cln_db.get_users()
        self.comboBox.addItems(known_user_list)

    def add_cont_func(self):
        cont_name = self.comboBox.currentText()
        self.cln_db.upd_contact(cont_name, 'add')
        # rec_type = REMOVE_CONTACT
        resp = srv_database_request(self.connector, request_type=ADD_CONTACT, username=self.username,
                                    contact_name=cont_name)
        if resp == 'OK':
            self.main_wind.listWidget.addItem(cont_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddContWindow()
    app.exec_()