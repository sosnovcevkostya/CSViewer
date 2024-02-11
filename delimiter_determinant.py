import re
from config import *

class DelimeterDeterminant:
  def __init__(self, file):
    self.file = file
  
  #TODO FLAG
  def get_head_rows(self, basis_rows_count=BASIS_ROWS_COUNT):
    try:
      res = [next(self.file) for _ in range(basis_rows_count)]
      self.file.seek(0) # reset data thread 
      return res
    except StopIteration:
      raise RuntimeError(
          """
          There are not enough lines in the file to determine the delimiter. 
          Try using FLAG to define delimiter manualy 
          or changing BASIS_ROWS_COUNT setting
          """
        )

  def detect(self):
    def preproc_row(row):
      return re.sub("\".*?\"|\"\"","", row)
    
    basis_rows = self.get_head_rows()
    for sym in POSSIBLE_DEL:
      occur_count = preproc_row(basis_rows[0]).count(sym)
      if occur_count:
          if all(preproc_row(row).count(sym) == occur_count for row in basis_rows):
            logging.info(f'Delimiter is determined and equals - {{{sym}}}')
            return sym
    raise RuntimeError('Unknown error during delimiter determination')
