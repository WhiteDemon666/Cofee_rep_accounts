import sys
import sqlite3

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QDialogButtonBox, QFileDialog, QMessageBox, QTableWidgetItem, QVBoxLayout
from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QHBoxLayout, QInputDialog, QMainWindow, QApplication
from PyQt5.QtGui import QPixmap


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 325)
        Form.setMinimumSize(QtCore.QSize(400, 325))
        Form.setMaximumSize(QtCore.QSize(400, 325))
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 381, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sign = QtWidgets.QWidget()
        self.tab_sign.setObjectName("tab_sign")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_sign)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 120, 221, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.sign_password_layot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.sign_password_layot.setContentsMargins(0, 0, 0, 0)
        self.sign_password_layot.setObjectName("sign_password_layot")
        self.sign_password_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sign_password_text.setObjectName("sign_password_text")
        self.sign_password_layot.addWidget(self.sign_password_text)
        self.sign_password_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.sign_password_input.setObjectName("sign_password_input")
        self.sign_password_layot.addWidget(self.sign_password_input)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_sign)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 70, 221, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.sign_login_layot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.sign_login_layot.setContentsMargins(0, 0, 0, 0)
        self.sign_login_layot.setObjectName("sign_login_layot")
        self.sign_login_text = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.sign_login_text.setObjectName("sign_login_text")
        self.sign_login_layot.addWidget(self.sign_login_text)
        self.sign_login_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.sign_login_input.setObjectName("sign_login_input")
        self.sign_login_layot.addWidget(self.sign_login_input)
        self.sign_button = QtWidgets.QPushButton(self.tab_sign)
        self.sign_button.setGeometry(QtCore.QRect(80, 170, 221, 31))
        self.sign_button.setObjectName("sign_button")
        self.sign_error = QtWidgets.QLabel(self.tab_sign)
        self.sign_error.setGeometry(QtCore.QRect(80, 210, 221, 31))
        self.sign_error.setObjectName("sign_error")
        self.tabWidget.addTab(self.tab_sign, "")
        self.tab_registration = QtWidgets.QWidget()
        self.tab_registration.setObjectName("tab_registration")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_registration)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 100, 221, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.reg_password_layot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.reg_password_layot.setContentsMargins(0, 0, 0, 0)
        self.reg_password_layot.setObjectName("reg_password_layot")
        self.reg_password_text = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.reg_password_text.setObjectName("reg_password_text")
        self.reg_password_layot.addWidget(self.reg_password_text)
        self.reg_password_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.reg_password_input.setObjectName("reg_password_input")
        self.reg_password_layot.addWidget(self.reg_password_input)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_registration)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 150, 221, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.reg_email_layot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.reg_email_layot.setContentsMargins(0, 0, 0, 0)
        self.reg_email_layot.setObjectName("reg_email_layot")
        self.reg_emal_text = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.reg_emal_text.setObjectName("reg_emal_text")
        self.reg_email_layot.addWidget(self.reg_emal_text)
        self.reg_email_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.reg_email_input.setObjectName("reg_email_input")
        self.reg_email_layot.addWidget(self.reg_email_input)
        self.reg_button = QtWidgets.QPushButton(self.tab_registration)
        self.reg_button.setGeometry(QtCore.QRect(20, 200, 221, 31))
        self.reg_button.setObjectName("reg_button")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_registration)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 50, 221, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.reg_login_layot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.reg_login_layot.setContentsMargins(0, 0, 0, 0)
        self.reg_login_layot.setObjectName("reg_login_layot")
        self.reg_login_text = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.reg_login_text.setObjectName("reg_login_text")
        self.reg_login_layot.addWidget(self.reg_login_text)
        self.reg_login_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.reg_login_input.setObjectName("reg_login_input")
        self.reg_login_layot.addWidget(self.reg_login_input)
        self.reg_error_login = QtWidgets.QLabel(self.tab_registration)
        self.reg_error_login.setGeometry(QtCore.QRect(250, 70, 91, 20))
        self.reg_error_login.setObjectName("reg_error_login")
        self.reg_error_password = QtWidgets.QLabel(self.tab_registration)
        self.reg_error_password.setGeometry(QtCore.QRect(250, 120, 91, 20))
        self.reg_error_password.setObjectName("reg_error_password")
        self.reg_error_email = QtWidgets.QLabel(self.tab_registration)
        self.reg_error_email.setGeometry(QtCore.QRect(250, 170, 91, 20))
        self.reg_error_email.setObjectName("reg_error_email")
        self.tabWidget.addTab(self.tab_registration, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sign_password_text.setText(_translate("Form", "Пароль"))
        self.sign_login_text.setText(_translate("Form", "Логин"))
        self.sign_button.setText(_translate("Form", "Войти"))
        self.sign_error.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; "
                                                   "color:#ff0000;\">Введены неверные данные</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sign), _translate("Form", "Вход"))
        self.reg_password_text.setText(_translate("Form", "Пароль"))
        self.reg_emal_text.setText(_translate("Form", "Почта"))
        self.reg_button.setText(_translate("Form", "Зарегистрироваться"))
        self.reg_login_text.setText(_translate("Form", "Логин"))
        self.reg_error_login.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                        "color:#ff0000;\">Логин занят</span></p></body></html>"))
        self.reg_error_password.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                           "color:#ff0000;\">PasswordError</span></p></body></html>"))
        self.reg_error_email.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                        "color:#ff0000;\">ValueError</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_registration), _translate("Form", "Регистрация"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(717, 406)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_accounts = QtWidgets.QWidget()
        self.tab_accounts.setObjectName("tab_accounts")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_accounts)
        self.verticalLayout.setContentsMargins(1, 5, 1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.accounts_buttons = QtWidgets.QHBoxLayout()
        self.accounts_buttons.setObjectName("accounts_buttons")
        self.button_add_account = QtWidgets.QPushButton(self.tab_accounts)
        self.button_add_account.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add_account.sizePolicy().hasHeightForWidth())
        self.button_add_account.setSizePolicy(sizePolicy)
        self.button_add_account.setObjectName("button_add_account")
        self.accounts_buttons.addWidget(self.button_add_account)
        self.button_save_accountchanges = QtWidgets.QPushButton(self.tab_accounts)
        self.button_save_accountchanges.setObjectName("button_save_accountchanges")
        self.accounts_buttons.addWidget(self.button_save_accountchanges)
        self.button_delete_account = QtWidgets.QPushButton(self.tab_accounts)
        self.button_delete_account.setObjectName("button_delete_account")
        self.accounts_buttons.addWidget(self.button_delete_account)
        self.verticalLayout.addLayout(self.accounts_buttons)
        self.accounts_table = QtWidgets.QTableWidget(self.tab_accounts)
        self.accounts_table.setObjectName("accounts_table")
        self.accounts_table.setColumnCount(0)
        self.accounts_table.setRowCount(0)
        self.verticalLayout.addWidget(self.accounts_table)
        self.tabWidget.addTab(self.tab_accounts, "")
        self.tab_access = QtWidgets.QWidget()
        self.tab_access.setObjectName("tab_access")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_access)
        self.verticalLayout_2.setContentsMargins(1, 5, 1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.access_buttons = QtWidgets.QHBoxLayout()
        self.access_buttons.setContentsMargins(-1, -1, 0, -1)
        self.access_buttons.setObjectName("access_buttons")
        self.button_add_user = QtWidgets.QPushButton(self.tab_access)
        self.button_add_user.setObjectName("button_add_user")
        self.access_buttons.addWidget(self.button_add_user)
        self.button_delete_user = QtWidgets.QPushButton(self.tab_access)
        self.button_delete_user.setObjectName("button_delete_user")
        self.access_buttons.addWidget(self.button_delete_user)
        self.verticalLayout_2.addLayout(self.access_buttons)
        self.table_access = QtWidgets.QTableWidget(self.tab_access)
        self.table_access.setObjectName("table_access")
        self.table_access.setColumnCount(0)
        self.table_access.setRowCount(0)
        self.verticalLayout_2.addWidget(self.table_access)
        self.tabWidget.addTab(self.tab_access, "")
        self.tab_profile = QtWidgets.QWidget()
        self.tab_profile.setObjectName("tab_profile")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_profile)
        self.verticalLayout_4.setContentsMargins(1, 5, 1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.profile_layot = QtWidgets.QVBoxLayout()
        self.profile_layot.setObjectName("profile_layot")
        self.profile_image_layot = QtWidgets.QHBoxLayout()
        self.profile_image_layot.setObjectName("profile_image_layot")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.profile_show_login = QtWidgets.QCheckBox(self.tab_profile)
        self.profile_show_login.setObjectName("profile_show_login")
        self.verticalLayout_5.addWidget(self.profile_show_login)
        self.profile_show_password = QtWidgets.QCheckBox(self.tab_profile)
        self.profile_show_password.setObjectName("profile_show_password")
        self.verticalLayout_5.addWidget(self.profile_show_password)
        self.profile_show_email = QtWidgets.QCheckBox(self.tab_profile)
        self.profile_show_email.setObjectName("profile_show_email")
        self.verticalLayout_5.addWidget(self.profile_show_email)
        self.profile_image_layot.addLayout(self.verticalLayout_5)
        self.profile_image = QtWidgets.QLabel(self.tab_profile)
        self.profile_image.setText("")
        self.profile_image.setObjectName("profile_image")
        self.profile_image_layot.addWidget(self.profile_image)
        self.profile_layot.addLayout(self.profile_image_layot)
        self.verticalLayout_4.addLayout(self.profile_layot)
        self.profile_image_input = QtWidgets.QPushButton(self.tab_profile)
        self.profile_image_input.setObjectName("profile_image_input")
        self.verticalLayout_4.addWidget(self.profile_image_input)
        self.tabWidget.addTab(self.tab_profile, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Дневник"))
        self.button_add_account.setText(_translate("MainWindow", "Добавить аккаунт"))
        self.button_save_accountchanges.setText(_translate("MainWindow", "Сохранить изменения"))
        self.button_delete_account.setText(_translate("MainWindow", "Удалить аккаунт"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_accounts), _translate("MainWindow", "Аккаунты"))
        self.button_add_user.setText(_translate("MainWindow", "Добавить пользователя"))
        self.button_delete_user.setText(_translate("MainWindow", "Удалить пользователя"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_access), _translate("MainWindow", "Доступ"))
        self.profile_show_login.setText(_translate("MainWindow", "Показать логин"))
        self.profile_show_password.setText(_translate("MainWindow", "Показать пароль"))
        self.profile_show_email.setText(_translate("MainWindow", "Показать почту"))
        self.profile_image_input.setText(_translate("MainWindow", "Загрузить изображение профиля"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_profile), _translate("MainWindow", "Профиль"))


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class EmailError(Exception):
    pass


class DomenError(EmailError):
    pass


class ContentError(EmailError):
    pass


def check_password(password):
    if len(password) < 9:
        raise LengthError
    if password.isupper() or password.islower() or password.isdigit():
        raise LetterError
    if set('0123456789') - set(password) == set('0123456789'):
        raise DigitError
    for i in range(len(password) - 2):
        if password[i:i + 3].lower() in 'qwertyuiop   asdfghjkl   zxcvbnm   ' \
                                      'йцукенгшщзхъ   фывапролджэё   ячсмитьбю':
            raise SequenceError
    return 'ok'


def check_email(word):
    if len(word.split('@')) != 2:
        raise DomenError
    if len(word.split('@')[-1].split('.')) != 2:
        raise DomenError
    for letter in word.split('@')[0]:
        if letter not in 'qwertyuiopasdfghjklzxcvbnm-0123456789':
            raise ContentError
    return True


def func_find_max_length(content):
    if not content:
        return 0
    absolute_max_length = []
    for i in range(len(content[0])):
        max_el = max(map(lambda x: len(str(x[i])), content)) * 7
        absolute_max_length.append(max_el)
    return max(absolute_max_length)


class Form(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Менеджер аккаунтов')

        self.connection = sqlite3.connect("account_manager")
        self.result = self.connection.cursor().execute("""SELECT name, password FROM Users""").fetchall()

        self.sign_password_input.setEchoMode(QLineEdit.Password)
        self.reg_password_input.setEchoMode(QLineEdit.Password)

        self.sign_error.setVisible(False)
        self.reg_error_login.setVisible(False)
        self.reg_error_password.setVisible(False)
        self.reg_error_email.setVisible(False)

        self.sign_button.clicked.connect(self.sign_show)
        self.reg_button.clicked.connect(self.reg_show)

    def sign_show(self):
        self.login = self.sign_login_input.text()
        self.password = self.sign_password_input.text()
        for user in self.result:
            if self.login == user[0] and self.password == user[1]:
                self.w = MainWindow(user[0])
                self.w.show()
                self.close()
            else:
                self.sign_error.setVisible(True)

    def reg_show(self):
        _translate = QtCore.QCoreApplication.translate
        self.login = self.reg_login_input.text()
        self.password = self.reg_password_input.text()
        self.email = self.reg_email_input.text()
        self.logins = [i[0] for i in self.result]
        if self.login in self.logins:
            self.reg_error_login.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                    "color:#ff0000;\">Логин занят</span></p></body></html>"))
            self.reg_error_login.setVisible(True)
        elif not self.login:
            self.reg_error_login.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                            "color:#ff0000;\">Пустой логин</span></p></body></html>"))
            self.reg_error_login.setVisible(True)
        else:
            self.reg_error_login.setVisible(False)
        try:
            check_password(self.password)
            self.reg_error_password.setVisible(False)
        except LengthError:
            self.reg_error_password.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                       "color:#ff0000;\">LengthError</span></p></body></html>"))
            self.reg_error_password.setVisible(True)
        except LetterError:
            self.reg_error_password.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                       "color:#ff0000;\">LetterError</span></p></body></html>"))
            self.reg_error_password.setVisible(True)
        except DigitError:
            self.reg_error_password.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                       "color:#ff0000;\">DigitError</span></p></body></html>"))
            self.reg_error_password.setVisible(True)
        except SequenceError:
            self.reg_error_password.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                       "color:#ff0000;\">SequenceError</span></p></body></html>"))
            self.reg_error_password.setVisible(True)
        try:
            check_email(self.email)
            self.reg_error_email.setVisible(False)
        except DomenError:
            self.reg_error_email.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                            "color:#ff0000;\">DomenError</span></p></body></html>"))
            self.reg_error_email.setVisible(True)
        except ContentError:
            self.reg_error_email.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; "
                                                            "color:#ff0000;\">ContenError</span></p></body></html>"))
            self.reg_error_email.setVisible(True)
        if not self.reg_error_login.isVisible() and not self.reg_error_password.isVisible() and not \
                self.reg_error_email.isVisible():
            self.connection.cursor().execute(
                f"""INSERT INTO Users(name, email, password) 
                VALUES (?, ?, ?)""", (self.login, self.email, self.password,))
            self.connection.commit()
            self.w = MainWindow(self.login)
            self.w.show()
            self.close()

    def closeEvent(self, event):
        self.connection.close()


