import inspect

import pytest
import logging


@pytest.mark.usefixtures("setup")
class TestBaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : % (message)s")
        fileHandler.setFormatter(format)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger
