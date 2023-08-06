import dis


class Verifier(type):
    def __init__(cls, classname, bases, classdict):
        load_global = []
        # print(classname)
        # print(bases)
        for func in classdict:
            try:
                # instructions = dis.get_instructions(classdict[func])
                instructions = dis.Bytecode(classdict[func])
                # print(func)
            except TypeError:
                pass
            else:
                for instr in instructions:
                    # print(instr)
                    if instr.opname == 'LOAD_GLOBAL':
                        if instr.argval not in load_global:
                            load_global.append(instr.argval)
        # print(load_global)
        if not ('SOCK_STREAM' in load_global and 'AF_INET' in load_global):
            raise TypeError('incorrect socket initialisation.')
        else:
            # print('socket initialisation is OK!')
            pass
        super().__init__(classname, bases, classdict)

    def __call__(cls, *args, **kwargs):  # вызов экземпляра
        # print(args[0])
        return super().__call__(*args, **kwargs)


class ServerVerifier(type):
    def __init__(self, classname, bases, classdict):
        load_method = []
        for func in classdict:
            try:
                instructions = dis.Bytecode(classdict[func])
                # print(func)
            except TypeError:
                pass
            else:
                for instr in instructions:
                    # print(instr)
                    if instr.opname == 'LOAD_METHOD':
                        if instr.argval not in load_method:
                            load_method.append(instr.argval)
        # print(load_method)
        if 'accept' not in load_method:
            raise TypeError('ERROR!!! server should use "accept" method !!')
        elif 'connect' in load_method:
            raise TypeError(
                'ERROR!!! you cannot use "connect" method in a server!!')
        else:
            pass
            # print('server validation is OK!')
        super().__init__(classname, bases, classdict)


class ClientVerifier(type):
    def __init__(self, classname, bases, classdict):
        load_method = []
        for func in classdict:
            try:
                instructions = dis.Bytecode(classdict[func])
                # print(func)
            except TypeError:
                pass
            else:
                for instr in instructions:
                    # print(instr)
                    if instr.opname == 'LOAD_METHOD':
                        if instr.argval not in load_method:
                            load_method.append(instr.argval)
        # print(load_method)
        if 'accept' in load_method or 'listen' in load_method:
            raise TypeError(
                'ERROR!!! client cannot use "accept" and "listen" methods !!')
        else:
            pass
            # print('client validation is OK!')
        super().__init__(classname, bases, classdict)
