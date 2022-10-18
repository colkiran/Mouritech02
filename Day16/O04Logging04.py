
import logging

logging.basicConfig(filename='file01.log',
                    level=logging.WARNING,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

# logger, streamhandler
parent_logger = logging.getLogger("parent")
parent_logger.setLevel(logging.INFO)
parent_shandler = logging.StreamHandler()
parent_logger.addHandler(parent_shandler)

parent_logger.debug("this is debug message")
parent_logger.info("this is info message")
parent_logger.warning("this is warning message")
parent_logger.error("this is error message")
parent_logger.critical("this is critical message")

