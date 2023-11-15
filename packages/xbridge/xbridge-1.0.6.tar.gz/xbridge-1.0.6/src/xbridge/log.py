import logging

logger = logging.getLogger('xbridge')
logger.setLevel(logging.ERROR)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s: [%(levelname)s] %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

