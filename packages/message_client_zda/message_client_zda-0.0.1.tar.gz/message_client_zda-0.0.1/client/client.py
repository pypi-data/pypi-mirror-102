import argparse
import logging
import os
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from client_dist.client.common.utils import ServerError
from client_dist.client.client.client_database import ClientDatabase
from client_dist.client.client.main_window import ClientMainWindow
from client_dist.client.client.start_dialog import UserNameDialog
from Cryptodome.PublicKey import RSA
from client_dist.client.client.transport import ClientTransport
from server_dist.server.common.variables import DEFAULT_PORT, DEFAULT_ADDRESS

CLIENT_LOG = logging.getLogger('client_logger')


def arg_parser():
    """
    Парсер аргументов командной строки.
    Выполняет проверку на корректность номера порта.
    :return: кортеж из 4 элементов адрес сервера, порт, имя пользователя,
    пароль
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-n', '--name', default=None, nargs='?')
    parser.add_argument('-p', '--password', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_name = namespace.name
    client_passwd = namespace.password

    if not 1023 < server_port < 65536:
        CLIENT_LOG.critical(
            f'Попытка запуска клиента с неподходящим номером порта: '
            f'{server_port}. Допустимы адреса с 1024 до 65535. '
            f'Клиент завершается.')
        sys.exit(1)

    return server_address, server_port, client_name, client_passwd


if __name__ == '__main__':
    server_address, server_port, client_name, client_passwd = arg_parser()
    CLIENT_LOG.debug('Args loaded')

    client_app = QApplication(sys.argv)

    start_dialog = UserNameDialog()
    if not client_name or not client_passwd:
        client_app.exec_()
        if start_dialog.ok_pressed:
            client_name = start_dialog.client_name.text()
            client_passwd = start_dialog.client_passwd.text()
            CLIENT_LOG.debug(
                f'Using USERNAME = {client_name}, PASSWD = {client_passwd}.')
        else:
            sys.exit(0)

    CLIENT_LOG.info(
        f'Запущен клиент с парамертами: адрес сервера: {server_address}, '
        f'порт: {server_port}, имя пользователя: {client_name}')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    key_file = os.path.join(dir_path, f'{client_name}.key')
    if not os.path.exists(key_file):
        keys = RSA.generate(2048, os.urandom)
        with open(key_file, 'wb') as key:
            key.write(keys.export_key())
    else:
        with open(key_file, 'rb') as key:
            keys = RSA.import_key(key.read())

    CLIENT_LOG.debug("Keys successfully loaded.")
    database = ClientDatabase(client_name)
    try:
        transport = ClientTransport(
            server_port,
            server_address,
            database,
            client_name,
            client_passwd,
            keys)
        CLIENT_LOG.debug("Transport ready.")
    except ServerError as error:
        message = QMessageBox()
        message.critical(start_dialog, 'Ошибка сервера', error.text)
        sys.exit(1)
    transport.setDaemon(True)
    transport.start()
    del start_dialog
    main_window = ClientMainWindow(database, transport, keys)
    main_window.make_connection(transport)
    main_window.setWindowTitle(f'Чат - {client_name}')
    client_app.exec_()
    transport.transport_shutdown()
    transport.join()
