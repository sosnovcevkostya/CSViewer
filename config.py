import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = os.getenv('DATA_DIR') or "./data"
POSSIBLE_DEL = [sym for sym in os.getenv('POSSIBLE_DEL')] or [' ', ',', '|', ';']