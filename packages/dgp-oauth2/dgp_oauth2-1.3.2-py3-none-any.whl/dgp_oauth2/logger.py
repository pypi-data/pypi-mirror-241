import sys
import logging

logger = logging.getLogger('dgp-oauth2')
handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.WARNING)
