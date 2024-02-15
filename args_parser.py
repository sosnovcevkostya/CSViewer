import re
import os
from config import *

class ArgsParser:
  __slots__ = 'show_header', 'range_from', 'range_to', 'path_to_file', 'delimiter'

  TYPE_TO_RE = {
    'num': r'\d+',
    'sym': r'\w',
    'str': r'[\a-zA-Z0-9]+'
  }
  
  def __init__(self, args) -> None:
    args = ' '.join(args) if args else ''

    self.show_header = True if '-H' in args else False
    self.range_from = self.set_arg('f', 'num', args)
    self.range_to = self.set_arg('t', 'num', args)
    self.delimiter = self.set_arg('d', 'sym', args)
    self.path_to_file = self.set_arg('p', 'str', args)

    if self.path_to_file:
      self.path_to_file = self.path_to_file.strip()

    self.validate()
    logging.info(f'CSViewer is configured with {
       {attr: getattr(self, attr) for attr in self.__dir__() if attr in self.__slots__} 
      }')

  def validate(self):
    if all(
        arg is not None for arg in [self.range_from, self.range_to]
      ) and self.range_from >= self.range_to:
      raise RuntimeError("""Range to show is not configured correctly.""")

  
  @staticmethod
  def set_arg(arg_name, arg_type, str_to_parse):
    search_res = re.search(r'\-\-' + arg_name + r'\=' + ArgsParser.TYPE_TO_RE[arg_type], str_to_parse)
    search_res = search_res.group().replace('--' + arg_name + '=', '') if search_res else None
    return int(search_res) if search_res and arg_type == 'num' else search_res