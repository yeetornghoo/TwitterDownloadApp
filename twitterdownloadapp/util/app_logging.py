__author__ = "CH"

import logging

logger = logging.getLogger()


def log_format(log_type, msg):
    return_msg = "{} - {}".format(log_type, msg)
    return return_msg


class AppLogging:
    def info(self, msg):
        log_msg = log_format("INFO", msg)
        print(log_msg)
        logger.info(log_msg)

    def exception(self, msg):
        log_msg = log_format("EXCEPTION", msg)
        print(log_msg)
        logger.info(log_msg)
