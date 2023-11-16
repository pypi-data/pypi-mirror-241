import logging

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s")) #%(asctime)s %(levelname)s %(message)s
logger = logging.getLogger("lgbopt")
logger.addHandler(handler)
logger.setLevel(logging.INFO)