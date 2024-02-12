from config import *

class CSViewer:
  __slots__ = 'file', 'head_rows', 'data', 'settings'

  def __init__(self, file, settings=None):
    self.file = file
    self.settings = settings 
    self.data = None
    self.head_rows = None

  #TODO FLAG 
  def get_head_rows(self, basis_rows_count=BASIS_ROWS_COUNT):
    try:
      res = [next(self.file) for _ in range(basis_rows_count)]
      self.file.seek(0) # reset data thread
      self.head_rows = res 
      return res
    except StopIteration:
      raise RuntimeError(
          """
          There are not enough lines in the file to determine the delimiter. 
          Try using FLAG to define delimiter manualy 
          or changing BASIS_ROWS_COUNT setting
          """
        )