class AddAccount(QDialog):
    def __init__(self):
        super(AddAccount, self).__init__()
        self.main_box = QVBoxLayout()
        self.setWindowTitle('Добавить аккаунт')
        sp = [QLabel('Логин  '), QLabel('Пароль'), QLabel('Почта  '), QLabel('Сервис')]
        self.line_login = QLineEdit('')
        self.line_password = QLineEdit('')
        self.line_email = QLineEdit('')
        self.line_web = QLineEdit('')
        sp2 = [self.line_login, self.line_password, self.line_email, self.line_web]
        for i in range(len(sp)):
            box = QHBoxLayout()
            box.addWidget(sp[i]), box.addWidget(sp2[i])
            self.main_box.addLayout(box)
        self.setLayout(self.main_box)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.main_box.addWidget(buttonBox)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def get_all(self):
        if self.line_login.text() and self.line_password.text() and self.line_password.text() and self.line_web.text():
            return self.line_login.text(), self.line_password.text(), self.line_password.text(), self.line_web.text()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user_name):
        super().__init__()
        self.user_name = user_name
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Менеджер аккаунтов')

        self.connection = sqlite3.connect("account_manager")
        self.result = self.connection.cursor().execute(f"""
                SELECT * FROM Users WHERE name = ?""", (self.user_name,)).fetchall()[0]

        self.id = self.result[0]
        self.login = self.result[1]
        self.email = self.result[2]
        self.password = self.result[3]
        self.fname = self.result[4]

        self.pixmap = QPixmap(self.fname).scaled(self.profile_image.width(), self.profile_image.height())
        self.profile_image.setPixmap(self.pixmap)

        self.profile_show_login.clicked.connect(lambda: self.profilecheck('login',
                                                                          self.profile_show_login.isChecked()))
        self.profile_show_password.clicked.connect(lambda: self.profilecheck('password',
                                                                             self.profile_show_password.isChecked()))
        self.profile_show_email.clicked.connect(lambda: self.profilecheck('email',
                                                                          self.profile_show_email.isChecked()))
        self.profile_image_input.clicked.connect(self.changeimage)

        self.update_result()
        self.update_access()
        self.accounts_table.itemChanged.connect(self.item_changed)
        self.button_save_accountchanges.clicked.connect(self.save_results)
        self.button_add_account.clicked.connect(self.add_account)
        self.button_delete_account.clicked.connect(self.delete_account)
        self.modified = {}
        self.button_add_user.clicked.connect(self.add_access)
        self.button_delete_user.clicked.connect(self.remove_access)

    def profilecheck(self, field, state):
        if field == 'login':
            if state:
                self.profile_show_login.setText(f'Показать логин: {self.login}')
            else:
                self.profile_show_login.setText(f'Показать логин')
        elif field == 'password':
            if state:
                self.profile_show_password.setText(f'Показать пароль: {self.password}')
            else:
                self.profile_show_password.setText(f'Показать пароль')
        elif field == 'email':
            if state:
                self.profile_show_email.setText(f'Показать почту: {self.email}')
            else:
                self.profile_show_email.setText(f'Показать почту')

    def changeimage(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.pixmap = QPixmap(self.fname).scaled(self.profile_image.width(), self.profile_image.height())
        self.profile_image.setPixmap(self.pixmap)
        self.connection.cursor().execute("""UPDATE users
        SET image = ?
        WHERE name = ?""", (self.fname, self.login,))
        self.connection.commit()

    def closeEvent(self, event):
        self.connection.close()

    def update_result(self):
        cur = self.connection.cursor()
        result = cur.execute("SELECT * FROM accounts WHERE user_id=?",
                             (self.id,)).fetchall()
        result2 = cur.execute("""SELECT * FROM accounts 
        LEFT JOIN relationships ON relationships.sender_id = user_id
        WHERE relationships.receiver_id = ?""", (self.id,)).fetchall()
        if not result:
            return
        if result2:
            result.extend(result2)
        self.accounts_table.setRowCount(len(result))
        self.accounts_table.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        width = func_find_max_length(result)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.accounts_table.setItem(i, j, QTableWidgetItem(str(val)))
                self.accounts_table.setColumnWidth(i, width)
        self.accounts_table.setHorizontalHeaderLabels(self.titles)

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.connection.cursor()
            que = "UPDATE accounts SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                              for key in self.modified.keys()])
            que += "WHERE id = ?"
            valid = QMessageBox.question(
                self, '', "Действительно сохранить изменения",
                QMessageBox.Yes, QMessageBox.No)
            if valid:
                cur.execute(que, (self.id,))
                self.connection.commit()
                self.modified.clear()

    def add_account(self):
        cur = self.connection.cursor()
        dialog = AddAccount()
        if not dialog.exec():
            pass
        else:
            val = dialog.get_all()
            if not val:
                return
            login, password, email, service = val
            cur.execute(f"""INSERT INTO accounts(user_id, login, email, password, service) 
                VALUES (?, ?, ?, ?, ?)""", (self.id, login, email, password, service,))
        self.connection.commit()
        self.update_result()

    def delete_account(self):
        rows = list(set([i.row() for i in self.accounts_table.selectedItems()]))
        ids = [self.accounts_table.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Действительно удалить выбранные элементы",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.connection.cursor()
            cur.execute("DELETE FROM accounts WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            self.connection.commit()
            self.update_result()

    def update_access(self):
        cur = self.connection.cursor()
        result = cur.execute("SELECT * FROM relationships WHERE sender_id=?",
                             (self.id,)).fetchall()
        self.table_access.setRowCount(len(result))
        if not result:
            return
        self.table_access.setColumnCount(len(result[0]))
        self.titles_access = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table_access.setItem(i, j, QTableWidgetItem(str(val)))
        self.table_access.setHorizontalHeaderLabels(self.titles_access)

    def add_access(self):
        login = QInputDialog.getText(self, 'Логин', 'Введите логин')
        text, valid = login
        if not valid:
            return
        cur = self.connection.cursor()
        try:
            receiver_id = cur.execute("""SELECT id FROM users WHERE name = ?""", (text,)).fetchall()[0][0]
            cur.execute("""INSERT INTO relationships(sender_id, receiver_id) VALUES(?, ?)""", (self.id, receiver_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            pass
        except IndexError as e:
            pass
        self.update_access()

    def remove_access(self):
        rows = list(set([i.row() for i in self.table_access.selectedItems()]))
        ids = [self.table_access.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Действительно удалить выбранные элементы",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.connection.cursor()
            cur.execute("DELETE FROM relationships WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            self.connection.commit()
            self.update_access()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec())
