from sys import stderr
from os import path
import logging
from server_dist.server.common.variables import LOG_LEVEL_FILE, \
    LOG_LEVEL_STREAM

FORMATTER = logging.Formatter(
    '%(asctime)s %(created)f %(levelname)s %(pathname)s %(filename)s '
    '%(lineno)d %(message)s')

PATH_LOG_FILE = path.abspath(path.join(__file__, "../../logs"))
PATH_LOG_FILE = path.join(PATH_LOG_FILE, 'client.log')

STREAM_HANDLER = logging.StreamHandler(stderr)
STREAM_HANDLER.setFormatter(FORMATTER)
STREAM_HANDLER.setLevel(LOG_LEVEL_STREAM)
LOG_FILE = logging.FileHandler(PATH_LOG_FILE, encoding='utf8')
LOG_FILE.setFormatter(FORMATTER)

LOGGER = logging.getLogger('client_logger')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOG_LEVEL_FILE)

if __name__ == '__main__':
    LOGGER.info('Информационное сообщение')
    LOGGER.debug('Отладочная информация')
    LOGGER.error('Ошибка')
    LOGGER.critical('Критическая ошибка')
