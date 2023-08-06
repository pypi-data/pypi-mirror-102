import inspect
import logging
import sys
import traceback

if sys.argv[0].find('client') >= 0:
    LOGGER = logging.getLogger('client')
elif sys.argv[0].find('server') >= 0:
    LOGGER = logging.getLogger('server')
else:
    # print(sys.argv[0])
    # raise ValueError
    pass


def log_decorator(func_to_log):
    def log_record(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        log_args = traceback.format_stack()[0].strip().split()
        code_record = ''
        for i in range(6, len(log_args)):
            code_record += log_args[i]
        log_str = f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. ' \
                  f'из модуля {func_to_log.__module__}. ' \
                  f'в строке {log_args[3]} ' \
                  f'код: {code_record} ' \
                  f'Вызов из функции {inspect.stack()[1][3]}. ' \
                  f'Функция вернула {ret}'
        log_str = log_str.replace('<module>', '__main__')
        LOGGER.debug(log_str, stacklevel=2)
        return ret

    return log_record
