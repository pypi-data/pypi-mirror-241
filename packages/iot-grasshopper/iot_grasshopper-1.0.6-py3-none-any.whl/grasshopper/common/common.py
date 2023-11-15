"""Provides configured logger"""
import logging


formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

log_handler = logging.StreamHandler()
log_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
logger.addHandler(log_handler)

children = []

def getLogger(name: str, level: int | str=logging.INFO):
    child_logger = logger.getChild(suffix=name)
    child_logger.setLevel(level)
    children.append(child_logger)
    return child_logger

def setLogLevel(level):
    for child_logger in children:
        child_logger.setLevel(level)
    logger.setLevel(level)
