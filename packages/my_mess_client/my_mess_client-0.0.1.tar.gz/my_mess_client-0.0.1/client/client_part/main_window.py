import sys
import base64
import json
import logging
from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from PyQt5.QtCore import pyqtSlot, Qt
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
sys.path.append('../')
from client_part.main_window_conv import Ui_MainClientWindow
from client_part.add_contact import AddContactDialog
from client_part.del_contact import DelContactDialog
from common.errors import ServerError
from common.decorator import LOGGER


# Класс основного окна
class ClientMainWindow(QMainWindow):
    """
    Класс - основное окно пользователя.
    Содержит всю основную логику работы клиентского модуля.
    Конфигурация окна создана в QTDesigner и загружается из
    конвертированого файла main_window_conv.py
    """
    def __init__(self, client):
        super().__init__()
        # основные переменные
        self.transport = client
        self.db_session = client.database.create_session()
        client.new_message.connect(self.message)
        client.connection_lost.connect(self.connection_lost)

        # объект - дешифорвщик сообщений с предзагруженным ключём
        self.decrypter = PKCS1_OAEP.new(client.keys)

        # Загружаем конфигурацию окна из дизайнера
        self.ui = Ui_MainClientWindow()
        self.ui.setupUi(self)

        # Кнопка "Выход"
        self.ui.menu_exit.triggered.connect(qApp.exit)

        # Кнопка отправить сообщение
        self.ui.btn_send.clicked.connect(self.send_message)

        # "добавить контакт"
        self.ui.btn_add_contact.clicked.connect(self.add_contact_window)
        self.ui.menu_add_contact.triggered.connect(self.add_contact_window)

        # Удалить контакт
        self.ui.btn_remove_contact.clicked.connect(self.delete_contact_window)
        self.ui.menu_del_contact.triggered.connect(self.delete_contact_window)

        # Нажатие клавиш в поле ввода сообщения
        self.ui.text_message.keyPressed.connect(self.text_message_key_pressed)

        # Дополнительные требующиеся атрибуты
        self.contacts_model = None
        self.history_model = None
        self.messages = QMessageBox()
        self.current_chat = None
        self.current_chat_key = None
        self.encryptor = None
        self.ui.list_messages.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.list_messages.setWordWrap(True)

        # Даблклик по листу контактов отправляется в обработчик
        self.ui.list_contacts.doubleClicked.connect(self.select_active_user)

        self.clients_list_update()
        self.set_disabled_input()
        self.show()

    def set_disabled_input(self):
        """Деактивировать поля ввода"""
        # Надпись  - получатель.
        self.ui.label_new_message.setText('Для выбора получателя дважды кликните на нем в окне контактов.')
        self.ui.text_message.clear()
        if self.history_model:
            self.history_model.clear()

        # Поле ввода и кнопка отправки неактивны до выбора получателя.
        self.ui.btn_clear.setDisabled(True)
        self.ui.btn_send.setDisabled(True)
        self.ui.text_message.setDisabled(True)

        self.encryptor = None
        self.current_chat = None
        self.current_chat_key = None

    def history_list_update(self):
        """Заполняем историю сообщений."""
        # Получаем историю сортированную по дате
        list = sorted(self.db_session.get_history(with_who=self.current_chat), key=lambda item: item[3])
        # Если модель не создана, создадим.
        if not self.history_model:
            self.history_model = QStandardItemModel()
            self.ui.list_messages.setModel(self.history_model)
        # Очистим от старых записей
        self.history_model.clear()
        # Берём не более 20 последних записей.
        length = len(list)
        start_index = 0
        if length > 20:
            start_index = length - 20
        # Заполнение модели записями, также стоит разделить входящие и исходящие выравниванием и разным фоном.
        # Записи в обратном порядке, поэтому выбираем их с конца и не более 20
        for i in range(start_index, length):
            item = list[i]
            if item[1] != self.current_chat:
                mess = QStandardItem(f'Входящее от {item[0]} {item[3].replace(microsecond=0)}:\n {item[2]}')
                mess.setEditable(False)
                mess.setBackground(QBrush(QColor(255, 213, 213)))
                mess.setTextAlignment(Qt.AlignLeft)
                self.history_model.appendRow(mess)
            else:
                mess = QStandardItem(f'Исходящее для {item[0]} {item[3].replace(microsecond=0)}:\n {item[2]}')
                mess.setEditable(False)
                mess.setTextAlignment(Qt.AlignRight)
                mess.setBackground(QBrush(QColor(204, 255, 204)))
                self.history_model.appendRow(mess)
        self.ui.list_messages.scrollToBottom()

    def select_active_user(self):
        """Метод обработчик даблклика по контакту"""
        # Выбранный пользователем (даблклик) находится в выделеном элементе в QListView
        self.current_chat = self.ui.list_contacts.currentIndex().data()
        # вызываем основную функцию
        self.set_active_user()

    def set_active_user(self):
        """
        Метод активации чата с собеседником.
        :return: если нет ключа шифрования, то выход
        """
        # Запрашиваем публичный ключ пользователя и создаём объект шифрования
        try:
            self.current_chat_key = self.transport.key_request(
                self.current_chat)
            LOGGER.debug(f'Загружен открытый ключ для {self.current_chat}')
            if self.current_chat_key:
                self.encryptor = PKCS1_OAEP.new(
                    RSA.import_key(self.current_chat_key))
        except (OSError, json.JSONDecodeError):
            self.current_chat_key = None
            self.encryptor = None
            LOGGER.debug(f'Не удалось получить ключ для {self.current_chat}')

        # Если ключа нет то ошибка, что не удалось начать чат с пользователем
        if not self.current_chat_key:
            self.messages.warning(
                self, 'Ошибка', 'Для выбранного пользователя нет ключа шифрования.')
            return

        # Ставим надпись и активируем кнопки
        self.ui.label_new_message.setText(f'Введите сообщенние для {self.current_chat}:')
        self.ui.btn_clear.setDisabled(False)
        self.ui.btn_send.setDisabled(False)
        self.ui.text_message.setDisabled(False)

        # Заполняем окно историю сообщений по требуемому пользователю.
        self.history_list_update()

    def clients_list_update(self):
        """Метод обновляющий контакт лист"""
        contacts_list = self.db_session.get_contacts()
        self.contacts_model = QStandardItemModel()
        for i in sorted(contacts_list):
            item = QStandardItem(i)
            item.setEditable(False)
            self.contacts_model.appendRow(item)
        self.ui.list_contacts.setModel(self.contacts_model)

    def add_contact_window(self):
        """Метод добавления контакта"""
        global select_dialog
        select_dialog = AddContactDialog(self.transport)
        select_dialog.btn_ok.clicked.connect(lambda: self.add_contact_action(select_dialog))
        select_dialog.show()

    def add_contact_action(self, item):
        """Метод - обработчик добавления, сообщает серверу, обновляет таблицу и список контактов"""
        new_contact = item.selector.currentText()
        self.add_contact(new_contact)
        item.close()

    def add_contact(self, new_contact):
        """Метод добавляющий контакт в базы"""
        try:
            self.transport.add_contact(new_contact)
        except ServerError as err:
            self.messages.critical(self, 'Ошибка сервера', err.text)
        except OSError as err:
            if err.errno:
                self.messages.critical(self, 'Ошибка', 'Потеряно соединение с сервером!')
                self.close()
            self.messages.critical(self, 'Ошибка', 'Таймаут соединения!')
        else:
            self.db_session.add_contact(new_contact)
            new_contact = QStandardItem(new_contact)
            new_contact.setEditable(False)
            self.contacts_model.appendRow(new_contact)
            LOGGER.info(f'Успешно добавлен контакт {new_contact}')
            self.messages.information(self, 'Успех', 'Контакт успешно добавлен.')

    def delete_contact_window(self):
        """Метод удаления контакта"""
        global remove_dialog
        remove_dialog = DelContactDialog(self.db_session)
        remove_dialog.btn_ok.clicked.connect(lambda: self.delete_contact(remove_dialog))
        remove_dialog.show()

    def delete_contact(self, item):
        """Метод - обработчик удаления контакта, сообщает на сервер, обновляет таблицу контактов"""
        selected = item.selector.currentText()
        try:
            self.transport.remove_contact(selected)
        except ServerError as err:
            self.messages.critical(self, 'Ошибка сервера', err.text)
        except OSError as err:
            if err.errno:
                self.messages.critical(self, 'Ошибка', 'Потеряно соединение с сервером!')
                self.close()
            self.messages.critical(self, 'Ошибка', 'Таймаут соединения!')
        else:
            self.db_session.del_contact(selected)
            self.clients_list_update()
            LOGGER.info(f'Успешно удалён контакт {selected}')
            self.messages.information(self, 'Успех', 'Контакт успешно удалён.')
            item.close()
            # Если удалён активный пользователь, то деактивируем поля ввода.
            if selected == self.current_chat:
                self.current_chat = None
                self.set_disabled_input()

    def text_message_key_pressed(self, key):
        """Обработка нажатия клавиш в поле ввода сообщения"""
        # Проверка на нажатие Enter
        if key == Qt.Key_Return:
            self.send_message()

    def send_message(self):
        """
        Метод отправки сообщения текущему собеседнику.
        Реализует шифрование сообщения и его отправку.
        :return: выход если нет сообщения
        """
        # Текст в поле, проверяем что поле не пустое затем забирается сообщение и поле очищается
        message_text = self.ui.text_message.toPlainText().strip()
        self.ui.text_message.clear()
        if not message_text:
            return
        # Шифруем сообщение ключом получателя и упаковываем в base64.
        message_text_encrypted = self.encryptor.encrypt(
            message_text.encode('utf8'))
        message_text_encrypted_base64 = base64.b64encode(
            message_text_encrypted)
        try:
            self.transport.send_message(message_text_encrypted_base64.decode('ascii'), self.current_chat)
            self.db_session.save_message(self.transport.client_name, self.current_chat, message_text)
            pass
        except ServerError as err:
            self.messages.critical(self, 'Ошибка', err.text)
        except OSError as err:
            if err.errno:
                self.messages.critical(self, 'Ошибка', 'Потеряно соединение с сервером!')
                self.close()
            self.messages.critical(self, 'Ошибка', 'Таймаут соединения!')
        except (ConnectionResetError, ConnectionAbortedError):
            self.messages.critical(self, 'Ошибка', 'Потеряно соединение с сервером!')
            self.close()
        else:
            LOGGER.debug(f'Отправлено сообщение для {self.current_chat}: {message_text}')
            self.history_list_update()

    # Слот приёма нового сообщений
    @pyqtSlot(dict)
    def message(self, message):
        """
        Слот обработчик поступаемых сообщений, выполняет дешифровку
        поступаемых сообщений и их сохранение в истории сообщений.
        Запрашивает пользователя если пришло сообщение не от текущего
        собеседника. При необходимости меняет собеседника.
        :param message: сообщение
        :return: выход, если не удалось декодировать сообщение
        """
        # Получаем строку байтов
        encrypted_message = base64.b64decode(message[self.transport.MESSAGE_TEXT])
        # Декодируем строку, при ошибке выдаём сообщение и завершаем функцию
        try:
            decrypted_message = self.decrypter.decrypt(encrypted_message)
        except (ValueError, TypeError):
            self.messages.warning(
                self, 'Ошибка', 'Не удалось декодировать сообщение.')
            return
        # Сохраняем сообщение в базу и обновляем историю сообщений или
        # открываем новый чат.
        self.db_session.save_message(self.current_chat, 'in', decrypted_message.decode('utf8'))
        sender = message[self.transport.SENDER]
        if sender == self.current_chat:
            self.history_list_update()
        else:
            # Проверим есть ли такой пользователь у нас в контактах:
            if self.db_session.check_contact(sender):
                # Если есть, спрашиваем и желании открыть с ним чат и открываем при желании
                if self.messages.question(self, 'Новое сообщение',
                                          f'Получено новое сообщение от {sender}, открыть чат с ним?', QMessageBox.Yes,
                                          QMessageBox.No) == QMessageBox.Yes:
                    self.current_chat = sender
                    self.set_active_user()
            else:
                print('NO')
                # Раз нету,спрашиваем хотим ли добавить юзера в контакты.
                if self.messages.question(self, 'Новое сообщение',
                                          f'Получено новое сообщение от {sender}.\n '
                                          f'Данного пользователя нет в вашем контакт-листе.\n '
                                          f'Добавить в контакты и открыть чат с ним?',
                                          QMessageBox.Yes,
                                          QMessageBox.No) == QMessageBox.Yes:
                    self.add_contact(sender)
                    self.current_chat = sender
                    self.set_active_user()

    # Слот потери соединения
    # Выдаёт сообщение о ошибке и завершает работу приложения
    @pyqtSlot()
    def connection_lost(self):
        self.messages.warning(self, 'Сбой соединения', 'Потеряно соединение с сервером. ')
        self.close()
