
import logging

logger = logging.getLogger("parent.child")

logger.info("this is info level")

parentlogger = logging.getLogger('parent')


handler = logging.StreamHandler()           # pushed to the screen
handler.setFormatter(logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s'))
parentlogger.setLevel(logging.INFO)

parentlogger.addHandler(handler)

logger.info("this is info level")