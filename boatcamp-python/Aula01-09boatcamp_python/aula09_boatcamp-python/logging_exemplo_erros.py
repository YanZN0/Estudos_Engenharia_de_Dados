from loguru import logger

logger.debug("Um aviso para o dev(talvez eu mesmo) no futuro")
logger.info("Informação importante no processo")
logger.warning("Um aviso que algo vai parar de funcionar")
logger.error("Aconteceu alguma falha")
logger.critical("Aconteceu uma falha grave que aborta a aplicação")