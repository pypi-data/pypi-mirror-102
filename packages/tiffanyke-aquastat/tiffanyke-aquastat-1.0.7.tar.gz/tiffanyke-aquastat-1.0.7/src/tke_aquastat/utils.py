import logging.config
logging.config.fileConfig('/Users/tiffanyke/2021-msia423-Ke-Tiffany-assignment1/logger.conf')
logger = logging.getLogger("utils")

def log_debug(msg = "DEBUG!"):
    logger.debug(msg)


def log_info(msg = "INFO!"):
    logger.info(msg)


def log_warning(msg = "WARNING!"):
    logger.warning(msg)


def log_error(msg = "ERROR!"):
    logger.error(msg)


if __name__ == "__main__":
    log_debug()
    log_info()
    log_warning()
    log_error()
