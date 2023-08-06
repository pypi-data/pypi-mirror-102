import json
from server_dist.server.common.variables import MAX_PACKAGE_LENGTH, ENCODING
from server_dist.server.common.decor import LogDecor


class PortException(Exception):
    def __str__(self):
        return 'Указан некорректный порт'


class ModeException(Exception):
    def __str__(self):
        return 'Указан некорректный режим'


class IncorrectDataReceivedError(Exception):
    def __str__(self):
        return 'Принято некорректное сообщение от удалённого компьютера.'


class NonDictInputError(Exception):
    def __str__(self):
        return 'Аргумент функции должен быть словарём.'


class ServerError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class ReqFieldMissingError(Exception):
    def __init__(self, missing_field):
        self.missing_field = missing_field


@LogDecor()
def get_message(client):
    """
    Функция приёма сообщений от удалённых компьютеров.
    :param client: сокет для передачи данных.
    :return: словарь - сообщение.
    """
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    json_response = encoded_response.decode(ENCODING)
    response = json.loads(json_response)
    if isinstance(response, dict):
        return response
    else:
        raise TypeError


@LogDecor()
def send_message(sock, message):
    """
    Функция отправки словарей через сокет.
    :param sock: сокет
    :param message: словарь для передачи
    """
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
