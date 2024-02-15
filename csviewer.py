import re
from config import *
from args_parser import ArgsParser
from delimiter_determinant import delimiterDeterminant

class CSViewer:
  __slots__ = 'file', 'delimiter', 'args'

  def __init__(self, file, args=None):
    self.file = file
    self.args = ArgsParser(args)
    self.delimiter = None

  def get_head_rows(self, basis_rows_count=BASIS_ROWS_COUNT):
    try:
      res = [next(self.file) for _ in range(basis_rows_count)]
      self.file.seek(0) # reset data thread
      return res
    except StopIteration:
      raise RuntimeError(
          """
          There are not enough lines in the file. Try to decrease BASIS_ROWS_COUNT setting
          """
        )
  
  def rows_gen(self):
    for row in self.file:
      yield row
  
  def parse(self):
    if not self.delimiter:
      self.delimiter = self.args.delimiter or delimiterDeterminant(
        self.get_head_rows()
      ).detect()

    counter = 0
    for row in self.rows_gen():
      line = self.split_line(row)
      if self.args.show_header and counter == 0:
        self.show_in_terminal(line)
        counter += 1
        continue
      elif counter == 0:
        self.show_in_terminal([i for i in range(len(line))])

      counter += 1

      if self.args.range_from and counter < self.args.range_from:
        continue

      if self.args.range_to and counter >= self.args.range_to:
        break

      self.show_in_terminal(line)

  #TODO other delimiter
  @staticmethod
  def split_line(row):
    return re.split(r'''((?:[^;"']|"[^"]*"|'[^']*')+)''', row)[1::2]
  
  @staticmethod
  def show_in_terminal(line):
    print('     |     '.join('{: <50}'.format(str(elem)) for elem in line))
