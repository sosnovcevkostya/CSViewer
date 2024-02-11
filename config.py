import os
import logging
from dotenv import load_dotenv

load_dotenv()
match os.getenv('LOGGING_LEVEL'):
  case "INFO":
    logging.basicConfig(level=logging.INFO)
  case _:
    logging.basicConfig(level=logging.WARNING)


DATA_DIR = os.getenv('DATA_DIR') or "./data"
POSSIBLE_DEL = [sym for sym in os.getenv('POSSIBLE_DEL')] or [' ', ',', '|', ';', ':']
BASIS_ROWS_COUNT = int(os.getenv('BASIS_ROWS_COUNT') or 2)