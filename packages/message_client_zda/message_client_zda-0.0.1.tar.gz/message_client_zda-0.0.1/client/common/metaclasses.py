import dis


class ServerMaker(type):
    def __init__(self, class_name, bases, class_dict):
        methods = []
        attribs = []

        for func_item in class_dict:
            try:
                res = dis.get_instructions(class_dict[func_item])
            except TypeError:
                pass
            else:
                for item in res:
                    if item.opname == 'LOAD_GLOBAL':
                        if item.argval not in methods:
                            methods.append(item.argval)
                    elif item.opname == 'LOAD_ATTR':
                        if item.argval not in attribs:
                            attribs.append(item.argval)

        if 'connect' in methods:
            raise TypeError(
                'Использование метода connect недопустимо в серверном классе')
        if not ('SOCK_STREAM' in attribs and 'AF_INET' in attribs):
            raise TypeError('Некорректная инициализация сокета.')
        super().__init__(class_name, bases, class_dict)


class ClientMaker(type):
    def __init__(self, class_name, bases, class_dict):

        methods = []
        for func in class_dict:
            try:
                ret = dis.get_instructions(class_dict[func])
            except TypeError:
                pass
            else:
                for item in ret:
                    if item.opname == 'LOAD_GLOBAL':
                        if item.argval not in methods:
                            methods.append(item.argval)

        for command in ('accept', 'listen', 'socket'):
            if command in methods:
                raise TypeError(
                    'В классе обнаружено использование запрещённого метода')

        if 'get_message' in methods or 'send_message' in methods:
            pass
        else:
            raise TypeError(
                'Отсутствуют вызовы функций, работающих с сокетами.')
        super().__init__(class_name, bases, class_dict)
