import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, qApp, QApplication, QMainWindow, QDialog

from common.constant import REMOVE_CONTACT, GET_CONTACTS
from common.messanger import srv_database_request


class DelContWindow(QDialog):
    def __init__(self, connector, username, cln_db, main_wind):
        super().__init__()
        uic.loadUi('del_contact.ui', self)
        self.btnCancel.clicked.connect(self.close)
        # self.actionExit.triggered.connect(qApp.quit)
        self.btnDel.clicked.connect(self.del_cont_func)
        self.connector = connector
        self.cln_db = cln_db
        self.username = username
        self.main_wind = main_wind
        self.show()
        #users_list = cln_db.get_contacts()
        #for x in range(self.main_wind.listWidget.count()):
            #users_list.append(self.main_wind.listWidget.item(x).text())
        #self.comboBox.addItems(users_list)

    #users_list = srv_database_request(self.connector, self.username, GET_CONTACTS)


    def del_cont_func(self):
        cont_name = self.comboBox.currentText()
        self.cln_db.upd_contact(cont_name, 'del')
        print(cont_name)
        # rec_type = REMOVE_CONTACT
        resp = srv_database_request(self.connector, request_type=REMOVE_CONTACT, username=self.username,
                                    contact_name=cont_name)
        if resp == 'OK':
            # self.main_wind.listWidget.addItem(cont_name)
            self.main_wind.listWidget.clear()
            self.main_wind.listWidget.addItems(srv_database_request(self.connector, self.username, GET_CONTACTS))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DelContWindow()
    app.exec_()
