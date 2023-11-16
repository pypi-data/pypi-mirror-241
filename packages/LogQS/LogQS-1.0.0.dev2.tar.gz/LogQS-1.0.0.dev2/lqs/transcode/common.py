import os
import logging


def get_logger(name, level=None):
    logger = logging.getLogger(name)
    if level is None:
        level = os.getenv("LQS_LOG_LEVEL", "INFO").upper()
    logger.setLevel(level)

    if not logger.handlers:  # Check if logger already has handlers
        if level == "DEBUG":
            # include filename and line number in log output
            formatter = logging.Formatter(
                "%(asctime)s  (%(levelname)s - %(name)s - %(filename)s:%(lineno)d): %(message)s"
            )
        else:
            formatter = logging.Formatter(
                "%(asctime)s  (%(levelname)s - %(name)s): %(message)s"
            )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
