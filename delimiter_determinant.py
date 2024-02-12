import re
from config import *

class DelimeterDeterminant:
  __slots__ = 'basis_rows'
  
  def __init__(self, basis_rows):
    self.basis_rows = basis_rows

  def detect(self):
    def preproc_row(row):
      return re.sub("\".*?\"|\"\"","", row)
    
    for sym in POSSIBLE_DEL:
      occur_count = preproc_row(self.basis_rows[0]).count(sym)
      if occur_count:
          if all(preproc_row(row).count(sym) == occur_count for row in self.basis_rows):
            logging.info(f'Delimiter is determined and equals - {{{sym}}}')
            return sym
    raise RuntimeError('Unknown error during delimiter determination')
