import logging, logging.config
import sys

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}

class Logger:
    LOG_FILE_PATH = "log.log"


    def get_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if not getattr(logger, "handler_set", None):
            formatter = logging.Formatter("%(asctime)s|%(module)s|%(lineno)d|| %(message)s")
            file_handler = logging.FileHandler(self.LOG_FILE_PATH)
            file_handler.setFormatter(formatter)
            consoleHandler = logging.StreamHandler()
            consoleHandler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.addHandler(consoleHandler)
            logger.handler_set = True
        return logger
