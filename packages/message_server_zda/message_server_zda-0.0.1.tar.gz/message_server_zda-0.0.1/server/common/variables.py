import logging

DEFAULT_PORT = 6666
DEFAULT_ADDRESS = 'localhost'
MAX_CONNECTIONS = 10
MAX_PACKAGE_LENGTH = 1024
ENCODING = 'utf-8'
SERVER_DATABASE = 'sqlite:///server_base.db3'

PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
GET_CONTACTS = 'get_contacts'
LIST_INFO = 'data_list'
REMOVE_CONTACT = 'remove'
ADD_CONTACT = 'add'
USERS_REQUEST = 'get_users'

ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
EXIT = 'exit'
SENDER = 'from'
DESTINATION = 'to'
PUBLIC_KEY = 'public_key'
DATA = 'bin'
PUBLIC_KEY_REQUEST = 'public_key_need'

LOG_LEVEL_FILE = logging.DEBUG
LOG_LEVEL_STREAM = logging.ERROR

DEFAULT_MODE = 'send'
DEFAULT_NAME = 'Guest'
MESSAGE = 'message'
MESSAGE_TEXT = 'message_text'

RESPONSE_200 = {RESPONSE: 200}

RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}

RESPONSE_202 = {
    RESPONSE: 202,
    LIST_INFO: None
}

RESPONSE_511 = {
    RESPONSE: 511,
    DATA: None
}

RESPONSE_205 = {
    RESPONSE: 205
}
