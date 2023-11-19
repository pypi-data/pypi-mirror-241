
import logging


def get_console_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('(%(name)s) [%(asctime)s | %(levelname)s]: %(message)s', datefmt='%H:%M:%S'))
    logger.addHandler(handler)
    return logger
