from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QApplication, QLabel , qApp


# Стартовый диалог с выбором имени пользователя
class UserNameDialog(QDialog):
    def __init__(self, name=None):
        super().__init__()
        self.name = name
        self.ok_pressed = False

        self.setWindowTitle('Hi!')
        self.setFixedSize(175, 140)

        self.label = QLabel('username:', self)
        self.label.move(10, 10)
        self.label.setFixedSize(150, 10)

        self.client_name = QLineEdit(self)
        self.client_name.setFixedSize(154, 20)
        self.client_name.move(10, 30)
        if self.name:
            self.client_name.setText(name)

        self.label2 = QLabel('password:', self)
        self.label2.move(10, 60)
        self.label2.setFixedSize(150, 10)

        self.client_pwd = QLineEdit(self)
        self.client_pwd.setFixedSize(154, 20)
        self.client_pwd.move(10, 80)
        self.client_pwd.setEchoMode(QLineEdit.Password)


        self.btn_ok = QPushButton('Ok', self)
        self.btn_ok.setFixedSize(50, 25)
        self.btn_ok.move(10, 110)
        self.btn_ok.clicked.connect(self.click)

        self.btn_cancel = QPushButton('Cancel', self)
        self.btn_cancel.setFixedSize(50, 25)
        self.btn_cancel.move(90, 110)
        self.btn_cancel.clicked.connect(qApp.exit)

        self.show()

    # Обработчик кнопки ОК, если поле вводе не пустое, ставим флаг и завершаем приложение.
    def click(self):
        if self.client_name.text():
            self.ok_pressed = True
            qApp.exit()


if __name__ == '__main__':
    app = QApplication([])
    dial = UserNameDialog()
    app.exec_()