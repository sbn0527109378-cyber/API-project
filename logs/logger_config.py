import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s | %(levelname)s | %(message)s",
                    filename="logs/app.log")


def get_logger(name):
    return logging.getLogger(name)