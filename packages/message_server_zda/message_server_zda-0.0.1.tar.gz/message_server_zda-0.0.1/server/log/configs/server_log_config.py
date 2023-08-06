from sys import stderr
from os import path
import logging.handlers
from server_dist.server.common.variables import LOG_LEVEL_FILE, \
    LOG_LEVEL_STREAM

FORMATTER = logging.Formatter(
    '%(asctime)s %(created)f %(levelname)s %(pathname)s %(filename)s '
    '%(lineno)d %(message)s')

PATH_LOG_FILE = path.abspath(path.join(__file__, "../../logs"))
PATH_LOG_FILE = path.join(PATH_LOG_FILE, 'server.log')

STREAM_HND = logging.StreamHandler(stderr)
STREAM_HND.setFormatter(FORMATTER)
STREAM_HND.setLevel(LOG_LEVEL_STREAM)

LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH_LOG_FILE,
                                                     encoding='utf8',
                                                     interval=1, when='D')
LOG_FILE.setFormatter(FORMATTER)

LOGGER = logging.getLogger('server_logger')
LOGGER.addHandler(STREAM_HND)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOG_LEVEL_FILE)

if __name__ == '__main__':
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
    LOGGER.error('Ошибка')
    LOGGER.critical('Критическая ошибка')
