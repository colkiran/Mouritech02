
import logging

logging.basicConfig(filename="file2.log",
                    level=logging.WARNING,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

parent_logger = logging.getLogger('parent')
parent_logger.setLevel(logging.INFO)
parent_fhandler = logging.FileHandler("parent.log")
parent_logger.addHandler(parent_fhandler)


parent_logger.debug("this is debug message")
parent_logger.info("this is info message")
parent_logger.warning("this is warning message")
parent_logger.error("this is error message")
parent_logger.critical("this is critical message")