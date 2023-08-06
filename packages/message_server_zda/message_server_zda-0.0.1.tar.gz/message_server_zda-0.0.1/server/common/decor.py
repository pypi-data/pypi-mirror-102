import sys
import logging
import traceback
import inspect

if sys.argv[0].find('client') != -1:
    LOGGER = logging.getLogger('client_logger')
else:
    LOGGER = logging.getLogger('server_logger')


class LogDecor:
    def __call__(self, func):
        def log_save(*args, **kwargs):
            ret = func(*args, **kwargs)
            LOGGER.debug(
                f'Была вызвана функция {func.__name__} c '
                f'параметрами {args}, {kwargs}. '
                f'Вызов из модуля {func.__module__}. Вызов из'
                f' функции {traceback.format_stack()[0].strip().split()[-1]}.'
                f'Вызов из функции {inspect.stack()[1][3]}. '
                f'Результат вызова функции {ret}')
            return ret
        return log_save
